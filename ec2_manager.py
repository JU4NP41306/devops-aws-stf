import boto3

ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-0abcdef1234567890',  # Reemplaza con una AMI válida
    MinCount=1,
    MaxCount=3,
    InstanceType='t2.micro',
    IamInstanceProfile={'Name': 'LabInstanceProfile'}
)
print("Instancias creadas:", response['Instances'])
