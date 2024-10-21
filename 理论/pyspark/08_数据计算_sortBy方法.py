from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = "D:/softwear/python/python3.10.9/python.exe"

# 构建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 读取数据文件
rdd = sc.textFile("F:/hello.txt")

# 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# 将所有单词都转换为二元元组，单词为key，value为1
word_one_rdd = word_rdd.map(lambda word: (word, 1))

# 分组并求和
result_rdd = word_one_rdd.reduceByKey(lambda a, b: a + b)

# 对结果进行排序
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
print(final_rdd.collect())

# 停止SparkContext对象
sc.stop()