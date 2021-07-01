# configparser module is used for working with configuration files.
# You can use it to manage user-editable configuration files for an application.

import configparser

# SparkConf is used to specify the configuration of your spark application.
# It is used to set spark application parameters as key-value pairs.

from pyspark import SparkConf

# get_spark_app_config() will load the configurations from spark.conf file and return a SparkConf object.

def get_spark_app_config():
  spark_conf = SparkConf()
  # 2 lines below are used to read spark.conf file.
  config = configparser.ConfigParser()
  config.read("spark.conf")

  #Loop through the configs and set it to the spark_conf object.
  for(key,val) in config.items("SPARK_APP_CONFIGS"):
    spark_conf.set(key,val)
  return spark_conf