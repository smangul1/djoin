#!/usr/bin/env python
import sqlite3
import csv
import re


conn = sqlite3.connect('/u/home/a/akarlsbe/scratch/djoin/data/refSeqFungiStats.db')
c = conn.cursor()

def ParseFiles(csvFile):

	with open(csvFile) as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')

	    for row in readCSV:
	        strain_tax_id = row[0]
	        filePath = row[1]
	        
	        # open each consensus file and determine seq attributes: number of contigs, min length, max length and avg length.
	        print(filePath)

		with open(filePath.strip()) as f:
			contig_lengths = []
			num_contigs = 0
			min_length = 0
			max_length = 0
			avg_length = 0
			sum_contig_lengths = 0
			for line in f:
				if re.findall(r">", line):
					num_contigs +=1
					contig_lengths.append(re.findall(r"\d+", line)[1])
			print(num_contigs, contig_lengths)
			if len(contig_lengths) >= 1:
				contig_lengths.sort()
				min_length = contig_lengths[0]
				max_length = contig_lengths[-1]
				for lengths in contig_lengths:
					sum_contig_lengths += int(lengths)
				avg_length = sum_contig_lengths / num_contigs
			print(avg_length, min_length, max_length)
			c.execute('''INSERT INTO strain_contig_consensus_db(min_length_contig, max_length_contig, avg_length_contig, contig_count, STRAINTAXID, FILEPATH) VALUES(?,?,?,?,?,?)''', (min_length, max_length, avg_length, num_contigs, strain_tax_id, filePath))
			conn.commit()
	conn.close()
	return


csvFile_filepath_and_TaxID = 'strain_contig.csv'
ParseFiles(csvFile_filepath_and_TaxID)


# c.execute("INSERT INTO strain_contig_consensus_db VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (seqAttributes["TAXID"], seqAttributes["GENUSNAME"], seqAttributes["SPECIESNAME"], seqAttributes["STRAIN"], seqAttributes["DBNAME"], seqAttributes["FILEPATH"], seqAttributes["chromosome_count"], seqAttributes["avg_length_chromosomes"], seqAttributes["max_length_chromosomes"], seqAttributes["min_length_chromosomes"], seqAttributes["contig_count"], seqAttributes["avg_length_contig"], seqAttributes["max_length_contig"], seqAttributes["min_length_contig"], seqAttributes["mtDNA_count"], seqAttributes["avg_length_mtDNA"], seqAttributes["max_length_mtDNA"], seqAttributes["min_length_mtDNA"], seqAttributes["plasmid_count"], seqAttributes["avg_length_plasmids"], seqAttributes["max_length_plasmids"], seqAttributes["min_length_plasmids"]))