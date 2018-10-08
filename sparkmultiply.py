import pyspark
import numpy as np


def reducer1(matched_block):
    results = []
    matA = matched_block[1][0]
    matB = matched_block[1][1]
    min_i = min([element[1] for element in matA])
    max_i = max([element[1] for element in matA])
    min_j = min([element[2] for element in matA])
    max_j = max([element[2] for element in matA])
    min_p = min([element[2] for element in matB])
    max_p = max([element[2] for element in matB])
    
    blockA = dict()
    for element in matA:
        if element[1] not in blockA:
            blockA[element[1]] = dict()
        blockA[element[1]][element[2]] = element[3]

    blockB = dict()
    for element in matB:
        if element[1] not in blockB:
            blockB[element[1]] = dict()
        blockB[element[1]][element[2]] = element[3]
        
    for i1 in range(max_i - min_i + 1):
        for k1 in range(max_p - min_p + 1):
            i = min_i + i1
            k = min_p + k1
            current_res = 0
            for j in range(max_j - min_j + 1):
                try:
                    current_res += blockA[i][min_j+j] * blockB[min_j+j][k]
                except KeyError:
                    pass
            results.append(((i, k), current_res))
            current_res = 0
    return(results)


def multiply(txtfile, mm, nn, pp, hh, ww):
	m = mm
	n = nn
	p = pp
	height = hh
	width = ww

	inputMatrix = txtfile.map(lambda x: x.split(",")).map(lambda x: (str(x[0]),int(x[1]),int(x[2]),float(x[3])))

	matrixA = inputMatrix.filter(lambda x: x[0]=="A")
	matrixB = inputMatrix.filter(lambda x: x[0]=="B")

	outputM1_A = matrixA.map(lambda x: ((int(x[1]/height),int(x[2]/ width)),x))
	outputM1_B = matrixB.map(lambda x: ((int(x[1]/width),int(x[2]/ height)),x))

	outputM2_A = outputM1_A.groupByKey().map(lambda x: (x[0][1],list(x[1])))
	outputM2_B = outputM1_B.groupByKey().map(lambda x: (x[0][0],list(x[1])))

	outputR1 = outputM2_A.join(outputM2_B)
	outputR2 = outputR1.flatMap(reducer1)

	outputR2.groupByKey().map(lambda x : (x[0], list(x[1]))).collect()

	final = outputR2.reduceByKey(lambda x,y: x+y).collect()
	return(final)





if __name__ == '__main__' :
    sc = pyspark.SparkContext()
    matrices = sc.textFile("hdfs:///home/user/hadoop/wc/input")
    mmx = multiply(matrices, 250, 125, 250, 20, 20)
    print(mmx.collect())
