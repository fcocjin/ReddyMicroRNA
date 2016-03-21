#This program just takes in a file that I have on my computer so that I could practice BLASTing from python.
#I know that I will need to adjust this when we make our own database, but I
#wanted to get started on practicing the code even before the database was constructed
from Bio.Blast import NCBIWWW #Used to access BLAST online
from Bio.Blast import NCBIXML #Used to parse the BLAST output
from Bio import SeqIO #Used to read the fasta file provided
record = SeqIO.read("pmrA_Test.fasta", format = "fasta")
print("record = " + record) #Made sure the record was correct
result_Handle = NCBIWWW.qblast("blastn", "nt", record.seq) #BLASTs against the nt database
##writer = open("pmrA_Results.txt", "w") #I will practice writing to file later
print("Here!") #Marks that the BLAST has been performed
blast_record = NCBIXML.read(result_Handle)
E_VALUE_THRESH = 0.04 #Copied the next lines from the BioPython cookbook for practice
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            s = alignment.title
            l = s.split("|")
            s = l[4].rstrip()
            l = s.split(" ")
            s = l[0] + ' ' + l[1] + ' ' + l[2] #????
            print('Organism:', s)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print(hsp.query[0:75])
            print(hsp.match[0:75])
            print(hsp.sbjct[0:75])
            print('query start:', hsp.query_start) #These lines are really what Reddy wants
            print('query end:', hsp.query_end)
            print('subject_start:', hsp.sbjct_start)
            print('subject_end:', hsp.sbjct_end)
            break #I only wanted to test against one BLAST result so I broke out of the provided loop
        break
    break

print("Finished!")
