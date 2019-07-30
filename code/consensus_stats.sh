#!/usr/bin/python
. /u/local/Modules/default/init/modules.sh
module load python/2.6

python /u/home/a/akarlsbe/scratch/djoin/code/populate_strain_consensus_database_straintaxis_and_filepath.py


# qsub -m beas -cwd -V -N fungiStats -l h_data=12G,highp,time=24:00:00 consensus_stats.sh
