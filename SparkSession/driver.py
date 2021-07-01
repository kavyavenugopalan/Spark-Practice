from pyspark.sql import *
  #EITHER
if __name__=="__main__":
  spark=SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .getOrCreate()
  
  #OR
  
#if __name__ == "__main__":
  #conf = SparkConf()
  #conf.set("spark.app.name","Hello Spark")
  #conf.set("spark.master","local[3]")
  #spark = SparkSession.builder \
          #.config(conf=conf) \
          #.getOrCreate()
