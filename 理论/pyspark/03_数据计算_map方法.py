from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 通过map方法将全部数据都乘以10
# def func(data):
#     return data * 10
# rdd2 = rdd.map(func)

rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd2.collect())

# 停止SparkContext对象
sc.stop()