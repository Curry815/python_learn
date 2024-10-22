from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子，输出RDD为list对象
rdd_list = rdd.collect()
print(rdd_list) # [1, 2, 3, 4, 5]

# reduce算子，将RDD进行两两聚合
rdd_sum = rdd.reduce(lambda x, y: x + y)
print(rdd_sum) # 15

# take算子，取出RDD前N个元素，组成list返回
rdd_take = rdd.take(3)
print(rdd_take) # [1, 2, 3]

# count，统计RDD内有多少条数据，返回值为数字
rdd_count = rdd.count()
print(rdd_count) # 5
# 停止SparkContext对象
sc.stop()