# TRAC
**TR**ansfer Learning for **A**ntibiotic Resistance Gene **C**lassification (TRAC) is a neural network based method to 
predict antibiotic resistance genes. Unlike traditional alignment based approaches such as BLAST or HMMER, TRAC uses an
alignment free approach. We show in our upcoming paper that performance of TRAC is better than the alignment based approaches. 


![](trac.gif)
[See as a video](https://terminalizer.com/view/017e67b82146)

#### Installation

Installation of TRAC requires installation of several packages which you can do by the following steps. First, make sure
you have python 3.6. This installation has only been tested for the 3.6 version.

First, download this repository. Then run the following commands

```
$ cd TRAC
```

We will use virtualenv to make sure the software is installed in its own sandbox, and the installation of the softwares 
needed to run TRAC do not affect the computer's default computing environment. Run

```
$ virtualenv trac_software
```

If you get an error that means virtualenv is not installed. So, do a pip installation of virtualenv.

```
$ pip install virtualenv
```

Activate the newly created virtual environment.

```
$ source trac_software/bin/activate
```

Now, install the necessary softwares to run TRAC with

```
$ pip install -r requirements.txt
```

Next, you need to download the neural network weights with by clicking on this 
[link](https://www.dropbox.com/sh/4qztwin2zkehmz0/AAB71w2o-vxKBGNRi709Cx-6a?dl=0). 

Create a weights folder inside the TRAC folder.

```
$ mkdir weights_TRAC
$ cd weights_TRAC
$ mkdir models
```

Move the downloaded zip folder to the newly created folder.

```
$ mv ~/Downloads/weights_TRAC.zip weights_TRAC/models/
```

Unzip the folder.

```
$ cd weights_TRAC/models/
$ unzip weights_TRAC.zip
$ cd ../../
```

Now, you can run TRAC against any fasta file with the following commmand

```
$ python trac.py test.fa
```
If there is an error of CUDA being out of memory, you can reduce the batch size at line 75 of the `trac.py` file, and
try again.


The program will output a new file that has the same name + '_ab_res_predictions_results'. This file will contain all 
the sequences from your original fasta file that have lengths of <=1600, and will assign an atibiotic at the end of
the desciption of each protein sequence. For example, a result file will have something like this with the predicted
antibiotic at the end of the description.

```
>gi|1559613023|ref|WP_128268288.1| quinolone resistance pentapeptide repeat protein QnrS15 [Escherichia coli]|MULTIDRUG
METYNHTYRHHNFSHKDLSDLTFTACTFIRSDFRRANLRDTTFVNCKFIEQGDIEGCRFDVADLRDASFQQCQLAMANFSNANCYGIEFRACDLKGANFSRTNFAHQVSNRMYFCSAFISGCNLSYANMERVCLEKCELFENRWIGTNLAGASLKESDLSRGVFSEDVWGQFSLQGANLCHAELDGLDPRKVDTSGIKIAAWQQELILEALGIVVYPD
>gi|1559613022|ref|WP_128268287.1| subclass B1 metallo-beta-lactamase VIM-62 [Pseudomonas putida]|GLYCOPEPTIDE
MFKLLSKLLVYLTASIMAIASPLVFSVDSSGEYPTVSEIPVGEVRLYQIADGVWSHIATQSFDGAVYPSNGLIVRDGDELLLIDTAWGAKNTAALLAEIEKQIGLPVTRAVSTHFHDDRVGGVDVLRAAGVATYASPSTRRLAEVEGNEIPTHSLEGLSSSGDAVRFGPVELFYPGAAHSTDNLVVYVPSASVLYGGCAIYELSRTSAGNVADADLAEWPTSIERIQQHYPEAQFVIPGHGLPGGLDLLKHTTNVVKAHTNRSVVE
>gi|1559613021|ref|WP_128268286.1| class A extended-spectrum beta-lactamase VEB-20 [Pseudomonas aeruginosa]|GLYCOPEPTIDE
MKIVKRILLVLLSLFFTVVYSNAQTDNLTLKIENVLKAKNARIGVAIFNSNEKDTLKINNDFHFPMQSVMKFPIALAVLSEIDKGNLSFEQKIEITPQDLLPKTWSPIKEEFPNGTTLTIEQILNYTVSESDNIGCDILLKLIGGTDSVQKFLNANHFTDISIKANEEQMHKDWNTQYQNWATPTAMNKLLIDTYNNKNQLLSKKSYDFIWKIMRETTTGSNRLKGQLPKNTIVAHRTGTSGINNGIAAATNDVGVITLPNGQLIFISVFVAESKETSEINEKIISDIAKITWNYYLNK
>gi|1559612971|ref|WP_128268236.1| class C beta-lactamase DHA-28 [Morganella morganii]|RIFAMYCIN
MTKSLSATLISALLAFSAPGFSAADNVAAVVDSTIKPLMAQQDIPGMAVAVSVKGKPYYFNYGFADVQAKQPVTENTLFELGSVSKTFTGVLGAVSVAKKEMTLNDPAAKYQPELALPQWKGITLLDLATYTAGGLPLQVPDAVKNRADLLNFYQQWQPSWQPGDMRLYANSSIGLFGALTANAAGMPYEQLLTARILAPLGLSHTFITVPESAQSQYAYGYKNKKPVRVSPGQLDAESYGVKSASKDMLRWAEMNMEPSRTGNADLEMAMYLAQTRYYKTVAINQGLGWEMYDWPQQKDMIINGVTNEVALQPHPVTDNQVQPYNRASWVHKTGATTGFGAYVAFIPEKQVAIVILANKNYPNTERVKAAQAILSALE
>gi|1559612969|ref|WP_128268234.1| CMY-2 family class C beta-lactamase CFE-2 [Citrobacter freundii]|RIFAMYCIN
MMKKSICCALLVTASLSTFAADKTEQQIADIVNRTITPLMQEQAIPGMRFAIIYQGKPYYFTWGKADIANDRPVTRQTLFELGSVSKTFNGVLGGDAIARGEIKLSDPVTQYWPKLTGKQWLGISLLHLATYTAGGLPLQVPDDVTDKAALLRFYQNWQPQWAPGAKRLYANPSIGLFGALAVKPSGMGYEEAMTKRVLQPLKLAHTWITVPQSEQKDYALGYREGRPVHVSPGQLDAEAYGVKSSLVDMTRWIQANMDASQVQEKTLRQGIEIAQARYWHIGDMYQGLGWEMVNWPVNADSIINGSDSKVALAALPAVEVNPPAPAVKASWVHKTGTSGGFGTYVALVPEKNLVGMMLANKSYPKPARVEAAWRILEKLQ

```

When your work is done, you can deactivate the virtual environment with the following command

```
deactivate
```

If you face any problem installing the software, you can contact me through email: `nafiz dot hamid dot iut at gmail dot com`
