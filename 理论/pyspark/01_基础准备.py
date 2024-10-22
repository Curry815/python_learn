from pyspark import SparkConf, SparkContext

# 构建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于SparkConf类对象创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark的版本号
print(sc.version)

# 停止SparkContext对象
sc.stop()