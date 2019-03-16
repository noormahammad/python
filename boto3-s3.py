Display a List of Amazon S3 Buckets
List all the buckets owned by the authenticated sender of the request.

The example below shows how to:

List buckets using list_buckets.
Example
import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call S3 to list current buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print out the bucket list
print("Bucket List: %s" % buckets)
Create an Amazon S3 Bucket
The example below shows how to:

Create a new bucket using create_bucket.
Example
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucket')
Upload a File to an Amazon S3 Bucket
The example below shows how to:

Upload a file to a bucket using upload_file.
Example
import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'file.txt'
bucket_name = 'my-bucket'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)
