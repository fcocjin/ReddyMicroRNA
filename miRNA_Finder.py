#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import csv
import operator
from collections import Counter
import os

def ToCSV(csv_file,csv_columns,dict_data):
    try:
        with open('Output_myedit.csv', 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)   # the output as a CSV Format
            writer.writeheader()
            # write the the query id and the # of occurrences
            # write the number of the occurance in descending order
            for key, value in sorted(dict_data.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                writer.writerow({'query_id': key, 'count': value})
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
    return

def summaryParser(file_handle, working_list, sorded_dict):





def locationParser(file_handle, working_list):
    writer = open(file_handle + '_locations.txt', 'w')
    writer.write('Query_miRNA_ID' + ',' + 'Subject_ID' + ',' + 'Organism_name' + ',' + 'Query_start' + ',' +
                 'Query_end' + ',' + 'Subject_start' + ',' +
                 'Subject_end' + '\n')  # Writes the header for the results file
    for s in working_list:
        writer.write(s + '\n')
    writer.close()


def main():
    query = input('Enter query file name: ')  # For the working example, type in 'gg_pre_mirna_short.fasta'
    file_handle = query[0:len(query)-6]  # Stores the original file name that we can add extension file names from
    query_coverage = input('What is your ideal cutoff query coverage?: ')  # I will use this later to filter results
    percent_identity = input('What is your ideal cutoff percent identity?: ')  # same as above
    organism_name = input("What organism's genome is represented by the BLAST database?: ")
    print('Now BLASTing')
    os.system('blastn -task blastn-short -query ' + query + ' -db Input/tg_db -out BLAST_result.txt -num_threads 8 '
                                                            '-outfmt "6" ')
    print('BLAST completed, now parsing file')
    count_dictionary ={}  # to hold the query id and the # of occurrences
    working_list = []
    top100writer = open(file_handle + '_results.')
    with open('BLAST_result.txt', 'r') as input:
        for line in input:
            lineList = line.strip().split()
            query_id = lineList[0]
            subject_id = lineList[1]
            identity = float(lineList[2])
            # qcoverage = float(?????)
            qstart = lineList[6]
            qend = lineList[7]
            sstart = lineList[8]
            send = lineList[9]
            if identity >= percent_identity:  # and (qcoverage >= query_coverage):
                working_list.append(query_id + ',' + subject_id + ',' + organism_name + ',' + qstart + ',' + qend +
                                   ',' + sstart + ',' + send)
                if query_id in count_dictionary:
                    count_dictionary[query_id] = count_dictionary[query_id]+1
                else:
                    count_dictionary[query_id]=1
                    top100writer = open('top_100_hits.txt', 'w')
        var = max(count_dictionary.iterkeys(), key=lambda k: count_dictionary[k])
        line1 = "The miRNA that appears the most is " + var + " which appears " + str(dictionary[var]) + " times"
        top100writer.write(str(line1) + '\n')
        sorted_dict = sorted(count_dictionary.iteritems(), key = lambda(k, v): (-v,k))[:100]
        top100writer.write('\n' "TOP 100 miRNAs found" + '\n' + '\n')
        for key, value in sorted_dict:
            output = "miRNA: " + str(key) + '\n' + "# of times found:" + str(value) + '\n' + '\n'
            top100writer.write(output)
    top100writer.close()

    summaryParser(file_handle, working_list, sorted_dict)
    locationParser(file_handle, working_list)
    print('Finished!')
    print('')
