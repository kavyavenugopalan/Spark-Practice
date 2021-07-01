from pyspark.sql import *

if __name__=="__main__":
  spark=SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .getOrCreate()
