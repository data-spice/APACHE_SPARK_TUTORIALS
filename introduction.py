from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("MySparkApp").getOrCreate()

#Create a DataFrame
census_df=spark.read.csv("census_df",["gender","age","zipcode","salary_range_usd","marriage_status"])


#Show the dataframe
census_df.show()
