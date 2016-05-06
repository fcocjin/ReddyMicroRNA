# **AvianScreen: A miRNA Screening Tool**
---
#####
##### Created By: Amani Almatrafi, Kelly Boyd, Francis Cocjin and Michael Courtois 
##### Loyola Univerisity Chicago: Department of Biology and Computer Science
##### COMP 383: Computational Biology | Spring 2016 | Dr. Heather E. Wheeler 
#
![LUC](http://www.luc.edu/media/home/images/loyola-logo-tag.png)

---
# Table of Contents
* [Introduction](#introduction)
* [Quick Start](#quickstart)
* [Setup](#setup)
    * [Hardware Requirements](#hardware)
    * [Software Requirements](#software)
* [Instructions](#instructions)
    * [Overview](#overview)
    * [Input 1: miRNA Sequences](#input1)
    * [Input 2: Genomic Database](#input2)
    * [Output](#output)
    * [GUI](#gui)
    * [Command Line](#commandline)
___

# Introduction <a id="introduction"></a>

Welcome to AvianScreen! AvianScreen is a python-based application for screening microRNAs against avian genomes.  This program originated as a project from [Dr. Reddy's Lab](http://www.reddylab.com/index.html) at Loyola University Chicago in collaboration with [Dr. Wheeler's](https://hwheeler01.github.io/) Computation Biology class.

MicroRNAs (miRNAs) are regulatory ribonucleic acids, ~22 nucleotides in length, common to plants and animals that serve in gene silencing and regulating post-transcriptional gene expression.  Due to their low-mutation rate and high evolutionary conservation, miRNAs serve as effective markers in phylogenetic studies.  Unfortunately, there is a severe annotation bottleneck of miRNA data, especially in class Aves.  Many computational tools such as _miRExplorer_ that exist discover new miRNA sequences _in silico_ based on physical characteristics.  However, their _in silico_ screening techniques of miRNAs are not favorable for miRNA screening and phylogenetic analysis of avian genomes. Using a local blast index of precursor and mature miRNA sequences of _Gallus gallus_ and _Taeniopygia guttata_ from miRBase, we have developed a tool to screen unannotated avian genomes of interest to identify novel and pre-existing miRNAs sequences and assist in performing phylogenetic analysis.  The python-based tool takes advantage of BioPython modules for simple data parsing and BLAST compatibility.  Run-time and memory usage are consistent with other BLAST applications of this nature when tested against pre-existing data for _Gallus gallus_.


For additional background and detailed information on our application please view the [application note].
___

# Quick Start <a id="quickstart"></a>

MicroRNA AvianScreen can be used either through command line or GUI.  However, before you begin please make sure you have the proper hardware and software requirements needed to run the program.  This information can be found in the Setup section of this document.  Detailed instructions on how to use AvianScreen can be found in the Instructions section of this document.  With all relevant files in the current directory, run the `miRNA_Finder.py` through a python terminal and follow the program prompts. 
___

# Setup <a id="setup"></a>

##### Hardware Requirements <a id="hardware"></a>
This program can work on any Windows or Mac machine with average RAM and processing cababilities. For simplicity's sake, any command line instructions found in this document will follow syntax for Mac machines. 

##### Software Requirements <a id="software"></a>

In order for the program to run you must have BLAST+, Python 2.7 or above, and the MicroRNA AvianScreen python scripts.  
* BLAST+
    * Before you begin you must have BLAST Command Line Applications (BLAST+) downloaded on your computer.  Proper installation instructions can be found [here](http://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download).  For reference, the BLAST+ User Manual can be found [here](http://www.ncbi.nlm.nih.gov/books/NBK279690/). 
* Python 2.7.11
    * This code was created and tested using Python 2.7.  DISCLAIMER: The program has not been tested or used on other versions of Python.  User may run into some syntatical issues using other versions of Python. These issues should be easy to fix.  Detailed information on the syntax of the code is included in this ReadMe file for your convience. 
    * The [Python](https://www.python.org/) website has detailed information on the Python programming language.  Python 2.7.11 installation instructions can be found [here](https://www.python.org/downloads/release/python-2711/).
* MicroRNA AvianScreen Scripts
    * All files and scripts needed to run AvianScreen can be found on this [GitHub](https://github.com/fcocjin/ReddyMicroRNA.git).  The program can either be run using command line or the provided GUI. 
    * The python scripts neededed are:
        * `miRNA_Finder.py`
        * _genus_species.fasta_
        * _genus_species.db_
    * Please view the **Instructions** section for additional information on program scripts.
___

# Instructions <a id="instructions"></a>

Once you have the proper software downloaded on your computer, you are ready to begin! There are two ways to run AvianScreen, through the GUI or command line. The GUI provides full functionality and is geared towards the average user.  More experienced users and programmers, however, may find command line easier and more robust to use. 

### Overview <a id="overview"></a>

AvianScreen takes in miRNA sequences, either precursor or mature, from avian species and BLASTs the query against unannotated avian genomes.  Three files are outputted containing the BLAST results.  One file contains the complete BLAST results from the program.  The other files relay the top 100 hits to the user and genomic locations for reference.    

### Input 1: miRNA Sequences <a id="input1"></a>

AvianScreen takes in precursor or mature miRNA sequences in FASTA format.  Some miRNA sequence files have already been included in the GitHub for your use and are detailed below.  The following input files were collected from [miRBase](http://www.mirbase.org/).  You can create your own input FASTA files to really take advantage of AvianScreen.

| File | Description | 
| ---- | ----------- | 
| `gg_pre_mirna_short.fasta` | A FASTA file consisting of three records from the Gallus gallus miRBase database for testing purposes. |
| `gg_pre_mirna.fasta` | FASTA file consisting of [740 precursor miRNA sequences from Gallus gallus miRBase database](http://www.mirbase.org/cgi-bin/mirna_summary.pl?org=gga). Scroll to bottom of page to fetch precursor sequences. |
| `gg_mat_mirna.fasta` | FASTA file consisting of [994 mature miRNA sequences from Gallus gallus miRBase database](http://www.mirbase.org/cgi-bin/mirna_summary.pl?org=gga). Scroll to bottom of page to fetch mature sequences.  |
| `tg_pre_mirna.fasta` | FASTA file consisting of [247 precursor miRNA sequences from Taeniopygia guttata miRBase database](http://www.mirbase.org/cgi-bin/mirna_summary.pl?org=tgu). Scroll to bottom of page to fetch precursor sequences.  |
| `tg_mat_mirna.fasta` | FASTA file consisting of [334 mature miRNA sequences from Taeniopygia guttata miRBase database](http://www.mirbase.org/cgi-bin/mirna_summary.pl?org=tgu). Scroll to bottom of page to fetch mature sequences.  |

Format: Each file is FASTA format.  Each record consists of two lines.  Each new record is denoted by a '>' followed by the miRBase ID and then accession number.  The second line contains the actual miRNA sequence.   

Example input files, used for testing and initial research, described above can be found [here](https://drive.google.com/folderview?id=0B51XeDdO69cnR1FoSU1nc0pkbWs&usp=sharing#grid).

### Input 2: Genomic Database <a id="input2"></a>

In addition, AvianScreen takes in a unannotated database created through BLAST+.  The program comes standard with some databases detailed below or the program can take in your own database.  If you do not have a database, AvianScreen can create a database from the FASTA file of your choice.  If no database is selected, the program will default to the Gallus gallus database provided.  HINT: Only one database can be accepted as input.  Please append all records from multiple organisms into one file in order to create a properly formatted database.  

| File | Description |
| ---- | ----------- |
| Database Files | When creating a local BLAST database from a FASTA file, three files are created with the extensions .nhr, .nin, .nsq. Each file is necessary for the program to work and none should be discarded.  Each file type is explained in detail below using Gallus_gallus.fasta as an input.
| `gg_db.nhr` | The header file of the locally created Gallus gallus database. |
| `gg_db.nin` | The index file of the locally created Gallus gallus database. |
| `gg_db.nsq`| The sequence file of the locally created Gallus gallus database. |
|`scamelus_genome.fasta` | This FASTA file contains the full, transcripted genome sequence data for _Struthio camelus_.  It serves as an example input file that AvianScreen can turn into a database.  |

Example input files, used for testing and initial research, described above can be found [here](https://drive.google.com/folderview?id=0B51XeDdO69cnR1FoSU1nc0pkbWs&usp=sharing#grid). 

### Output <a id="output"></a>

Once the program receives the necessary input and user parameters, it will begin to BLAST the miRNA sequences against the database.  Once completed, three files will be outputted.  These files are described in greater detail below.  The program will ask append a result name to the query FASTA file to denote the results.  The user chooses the file path in which the files are stored. Examples are detailed below with the `gg_pre_mirna_short.fasta` file.    

| File | Description | 
| ---- | ----------- | 
| `gg_pre_mirna_short_locations.txt` | A text file that possesses the locations of the BLAST hits for referencing. | 
| `gg_pre_mirna_short_results.txt` | A text file that shows the top 100 most frequent miRNAs found in order from most frequent to least frequent. Each result also lists the number of times each miRNA is found. |
| `gg_pre_mirna_short_results.txt`| A text file that holds the full BLAST results from the program.  WARNING: The file will be the largest file ranging from tens to hundreds of thousands of hits. |

Example output files, used for testing and initial research, described above can be found [here](https://drive.google.com/folderview?id=0B51XeDdO69cnUGdwWmE5Y3d3elU&usp=sharing&tid=0B51XeDdO69cnR1FoSU1nc0pkbWs#grid).

### GUI <a id="gui"></a>

The GUI provides full AvianScreen functionaltiy in a easy, user-friendly means. To load the GUI, HOLD. Once the GUI application is open, use the dropdown menus to select the appropriate input files.     

### Command Line <a id="commandline"></a>

To run the program, open a terminal window and change the current directory to the file path where your miRNA files are. Make sure all relevant files (such as the three database files and the genomic of miRNA FASTA files) are stored in this location on your computer. The program will not run correctly unless this is done.    

`cd /Users/Francis/Desktop/ReddyMicroRNA`

Once the directory is changed, you need to initiate Python and AvianScreen. Enter "python miRNA_Finder.py" to run the file.

`python miRNA_Finder.py`

The program will then prompt the user:
>Do you need to make a BLAST database? Please type Yes or No:

If a "Yes" is registered, the program will prompt you for the path to the FASTA file to make the database from.
>Please type the full path to the fasta file you wish to use:

`/Users/Francis/Desktop/ReddyMicroRNA/scamelus.fasta`

Next, enter the type of database following the prompt:
>Please input the database type (prot for protein or nucl for nucleotide): 

`nucl`

The program will then prompt the user for an output destination where they would like to store the files:
>Please enter the full path to the output destination:

`/Users/Francis/Desktop/ReddyMicroRNA/scamelus`

Next, AvianScreen allows you to name the database you just created. This name must match the file input name. See the example below: 
>Please enter the name of your database: 

`scamelus`

If a "No" or no response is registered for creating the database, the program will automatically select the Gallus gallus database to use. Next, the program will ask the user for their ideal cutoffs for query coverage and percent identity.
>What is your ideal cutoff query coverage? What is your ideal cutoff percent identity?

If no value is entered, default values will be used:
>Since no value was inputted, BLAST will not filter by query coverage 

>Since no value was inputted, BLAST will not filter by percent identity

Next, the program will ask about E-value:
>What is your ideal cutoff E-value?

If no value is entered, default values will be used:
>Since no value was inutted, BLAST will choose a max E-value of 10

Enter the genus and species of the organism for the file type:
>What organism's genome is represented by the BLAST database? (No spaces please): 

`Struthio_camelus`

Once the parameters have been set, the program will begin to BLAST the query against the selected database.
>Now BLASTing 

The program will return a statement telling when the BLAST has been completed and file parsing has begun and completed.
>BLAST completed, now parsing file 

>Finished!

The program will then output two files when completed.
>gg_pre_mirna_short_locations.txt will hold the locations for referencing

>gg_pre_mirna_short_results.txt will present the top 100 most frequent miRNAs in order

>gg_pre_mirna_short_full_BLAST_result.txt will hold the full BLAST result









