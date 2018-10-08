import pyspark
import numpy as np
 
def Sparse(l,s):
    # from a given list l assign values to tuples with
    # sparsity s
     
    list_len = len(l)
    # number of non-zero elements
    n_sparse = np.round(s*list_len)
     
    if list_len != 0:
        l_tuples = np.random.choice(list_len,size=int(n_sparse),replace=False)
        result = []
        for i in range(list_len):
            if i in l_tuples:
                val = np.random.rand()
                result.append((l[i][0],l[i][1],val))
        return(result)
         
    else:
        return([])
 
 
def generate(size_n,size_m,spars,num_part):
    # generate square matrices of given size and sparsity
     
    matrix = sc.parallelize(range(size_n))
    matrix = matrix.flatMap(lambda x: [(x,i) for i in range(size_m)])
     
    # num_part should be big enough for the size of your matrix
    # to get small lists in glom
    matrix = matrix.repartition(num_part).glom()
     
    matrix = matrix.flatMap(lambda x: Sparse(list(x),spars))
     
    return(matrix)
 
 
if __name__ == '__main__' :
    sc = pyspark.SparkContext()
 
    matrixA = generate(250,125,0.25,5).map(lambda x: "A,%s,%s,%s" % (x[0],x[1],x[2]))
    matrixB = generate(125,250,0.25,5).map(lambda x: "B,%s,%s,%s" % (x[0],x[1],x[2]))
 
    matrix = matrixA.union(matrixB)
    matrix.saveAsTextFile("hdfs:///home/user/hadoop/wc/input")