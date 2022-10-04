from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql import SparkSession

conf = (

    SparkConf()
    .set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.1')

    .setAppName('Spark minIO Test')

    .set('spark.hadoop.fs.s3a.endpoint', 'http://10.140.19.241:9000')

    .set('spark.hadoop.fs.s3a.access.key', 'admin')

    .set('spark.hadoop.fs.s3a.secret.key', 'behUcVcTIF')

    .set('spark.hadoop.fs.s3a.path.style.access', 'True')

    .set('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')

    .set('spark.hadoop.fs.s3a.connection.ssl.enabled','false')

    .set('spark.hadoop.com.amazonaws.services.s3.enableV2', 'true')

    .set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')

)

sc = SparkContext(conf=conf).getOrCreate()
spark = SparkSession.builder.config(conf=conf).getOrCreate()
# spark.sparkContext.getConf().getAll()
dataframe = spark.read.csv('s3a://orders/heights.csv', inferSchema=True)
dataframe.show()
