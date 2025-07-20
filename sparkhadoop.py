from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("PySparkHadoopExample") \
    .getOrCreate()
# Read data from HDFS
data = spark.read.text("hdfs://localhost:9000/user/hadoop/input_data")
# Perform word count
word_counts = data.rdd.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)
# Save results to HDFS
word_counts.saveAsTextFile("hdfs://localhost:9000/user/hadoop/output_data")
spark.stop()
