# start:  pyspark --packages com.databricks:spark-csv_2.10:1.4.0
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
import json

spark = SparkSession\
    .builder\
    .appName("example-spark")\
    .getOrCreate()
sc = SparkContext.getOrCreate()
sqlContext = SQLContext(sc)

csv_path = '/home/yankee/Documents/template/src/main/resources/gps_country_city.csv'
json_path = '/home/yankee/Documents/template/src/main/resources/meteo_data.json'
cities_temp_df = sqlContext.read.format('com.databricks.spark.csv')\
    .options(header='false', inferschema='true')\
    .load(csv_path)

cities_temp_df.show(10, False)
cities_temp_df.count()


# >>> cities_temp_df.show(10, False)
# +---------+------------+----------+----------+
# |_c0      |_c1         |_c2       |_c3       |
# +---------+------------+----------+----------+
# |Country  |City        |Latitude  |Longitude |
# |Argentina|Buenos Aires|-34.608521|-58.373539|
# |Australia|Adelaide    |-34.926102|138.599884|
# |Australia|Brisbane    |-27.46888 |153.022827|
# |Australia|Derrimut    |-37.79953 |144.789078|
# |Australia|Melbourne   |-37.817532|144.967148|
# |Australia|Perth       |-31.95302 |115.857239|
# |Australia|Sydney      |-33.869629|151.206955|
# |Austria  |Graz        |47.068565 |15.44318  |
# |Austria  |Linz        |48.30425  |14.288155 |
# +---------+------------+----------+----------+
# only showing top 10 rows
#
# >>> cities_temp_df.count()
# 410
# >>>

meteo_rdd = sc.wholeTextFiles(json_path).values().map(json.loads)
#or
meteo_df = spark.read.json()
#than split JSON To rows & convert o rdd


meteo_df.show(1, True)
meteo_df.count()

# dataframes could be jones by condition city & country  (broadcasting cities table) grouped by city (using window func)
#than calculate in window who is closest

# >>> meteo_df.show(1, True)
# +--------------------+-------+
# |                data|     id|
# +--------------------+-------+
# |[[2010-01-02, -0....|dataset|
# +--------------------+-------+




