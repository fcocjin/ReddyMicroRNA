#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python


# This program takes in a fasta file of miRNA sequences and BLASTs it against a given database
# The parsing method is included to pull out subject locations of each BLAST result


from Bio.Blast import NCBIXML  # Used to parse the BLAST output
from Bio import SeqIO
import os


def parsefile(blast_record, writer, query_ID, percent_identity, query_coverage):  # This function writes the desired information to the final file
    if len(blast_record.alignments) != 0: # Prevents an error from occurring if there is no BLAST match
        alignment = blast_record.alignments[0] # Retrieves the best hit (first alignment)
        for hsp in alignment.hsps: # Retrieves all locations in the best hit
            coverage = float(float(hsp.align_length)/float(blast_record.query_length))  # Calculates query coverage
            p_identity = float(float(hsp.identities)/float(hsp.align_length))  # Calculates percent identity
            if (p_identity >= percent_identity) and ((hsp.query_start != hsp.sbjct_start) and
                (coverage >= query_coverage)):
                s = alignment.title
                l = s.split("|")
                s = l[2]
                l1 = s.split(" ")
                s = l1[2] + ' ' + l1[3] # Finalized organism name
                writer.write(query_ID + ',' + s + ',' + str(hsp.query_start) + ',' + str(hsp.query_end) + ',' +
                             str(hsp.sbjct_start) + ',' + str(hsp.sbjct_end) + '\n')
            # Writes the location of the subject hit


def main():
    
    query = input('Enter query file name: ')  # For the working example, type in 'gg_pre_mirna_short.fasta'
    locationsFilename = query[0:len(query)-6] + '_locations' + query[len(query)-6:len(query)]
    query_coverage = input('What is your ideal cutoff query coverage?')  # I will use this later to filter results
    percent_identity = input('What is your ideal cutoff percent identity')  # same as above
    records = SeqIO.parse(query,'fasta')  # Retrieves miRNA ID's
    queryList = []  # Stores miRNA ID's
    for record in records:
        queryList.append(record.id)
    writer = open(locationsFilename, 'w')
    writer.write('query_miRNA_ID' + ',' 'Organism_name' + ',' + 'Query_start' + ',' + 'Query_end' + ',' +
                 'Subject_start' + ',' + 'Subject_end' + '\n')  # Writes the header for the results file
    print('Now BLASTing')
    os.system('blastn -task blastn-short -query ' + query + ' -db Input/tg_db -out BLAST_result.xml -num_threads 8 '
                                                            '-outfmt "5" ')
    print('BLAST completed, now parsing file')
    result_handle = open('BLAST_result.xml')
    blast_records = NCBIXML.parse(result_handle)
    recordCount = 0
    for blast_record in blast_records: # Writes a result for each miRNA BLASTed
        parsefile(blast_record,writer,queryList[recordCount], percent_identity, query_coverage)
        recordCount += 1
    writer.close()
    print('Finished!')

main()
