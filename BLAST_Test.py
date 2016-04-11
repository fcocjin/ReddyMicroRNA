#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python


# This program takes in a fasta file of miRNA sequences and BLASTs it against a given database
# The parsing method is included to pull out subject locations of each BLAST result


from Bio.Blast import NCBIXML  # Used to parse the BLAST output
from Bio import SeqIO
import os


def parsefile(blast_record, writer):  # This function writes the desired information to the final file
    if len(blast_record.alignments) != 0: # Prevents an error from occurring if there is no BLAST match
        alignment = blast_record.alignments[0] # Retrieves the best hit (first alignment)
        for hsp in alignment.hsps: # Retrieves all locations in the best hit
            # if (hsp.identities >= percent_identity): # and (hsp.query_start != hsp.sbjct_start): and
            #  (hsp.query >= query_coverage)
                s = alignment.title
                l = s.split("|")
                s = l[2]
                l1 = s.split(" ")
                s = l1[2] + ' ' + l1[3] # Finalized organism name
                writer.write(s + '\t' + str(hsp.query_start) + '\t' + str(hsp.query_end) + '\t' + str(hsp.sbjct_start) +
                             '\t' + str(hsp.sbjct_end) + '\n') # Writes the location of the subject hit
    writer.write('\n')


def main():
    
    query = input('Enter query file name: ')  # For the working example, type in 'gg_pre_mirna_short.fasta'
    filename = input('What is your desired file name for the top hits file? ')  # 'gg_pre_mirna_short_results.fasta
    # query_coverage = input('What is your ideal cutoff query coverage?')  # I will use this later to filter results
    # percent_identity = input('What is your ideal cutoff percent identity')  # same as above
    records = SeqIO.parse(query,'fasta')  # Retrieves miRNA ID's
    queryList = []  #Stores miRNA ID's
    for record in records:
        queryList.append(record.id)
    writer = open(filename, 'w')
    writer.write('Organism_name' + '\t' + 'Query_start' + '\t' + 'Query_end' + '\t' + 'Subject_start' + '\t' +
                 'Subject_end' + '\n') # Writes the header for the results file
    print('Now BLASTing')
    os.system('blastn -task blastn-short -query ' + query + ' -db Input/gg_db -out BLAST_result.xml -num_threads 8 '
                                                            '-outfmt "5" ')
    print('BLAST completed, now parsing file')
    result_handle = open('BLAST_result.xml')
    blast_records = NCBIXML.parse(result_handle)
    recordCount = 0
    for blast_record in blast_records: # Writes a result for each miRNA BLASTed
        writer.write('\r' + '*' + queryList[recordCount] + '*' + '\n')  # Labels the BLAST results
        parsefile(blast_record,writer)
        recordCount += 1
    writer.close()
    print('Finished!')

main()
