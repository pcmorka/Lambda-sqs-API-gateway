import boto3  #import boto3 module 

sqs = boto3.client('sqs')  #creating an sqs client

 #creating queue
response = sqs.create_queue( QueueName='Week15_Project-sqs-queue') 

print(response)