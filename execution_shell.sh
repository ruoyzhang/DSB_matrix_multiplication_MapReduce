#!/bin/sh

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/mmx/input \
-output /user/hadoop/mmx/output \
-file /home/hadoop/mapper_block_0_v1.py \
-mapper /home/hadoop/mapper_block_0_v1.py \
-file /home/hadoop/reducer_block_1_v1.py \
-reducer /home/hadoop/reducer_block_1_v1.py 

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/mmx/output \
-output /user/hadoop/mmx/output1 \
-file /home/hadoop/reducer_block_0_v1.py \
-mapper /home/hadoop/reducer_block_0_v1.py \
-file /home/hadoop/reducer_block_1_v1.py \
-reducer /home/hadoop/reducer_block_1_v1.py