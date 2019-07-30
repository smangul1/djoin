#!/usr/bin/env python
import sqlite3


conn = sqlite3.connect('/u/home/a/akarlsbe/scratch/djoin/datarefSeqFungiStats.db')
c = conn.cursor()


c.execute("CREATE TABLE IF NOT EXISTS strain_contig_consensus_db(GENUSTAXID INT, GENUSNAME TEXT, SPECIESTAXID INT, SPECIESNAME TEXT, STRAINTAXID INT, STRAINNAME TEXT, DBNAME TEXT, FILEPATH TEXT, chromosome_count INT, avg_length_chromosomes INT, max_length_chromosomes INT, min_length_chromosomes INT, contig_count INT, avg_length_contig INT, max_length_contig INT, min_length_contig INT, mtDNA_count INT, avg_length_mtDNA INT, max_length_mtDNA INT, min_length_mtDNA INT, plasmid_count INT, avg_length_plasmids INT, max_length_plasmids INT, min_length_plasmids INT)")
conn.commit()








# 
# 
# 
# 
# 
# 
# RUN THIS CODE IN terminal:
# INSERT INTO SPECIESDB(GENUSNAME, SPECIESTAXID, SPECIESNAME, STRAINNAME, DBNAME, FILEPATH, chromosome_count, avg_length_chromosomes, max_length_chromosomes, min_length_chromosomes, contig_count, avg_length_contig, max_length_contig, min_length_contig, mtDNA_count, avg_length_mtDNA, max_length_mtDNA, min_length_mtDNA, plasmid_count, avg_length_plasmids, max_length_plasmids, min_length_plasmids) 
# SELECT GENUSNAME, TAXID, SPECIESNAME, STRAIN, DBNAME, FILEPATH, chromosome_count, avg_length_chromosomes, max_length_chromosomes, min_length_chromosomes, contig_count, avg_length_contig, max_length_contig, min_length_contig, mtDNA_count, avg_length_mtDNA, max_length_mtDNA, min_length_mtDNA, plasmid_count, avg_length_plasmids, max_length_plasmids, min_length_plasmids 
# FROM TMP;
# DROP TABLE TMP;