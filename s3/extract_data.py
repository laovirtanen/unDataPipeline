import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_from_s3(bucket_name, object_key, local_path, region='eu-north-1'):
    """
    Download a file from an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param object_key: The key (path) of the file in the S3 bucket
    :param local_path: The local file path to save the downloaded file
    :param region: AWS region where the S3 bucket is located
    """
    try:
        AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY']
        AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']

        # Initialize an S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=region
        )

        # Download the file
        s3_client.download_file(bucket_name, object_key, local_path)
        logging.info(f"File downloaded successfully to {local_path}")

    except NoCredentialsError:
        logging.error("Credentials not available. Please check your AWS_ACCESS_KEY and AWS_SECRET_KEY.")
    except PartialCredentialsError:
        logging.error("Incomplete credentials provided. Please check your AWS credentials.")
    except ClientError as e:
        logging.error(f"Client error: {e}")
    except FileNotFoundError:
        logging.error(f"Local path {local_path} not found. Please check the local path.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Set parameters
bucket_name = os.environ['BUCKET_NAME']
object_key = os.environ['OBJECT_KEY']
local_path = os.path.join('imports', 'population_indicators.csv')

# Call the function
download_from_s3(bucket_name, object_key, local_path)
