#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python



# This program just takes in a file that I have on my computer so that I could practice BLASTing from python.
# I know that I will need to adjust this when we make our own database, but I
# wanted to get started on practicing the code even before the database was constructed


from Bio.Blast import NCBIWWW  # Used to access BLAST online
from Bio.Blast import NCBIXML  # Used to parse the BLAST output
from Bio import SeqIO  # Used to read the fasta file provided
# import os


def parsefile(blast_record, writer):  # This function writes the desired information to the final file
    # This method works, I'm just having trouble reading in multiple FASTA sequences for BLASTing
    alignment = blast_record.alignments[0] # Retrieves the best hit (first alignment)
    for hsp in alignment.hsps: # Retrieves all locations in the best hit
        # Add a way to label each result with the corresponding microRNA
        # Add a way to compensate for an empty result (no matches)
        s = alignment.title
        l = s.split("|")
        s = l[4].strip()
        l = s.split(" ")
        s = l[0] + ' ' + l[1] + ' ' + l[2] # Finalized organism name
        writer.write(s + '\t' + str(hsp.query_start) + '\t' + str(hsp.query_end) + '\t' + str(hsp.sbjct_start) +
                     '\t' + str(hsp.sbjct_end) + '\n') # Writes the information Reddy Wants
    writer.write('\n') # Writes an extra line break so that eventaully we can write multiple sequences
# We may have to separate by a different character/string so that we can parse individual
# results in the future better


def main():
    
    query = input('Enter query file name: ') # For the working example, type in 'Test_miRNA.txt'
    records= list(SeqIO.parse(query, "fasta"))
    #record = SeqIO.read(query, format="fasta")
    filename = input('What is your desired file name for the top hits file? ') # I used 'Test_miRNA_Results.txt'
    writer = open(filename, 'w')
    writer.write('Organism_name' + '\t' + 'Query_start' + '\t' + 'Query_end' + '\t' + 'Subject_start' + '\t' +
                 'Subject_end' + '\n') # Writes the header for the results file
    print('Now BLASTing')
    for record in records:
        result_handle = NCBIWWW.qblast("blastn", "nt", record.format('fasta'))  # BLASTs against the nt database
        blast_record = NCBIXML.read(result_handle) #Makes the BLAST results able to be processed
        parsefile(blast_record, writer) # Writes the information that we want
                 
                 # The below commented lines are goign to be used to parse each blast_record
                 # We can use those ines after we figure out how to BLAST multiple sequences....
                 # blast_records = NCBIXML.parse(result_handle)  # NCBIXML.parse() is used for parsing through multiple BLAST results
                 # for blast_record in blast_records:
                 #     parsefile(blast_record, writer)
                 
    print("Finished!")
    writer.close()

main()

# Still need to work on iterating through each microRNA and how to organize each of those (Perhaps we can pass in the
# writer for the file, in the main we can make the header and comments for the text file and then the function itself
# is what takes the information)

# Below are lines used for our eventual local blast
# database = input('enter path to local blast database')  # input blast database to blast query against
# query = input('enter the path to the query fasta file: ')  # input query fasta file (in our case, the miRNA)
# output = input('what is your desired output path?')  # where should results go? output as text file
# filename = input('what is your desired file name for the BLAST results? *please make it a .XML*')
# run = "blastn -db " + database + "-query " + query + "-out " + output  # how run would appear in commandline
# os.chdir(output)
# result_handle = open(filename)
# os.system(run)  # run through commandline (Saves the blast record)