import warnings
warnings.filterwarnings('ignore')

from fastai import *
from fastai.text import *
from Bio import Seq
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import FeatureLocation, CompoundLocation

import pandas as pd
import numpy as np

from utils import *

path = Path('weights_TRAC/')
utility_path = Path('util_files')
voc = np.load(path/'bact_vocab.npy')
model_vocab = GenomicVocab(voc)

TOTAL_CLASSES = 16
ab_res_class_dict = {0:'BETA-LACTAM', 1:'AMINOGLYCOSIDE', 2:'TETRACYCLINE', 3:'GLYCOPEPTIDE', 
                     4:'PHENICOL', 5:'FOLATE-SYNTHESIS-INHABITOR', 6:'RIFAMYCIN', 7:'TRIMETHOPRIM', 
                     8:'SULFONAMIDE', 9:'MACROLIDE', 10:'FOSFOMYCIN', 11:'QUINOLONE', 
                     12:'STREPTOGRAMIN', 13:'MACROLIDE/LINCOSAMIDE/STREPTOGRAMIN', 
                     14: 'MULTIDRUG', 15: 'BACITRACIN'}
                     
                     
def create_csv_file(file_name):
    """
    Takes a fasta file and create the csv file from it
    """
    out_handle = open(file_name + '_ab_res_purpose.csv', 'w')
    out_handle.write('Sequence,antibiotic,set\n')
    for record in SeqIO.parse(file_name, 'fasta'):
        out_handle.write("%s,0,inference\n" % (record.seq))
    out_handle.close()
    
def load_model_encoder():
    """
    Loads the pretrained and finetuned encoder
    """
    classification_df = pd.read_csv(utility_path/'coala_transfer_learning_ml_set_cd_hit_0.7_fold_number_1_of_10.csv')
    train_df = classification_df[classification_df.set == 'train']
    valid_df = classification_df[classification_df.set == 'test']
    tok = Tokenizer(GenomicTokenizer, n_cpus=1, pre_rules=[], post_rules=[], 
                special_cases=['xxpad'])
    data_clas = GenomicTextClasDataBunch.from_df(path, train_df, valid_df, tokenizer=tok, 
                                             vocab=model_vocab,
                                            text_cols='Sequence', label_cols='antibiotic', 
                                             bs=32)
    clas_config = dict(emb_sz=400, n_hid=1150, n_layers=3, pad_token=0, qrnn=False, output_p=0.4, 
                       hidden_p=0.2, input_p=0.6, embed_p=0.1, weight_p=0.5)
    drop_mult = 0.5
    learn = get_model_clas(data_clas, drop_mult, clas_config)
    learn.load_encoder('bact_finetune_enc_cd_hit_0.7')
    return learn

def model_run(target_fasta):
    """
    Runs all 10 models and build a soft majority voting classifier
    """
    print ("\n")
    print ("Loading pretrained and finetuned Encoder")
    learn = load_model_encoder()
    classification_df = pd.read_csv(target_fasta + '_ab_res_purpose.csv')
    train_df = classification_df[classification_df.set == 'inference']
    valid_df = classification_df[classification_df.set == 'inference']
    tok = Tokenizer(GenomicTokenizer, n_cpus=1, pre_rules=[], post_rules=[], 
                special_cases=['xxpad'])
    data_clas = GenomicTextClasDataBunch.from_df(path, train_df, valid_df, tokenizer=tok, 
                                             vocab=model_vocab,
                                            text_cols='Sequence', label_cols='antibiotic', 
                                             bs=32)
    learn.data = data_clas
    total = torch.zeros(len(valid_df), TOTAL_CLASSES)
    print ("\n")
    print ("Running 10 models and building a soft majority voting classifier to get predictions")
    for index in range(0, 10):
        print ("Running model %d" % (index+1))
        learn.load('learn_model_cd_hit_0_7_for_loop_fold_%d_label_smoothing_all_freeze.pth' % (index + 1))
        val_preds = learn.get_preds(DatasetType.Valid)
        total = total + val_preds[0]
        
    predictions = np.argmax(total/TOTAL_CLASSES, axis = 1)
    return predictions
    
def build_result_file(target_fasta, predictions):
    """
    Builds the result file
    """
    out_handle = open(target_fasta + '_ab_res_predictions_results', 'w')
    for index, record in enumerate(SeqIO.parse(target_fasta, 'fasta')):
        out_handle.write('>%s|%s\n%s\n' % (record.description, ab_res_class_dict[predictions[index].item()], 
                                         record.seq))
    out_handle.close()
        
    
if __name__ == '__main__':
    #print ('hello world')
    target_fasta = sys.argv[1] 
    print ("\n")
    print ("Creating a csv file for doing prediction!")
    create_csv_file(target_fasta)
    
    print ("Starting prediction!!")
    predictions = model_run(target_fasta)
    
    print ("Building the result fasta file!!!")
    build_result_file(target_fasta, predictions)
    
    print ("\n")
    print ("Done!!!!")
    
    
    
    
    
    
    
    
    
    
    
