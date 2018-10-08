#!/bin/sh

# sudo /mnt/config/cluster/connect.sh

# 1. Download the files
# 1.1.3 mapper 0 (v3)
wget https://www.dropbox.com/s/0v7svu3rg7q7de4/mapper_block_0_v3.py

# 1.2.1 reducer 0 (v1)
wget https://www.dropbox.com/s/awk8wchy906cawd/reducer_block_0_v1.py

# 1.3 mapper 1
wget https://www.dropbox.com/s/579dqicxivuo9ev/mapper_block_1_v1.py

# 1.4 reducer 1
wget https://www.dropbox.com/s/hdwztn3xuavhu3v/reducer_block_1_v1.py

# 1.5.2 matrix sans param
wget https://www.dropbox.com/s/nkncjsstzvvbr0s/test_matrix_big_sansparam.txt

# 1.6 execution shell
# see below

# 2. GIVE PERMISSION
chmod +x *.py

# 3. CREATE DIRECTORY
hdfs dfs -mkdir /user/hadoop/wc

# 4. CREATE INPUT SUBDIRECTORY
hdfs dfs -mkdir /user/hadoop/wc/input

# 5. PUT TEXT FILE INTO INPUT
hdfs dfs -put test_matrix_big_sansparam.txt /user/hadoop/wc/input

# 6) RUN
# chmod +x project_exe_v1.sh
# ./project_exe_v1.sh



 
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file /home/hadoop/mapper_block_0_v3.py \
-mapper '/home/hadoop/mapper_block_0_v3.py 8 13 10 3 4' \
-file /home/hadoop/reducer_block_0_v1.py \
-reducer /home/hadoop/reducer_block_0_v1.py \
-input /user/hadoop/wc/input \
-output /user/hadoop/wc/output
 
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-file /home/hadoop/mapper_block_1_v1.py \
-mapper /home/hadoop/mapper_block_1_v1.py \
-file /home/hadoop/reducer_block_1_v1.py \
-reducer /home/hadoop/reducer_block_1_v1.py \
-input /user/hadoop/wc/output \
-output /user/hadoop/wc/output1 \















# #### alternagtively, to execute locally
# cd /Users/ruoyangzhang/Documents/Database_management_II/project

# cat test_matrix_big.txt | python mapper_block_0_v1.py | sort | python reducer_block_0_v1.py | python mapper_block_1_v1.py | sort | python reducer_block_1_v1.py



# navigation: 
# hdfs fs -ls complete directory

# find a file:
# hdfs dfs -find <path> -name mapper_block_1_v1.py
# hdfs dfs -find -name mapper_block_1_v1.py



# /home/hadoop


# cat test_matrix_big_sansparam.txt | ./mapper_block_0_v3.py 8 13 10 3 4 | sort | ./reducer_block_0_v1.py | ./mapper_block_1_v1.py | sort | ./reducer_block_1_v1.py







