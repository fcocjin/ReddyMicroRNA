#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

#from subprocess import call
import os

os.system('blastn -task blastn-short -query input/gg_mat_mirna.fasta -db input/gg_db -out gg_mat_result.txt -outfmt "6"')
#os.system('blastn -query input/gg_pre_mirna.fasta -db input/gg_db -out gg_pre_result.txt -outfmt "6"')
#os.system('blastn -query input/tg_mat_mirna.fasta -db input/tg_db -out tg_mat_result.txt -outfmt "6"')
#os.system('blastn -query input/tg_pre_mirna.fasta -db input/tg_db -out tg_pre_result.txt -outfmt "6"')



#os.system('blastn -query input/gg_mat_mirna.fasta -db input/tg_db -out gg_mat_cross_result.txt -outfmt "6"')
#os.system('blastn -query input/gg_pre_mirna.fasta -db input/tg_db -out gg_pre_cross_result.txt -outfmt "6"')
#os.system('blastn -query input/tg_mat_mirna.fasta -db input/gg_db -out tg_mat_cross_result.txt -outfmt "6"')
#os.system('blastn -query input/tg_pre_mirna.fasta -db input/gg_db -out tg_pre_cross_result.txt -outfmt "6"')
