#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python



# This program just takes in a file that I have on my computer so that I could practice BLASTing from python.
# I know that I will need to adjust this when we make our own database, but I
# wanted to get started on practicing the code even before the database was constructed


from Bio.Blast import NCBIXML  # Used to parse the BLAST output
import os


def parsefile(blast_record, writer):  # This function writes the desired information to the final file
    alignment = blast_record.alignments[0] # Retrieves the best hit (first alignment)
    for hsp in alignment.hsps: # Retrieves all locations in the best hit
        # Add a way to label each result with the corresponding microRNA
        # Add a way to compensate for an empty result (no matches)
        s = alignment.title
        print ('query = ' + hsp.query)
        print ('s = ' + s)
        l = s.split("|")
        s = l[2]
        l1 = s.split(" ")
        # l1[1] = ID
        s = l1[2] + ' ' + l1[3] # Finalized organism name
        writer.write(s + '\t' + str(hsp.query_start) + '\t' + str(hsp.query_end) + '\t' + str(hsp.sbjct_start) +
                     '\t' + str(hsp.sbjct_end) + '\n') # Writes the information Reddy Wants
    writer.write('\n') # Writes an extra line break so that eventaully we can write multiple sequences
# We may have to separate by a different character/string so that we can parse individual
# results in the future better


def main():
    
    query = input('Enter query file name: ') # For the working example, type in 'Test_miRNA.txt'
    filename = input('What is your desired file name for the top hits file? ') # I used 'Test_miRNA_Results.txt'
    writer = open(filename, 'w')
    writer.write('Organism_name' + '\t' + 'Query_start' + '\t' + 'Query_end' + '\t' + 'Subject_start' + '\t' +
                 'Subject_end' + '\n') # Writes the header for the results file
    print('Now BLASTing')
    os.system('blastn -task blastn-short -query ' + query + ' -db Input/gg_db -out BLAST_result.xml -outfmt "5" ')
    result_handle = open('BLAST_result.xml')
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        parsefile(blast_record,writer)
    writer.close()
    print('Finished!')

main()
