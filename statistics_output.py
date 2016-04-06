#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

dictionary ={} # to hold the query id and the # of occurrences

import csv
import operator

def ToCSV(csv_file,csv_columns,dict_data):
    try:
        with open('Output.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)   # the output as a CSV Format
            writer.writeheader()
            # write the the query id and the # of occurrences
            # write the number of the occurance in descending order
            for key, value in sorted(dict_data.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                writer.writerow({'query_id': key, 'count': value})
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
    return



csv_columns = ['query_id','count']  # the file headers
csv_file='Output.csv'               # the output file

with open('gg_mat_cross_result.txt', 'r') as input:  # the input file
    for line in input:                                 # get the query id and test if the identity equals 100%
        linelist = line.strip().split()                 # if so, add the query id to the dictionary
        (query_id, subject_id, identity) = linelist[0:3]
        if identity =="100.00":
            if query_id in dictionary:
                dictionary[query_id]=dictionary[query_id]+1
            else:
                dictionary[query_id]=1



ToCSV(csv_file,csv_columns,dictionary)  # a call to function with three parametes ( the output file, the headers, and the dictionart)