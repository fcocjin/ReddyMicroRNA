# This program just takes in a file that I have on my computer so that I could practice BLASTing from python.
# I know that I will need to adjust this when we make our own database, but I
# wanted to get started on practicing the code even before the database was constructed
# from Bio.Blast import NCBIWWW  # Used to access BLAST online
# from Bio import SeqIO  # Used to read the fasta file provided

from Bio.Blast import NCBIXML  # Used to parse the BLAST output
import os


def parsefile(blast_record):
    # record = SeqIO.read("pmrA_Test.fasta", format="fasta")
    # print("record = " + record)  # Made sure the record was correct
    # result_Handle = NCBIWWW.qblast("blastn", "nt", record.seq)  # BLASTs against the nt database
    # writer = open("pmrA_Results.txt", "w") #I will practice writing to file later
    # print("Here!")  # Marks that the BLAST has been performed
    # blast_record = NCBIXML.read(result_Handle)

    alignment = blast_record.alignments[0]
    filename = input('what is your desired file name for the top hits file?')
    writer = open(filename, 'w')
    writer.write('Organism_name' + '\t' + 'Query_start' + '\t' + 'Query_end' + '\t' + 'Subject_start' + '\t' + 'Subject_end')
    for hsp in alignment.hsps:
        # Add a way to label each result with the corresponding microRNA
        # Add a way to compensate for an empty result (no matches)
        s = alignment.title
        l = s.split("|")
        s = l[4].rstrip()
        l = s.split(" ")
        s = l[0] + ' ' + l[1] + ' ' + l[2]  # ???? This was including a weird 'u'
        writer.write(s + '\t' + hsp.query_start + '\t' + hsp.query_end + '\t' + hsp.sbjct_start + '\t' + hsp.sbjct_end )
    print("Finished!")


def main():
    database = input('enter path to local blast database')  # input blast database to blast query against
    query = input('enter the path to the query fasta file')  # input query fasta file (in our case, the miRNA)
    output = input('what is your desired output path?')  # where should results go? output as text file
    filename = input('what is your desired file name for the BLAST results? *please make it a .XML*')
    run = "blastn -db " + database + "-query " + query + "-out " + output  # how run would appear in commandline
    os.chdir(output)
    result_handle = open(filename)
    os.system(run)  # run through commandline (Saves the blast record)
    blast_record = NCBIXML.read(result_handle)
    parsefile(blast_record)
# Still need to work on iterating through each microRNA and how to organize each of those (Perhaps we can pass in the
# writer for the file, in the main we can make the header and comments for the text file and then the function itself
# is what takes the information)
