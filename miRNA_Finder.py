#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os

def locationParser(file_handle, working_list, organism_name):
    # This function takes in a file handle to write a uniform file name as well as the list of information to write
    # (file_handle)_locations.txt will hold all of this information
    # The locations are being saved separately in case the user cares about an miRNA not listed in the top 100
    writer = open(file_handle + '_' + organism_name + '_locations.txt', 'w')  # Creates the uniform file extension
    writer.write('Query_miRNA_ID' + ',' + 'Subject_ID' + ',' + 'Organism_name' + ',' + 'Query_start' + ',' +
                 'Query_end' + ',' + 'Subject_start' + ',' +
                 'Subject_end' + ',' + 'Percent_Identity' + ',' + 'Query_Coverage' + ',' + 'E-Value' +
                 '\n')  # Writes the header for the location results file
    for s in working_list:
        writer.write(s + '\n')
    writer.close()


def main():
    db = raw_input("Do you need to make a BLAST database? Please type Yes or No: ")
    if db == "Yes" or db == "yes" or db == "Y" or db == "YES":
        path = raw_input("Please type the full path to the fasta file you wish to use: ")
        dbtype = raw_input("Please input the database type (prot for protein or nucl for nucleotide): ")
        output = raw_input("Please enter the full path to the output destination: ")
        database_name = raw_input("Please enter the name of your database: ")
        os.system("makeblastdb -in " + path + " -dbtype " + dbtype + " -out " + output)
        # creates the database through the command line

    else:
        print("ok! We will BLAST against the chicken database as a default")
        database_name = 'gg_db'
    query = raw_input('Enter query file name: ')  # For the working example, type in 'gg_pre_mirna_short.fasta'
    file_handle = query[0:len(query)-6]  # Stores the original file name that we can add extension file names from
    temp_string = raw_input('What is your ideal cutoff query coverage?: ')
    if temp_string != '':
        query_coverage = float(temp_string)  # The user can input a query coverage.
    else:
        print('Since no value was inputted, BLAST will not filter by query coverage')
        query_coverage = 0
    temp_string = raw_input('What is your ideal cutoff percent identity?: ')
    if temp_string != '':
        percent_identity = float(temp_string)  # The user can input a percent identity cutoff
    else:
        print('Since no value was inputted, BLAST will not filter by percent identity')
        percent_identity = 0
    temp_string = raw_input('What is your ideal cutoff E-value: ')
    if temp_string != '':
        expectedvalue = float(temp_string)  # The user can input a percent identity cutoff
    else:
        print('Since no value was inputted, BLAST will choose a max E-value of 10')
        expectedvalue = 10
    organism_name = raw_input("What organism's genome is represented by the BLAST database? (No spaces please): ")
    if ' ' in organism_name:
        organism_name = organism_name.replace(' ', '_')
    print('Now BLASTing')
    blast_result_file = file_handle + '_' + organism_name + '_full_BLAST_result.txt'
    os.system('blastn -task blastn-short -query ' + query + ' -db ' + database_name + ' -out '+ blast_result_file +
              ' -num_threads 8 -outfmt "6 std qcovs" ')  # BLASTs from command line
    print('BLAST completed, now parsing file')
    count_dictionary ={}  # to hold the query id and the # of occurrences
    working_list = []  # This will hold summary information like location for ALL miRNA's
    top100writer = open(file_handle + '_' + organism_name + '_results.txt', 'w')  # This will write the top
    with open(blast_result_file, 'r') as input:  # Reads the results from the comma-separated BLAST output
        for line in input:
            lineList = line.strip().split()
            query_id = lineList[0]
            subject_id = lineList[1]
            identity = float(lineList[2])
            evalue = float(lineList[10])
            qcoverage = float(lineList[12])
            qstart = lineList[6]
            qend = lineList[7]
            sstart = lineList[8]
            send = lineList[9]
            if identity >= percent_identity and (qcoverage >= query_coverage) and (evalue <= expectedvalue):  # Filters for quality
                working_list.append(query_id + ',' + subject_id + ',' + organism_name + ',' + qstart + ',' + qend +
                                   ',' + sstart + ',' + send + ',' + str(identity) + ',' + str(qcoverage) + ',' + str(evalue))
                if query_id in count_dictionary:
                    count_dictionary[query_id] = count_dictionary[query_id]+1
                else:
                    count_dictionary[query_id]=1
        if len(count_dictionary) == 0:
            print ("Sorry, there were no BLAST results with the given parameters")
            return 1
        var = max(count_dictionary.iterkeys(), key=lambda k: count_dictionary[k])
        line1 = "The miRNA that appears the most is " + var + " which appears " + str(count_dictionary[var]) + " times"
        top100writer.write(str(line1) + '\n')
        sorted_dict = sorted(count_dictionary.iteritems(), key = lambda(k, v): (-v,k))[:100]
        top100writer.write('\n' "TOP 100 miRNAs found" + '\n' + '\n')
        for key, value in sorted_dict:
            output = "miRNA: " + str(key) + '\n' + "# of times found:" + str(value) + '\n' + '\n'
            top100writer.write(output)
    top100writer.close()

    locationParser(file_handle, working_list, organism_name)
    print('Finished!')
    print(file_handle + '_' + organism_name + '_locations.txt will hold the locations for referencing')
    print(file_handle + '_' + organism_name + '_results.txt will present the top 100 most frequent miRNAs in order')
    print(blast_result_file + ' will hold the full BLAST result')
    print('')

main()