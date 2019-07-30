#!/usr/bin/env python
import sqlite3
import csv
import re

conn = sqlite3.connect('/u/home/a/akarlsbe/scratch/djoin/data/refSeqFungiStats.db')
c = conn.cursor()
strain_tax_id = 1028729

filePath = '/u/home/a/akarlsbe/scratch/strain_contig_only_assemblies/1028729/1028729_2_contributing_databases_ENSEMBLE_1K.raw.fa'

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
	# c.execute('''UPDATE strain_contig_consensus_db SET min_length_contig =?, max_length_contig =?, avg_length_contig =?, contig_count = ? WHERE STRAINTAXID=?''',(min_length, max_length, avg_length, contig_count, strain_tax_id))
	conn.commit()
conn.close()