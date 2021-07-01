from pyspark.sql import *

from lib.logger import Log4J

if __name__=="__main__":
  spark=SparkSession.builder \
    .appName("Hello Spark") \
    .master("local[3]") \
    .getOrCreate()

  logger=Log4J(spark)
  logger.info("starting")
  logger.info("stop")
  spark.stop()
