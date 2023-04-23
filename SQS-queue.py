import boto3 #import boto3 module

sqs = boto3.resource('sqs') #creating an sqs client

#create a queue
queue = sqs.create_queue(
  QueueName='Week15_Project-sqs-queue',
  )

#print queue url
print(queue.url)