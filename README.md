# Similarity Search Automated!

The scripts in this repo is used for automating similarity search against a number of protein databases available online. Some of these websites require you to copy and paste the proteins' sequences manually and sometimes they can only take one input at a time! These scripts help you to automate these requests without having to input one by one which can be annoying and takes a lot of time. 

Feel free to use the scripts but, just put me in the reference! ^^

## chembl-similarity-protein.py
ChEMBL is a curated database of bioactive chemical compounds maintained by the EMBL. The script takes input from a file.

### Install requirements
pip3 install -r  requirements.txt
or
pip install -r  requirements.txt
#### Recommended: use a separate python environment before installing the requirements
1. Using python
python -m venv /path/to/new/virtual/environment.

2. Using Conda
https://saturncloud.io/blog/how-to-create-a-conda-environment-with-a-specific-python-version/


### Usage
Open the python file using a code/text editor and change the variable 'filename' to your file name.

The txt contains FASTA formatted proteins separated by 2 newline characters vvvv
```
>[string]
[protein sequence]

>[string]
[protein sequence]

....
```
file format ^^^^

For a faster version, check v2!

#### The server can be quite slow, so be patient!

## chembl_v2.py
This is the faster version of chembl-similarity-protein.py, done with asynchronous requests. Same inputs as above!


## vicmpred.py
VICMpred an SVM-based functional classification server for Gram-negative bacterial proteins that functionally classify the proteins into different categories based on amino acid composition. The script takes input from a file.

### Usage
Open the python file and put your sequencees in the 'sequences' array/list.

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