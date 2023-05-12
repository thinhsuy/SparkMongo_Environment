import findspark
from pyspark.sql import SparkSession
findspark.init()

try: 
    spark = SparkSession.builder.master("local").appName("Introduction to Spark").getOrCreate()
except: 
    raise Exception('Spark AppName aready exist!')

df = spark.read.json("CSC14118/movies.json") 
# cast_df = spark.read.json("CSC14118/casters.json") 
