from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 1, 2, 3, 4, 5, 7, 7, 9])

# 需求：将RDD数据进行去重
rdd2 = rdd.distinct()
print(rdd2.collect()) # [1, 2, 3, 4, 5, 7, 9]

# 停止SparkContext对象
sc.stop()