from pyspark.sql import SparkSession

def read_file(spark, s3_input_path, s3_output_path):
    '''
    Read the file and just move the file to output folder

    '''
    df = spark.read.load(s3_input_path, format="csv", inferSchema = "true", header="true")
    print(df.show(20))
    #df.write.mode('overwrite').save(s3_output_path)
    df.write.format("csv").save(s3_output_path)

if __name__ == "__main__":
    spark = SparkSession.builder.appName("sample-read-EMR").getOrCreate()
    s3_input_path='s3://spark-emr-demo-terraform/inputfile/'
    s3_output_path ='s3://spark-emr-demo-terraform/outputfile/'
    read_file(spark, s3_input_path, s3_output_path)