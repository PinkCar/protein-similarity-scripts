# Similarity Search Automated!

The scripts in this repo is used for automating similarity search against a number of protein databases available online. Some of these websites require you to copy and paste the proteins' sequences manually and sometimes they can only take one input at a time! These scripts help you to automate these requests without having to input one by one which can be annoying and takes a lot of time. 

## chembl-similarity-protein.py
ChEMBL is a curated database of bioactive chemical compounds maintained by the EMBL. The script takes input from a file.

The txt contains FASTA formatted proteins separated by 2 newline characters vvvv
```
>[string]
[protein sequence]

>[string]
[protein sequence]

....
```
file format ^^^^

## vicmpred.py
VICMpred an SVM-based functional classification server for Gram-negative bacterial proteins that functionally classify the proteins into different categories based on amino acid composition. The script takes input from a file.

The txt contains FASTA formatted proteins separated by 2 newline characters vvvv
```
>[string]
[protein sequence]

>[string]
[protein sequence]

....
```
file format ^^^^

The output is the virulence prediction as provided by VFDB.