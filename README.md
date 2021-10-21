# PharmaTrue2

The PharmaTrue2 repo contains a file named "hi.py", alongside supplementary information regarding pharmacogenomic indicators, which can be used to produce a (genetically) personalized list of potentially problematic pharmaceutical substances, on the basis of direct-to-consumer 23andMe genomic reports (which indicate Single-nucleotide polymorphisms - SNPs).

NOTE: 23andMe reports should not be used to make medical decisions - this must always be done in consultation with licensed medical professionals. This repository, along with your 23andMe report might, however, serve to start such a discussion. 

First, clone this repo by executing the following command in your terminal:
git clone https://github.com/sijaric/PharmaTrue2.git

After downloading your 23andMe raw data (txt file) from the official 23andMe website and renaming it to "genome.txt", you can add it to the PharmaTrue2 directory.

Finally, you run the "hi.py" script using the following command in the zsh terminal (after navigating to the PharmaTrue2 directory):
python3 hi.py

The above assumes that you have python and pandas installed. 

### A list of your potentially genetically incompatible pharmaceutical substances will be displayed in the terminal, on the basis of your  23andMe genomic report. 

### PharmGKB is the source of the "var_pheno_ann.tsv" file, which indicates associations between nsSNVs and their drug response phenotypes, along with information on the drug involved.


