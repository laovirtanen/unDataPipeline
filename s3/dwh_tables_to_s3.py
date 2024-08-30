from dotenv import load_dotenv
import boto3
import os

load_dotenv('../.env')


# Define the files to upload
csv_files = ['Dim_Country.csv', 'Dim_Series.csv', 'Dim_Time.csv', 'Fact_HealthIndicators.csv']
output_dir = '../data_transformation/data_folder/'


aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY')
aws_region = os.getenv('AWS_REGION')
s3_bucket = os.getenv('BUCKET_NAME')

# Check if environment variables are loaded correctly
if not all([aws_access_key_id, aws_secret_access_key, aws_region, s3_bucket]):
    raise ValueError("Missing environment variables. Please check your .env file.")

s3 = boto3.client(
    's3',
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    region_name = aws_region
)


for filename in csv_files:
    file_path = os.path.join(output_dir, filename)
    try:
        s3.upload_file(file_path, s3_bucket, filename)
        print(f'Uploaded {filename} to s3 bucket {s3_bucket}')
    except Exception as e:
        print(f"Failed to upload {filename} to S3. Error: {e}")


print('All files have been uploaded')
