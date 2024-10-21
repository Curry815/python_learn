from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"
os.environ["HADOOP_HOME"] = "D:/softwear/hadoop-3.0.0"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)])
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]])

# 输出到文件
rdd1.saveAsTextFile("F:/output_one")
rdd2.saveAsTextFile("F:/output_two")
rdd3.saveAsTextFile("F:/output_three")
