from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# # 通过parallelize方法创建RDD对象
# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize((1, 2, 3, 4, 5))
# rdd3 = sc.parallelize("abcdefg")
# rdd4 = sc.parallelize({1, 2, 3, 4, 5})
# rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
#
# print(rdd1.collect())
# print(rdd2.collect())
# print(rdd3.collect())
# print(rdd4.collect())
# print(rdd5.collect())

# 用过textFile方法，读取问价数据加载到Spark内，成为RDD对象
# rdd = sc.textFile("F:/hello.txt")
# print(rdd.collect())

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
print(rdd.collect())

# 停止SparkContext对象
sc.stop()