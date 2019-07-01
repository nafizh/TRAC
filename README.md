# TRAC
**TR**ansfer Learning for **A**ntibiotic Resistance Gene **C**lassification (TRAC) is a neural network based method to 
predict antibiotic resistance genes. Unlike traditional alignment based approaches such as BLAST or HMMER, TRAC uses an
alignment free approach. We show that performance of TRAC is better than the alignment based approaches. 

#### Installation

Installation of TRAC requires installation of several packages which you can do by the following steps.

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

Now, install the necessary softwares to run NeuBI with

```
$ pip install -r requirements.txt
```

Next, you need to download the neural network weights with by clicking on this 
[link](https://www.dropbox.com/sh/4qztwin2zkehmz0/AAB71w2o-vxKBGNRi709Cx-6a?dl=0). Then extract the zip file.
Make sure to move the weights_TRAC folder inside the TRAC folder.


Now, you can run TRAC against any fasta file with the following commmand

```
$ python trac.py test.fa
```

The program will output a new file that has the same name + '_ab_res_predictions_results'. This file will contain all 
the sequences from your original fasta file that have lengths of <=1600, and will assign a probability that the sequence 
is a bacteriocin. For example, a result file will have something like this

```
>EFGCFBOH_00014 Accessory gene regulator A|249|0.010913903
MNIFVLEDDFLHQTRIEKIIYKILTDNKLEVNHLEVYGKPNQLLEDISERGRHQLFFLDIDIKGEDKKGMEIAVEIRNRDPHAVIVFVTTHSEFMPVSFQYQVSALDFIDKELPEELF
SHRIEKAITYVQDNQGKTLAEDSFVFINVKSQIQVPFSDLLYIETSLIPHKLILYSTKQRVEFYGQLSEIVEQDDRLFQCHRSFVVNPYNISSIDRSERLVYLKGGLSCIVSRLKIRSLIKVV
EELHTKEK
>EFGCFBOH_00016 hypothetical protein|41|0.09664696
MNNKKTKNNFSTLSESELLKVIGGDIFKLVIDHISMKARKK
>EFGCFBOH_00019 hypothetical protein|74|0.9983411
MNTTKKQFEVIDDIKLSLMGGGSKISVGEVGQALAVCTLAGATIGSVFPIAGTLGGAVLGAQYCTGAWAIIRAH
```

When your work is done, you can deactivate the virtual environment with the following command

```
deactivate
```

If you face any problem installing the software, you can contact me through email: `nafiz dot hamid dot iut at gmail dot com`
