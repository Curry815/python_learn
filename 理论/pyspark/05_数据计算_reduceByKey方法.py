from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('女', 88), ('男', 77), ('女', 66)])

# 需求：将RDD数据里面的一个个单词提取出来
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())

# 停止SparkContext对象
sc.stop()