# from pyspark import SparkConf
# from pyspark.sql import SparkSession
 
# conf = SparkConf()
# conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.1')
# # conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider')
# # conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider')
# conf.set('spark.hadoop.fs.s3a.access.key', "admin")
# conf.set('spark.hadoop.fs.s3a.secret.key', 'behUcVcTIF')
# conf.set('spark.hadoop.fs.s3a.endpoint', 'http://10.140.19.241:9001/')
# conf.set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
# conf.set("fs.s3a.path.style.access", "true")
# conf.set("fs.s3a.connection.ssl.enabled", "false")
# spark = SparkSession.builder.config(conf=conf).getOrCreate()
 
# df = spark.read.csv('s3a://orders/dealerships.csv', inferSchema=True)

# # spark = SparkSession.builder.master("local[*]")\
# #         .config('spark.jars.packages','org.apache.hadoop:hadoop-aws:3.3.1')\
# #         .getOrCreate()
# # spark = SparkSession.builder.getOrCreate()

# # def load_config(spark_cotext:SparkContext):
# #     # spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://10.140.19.241:9001/")
# #     # spark_cotext._jsc.hadoopConfiguration().set('fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
# #     spark_cotext._jsc.hadoopConfiguration().set('fs.s3a.access.key','admin')
# #     spark_cotext._jsc.hadoopConfiguration().set('fs.s3a.secret.key','behUcVcTIF')
# #     spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
# #     spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.attempts.maximum", "5")
# #     spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.connection.establish.timeout", "5000")
# #     spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.connection.timeout", "10000")
# #     spark_cotext._jsc.hadoopConfiguration().set("fs.s3a.connection.ssl.enabled", "false")

# # load_config(spark.sparkContext)
# # dataframe = spark.read.json('s3a://orders/*')