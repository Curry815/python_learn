import json

from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# TODO 需求1：城市销售额排名
# 1.1 读取文件得到RDD
rdd = sc.textFile("F:/orders.txt")
# 1.2 取出一个个JSON字符串
json_str_rdd = rdd.flatMap(lambda x: x.split("|"))
# 1.3 将一个个JSON字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
# 1.4 取出城市和销售额数据
city_amount_rdd = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))
# 1.5 按城市分组销售额聚合
city_result_rdd = city_amount_rdd.reduceByKey(lambda a, b: a + b)
# 1.6 按照销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(f"需求1的结果是：{result1_rdd.collect()}")

# TODO: 需求2：全部城市有哪些商品类别在售卖
category_rdd = dict_rdd.map(lambda x: x['category']).distinct()
print(f"需求2的结果是：{category_rdd.collect()}")

# TODO: 需求3：北京市有哪些商品类别在售卖
# 3.1 过滤北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')
# 3.2 取出全部商品类别
result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()
print(f"需求3的结果是：{result3_rdd.collect()}")

# 停止SparkContext对象
sc.stop()