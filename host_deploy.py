import os
import boto3
from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)

ec2_client = session.client("ec2")


def create_machine( name_of_instance):
   response = ec2_client.run_instances(
      ImageId="ami-01a00762f46d584a1",
      InstanceType="t3.micro",
      KeyName="Bobby",           
    SecurityGroupIds=[
        "sg-067599e290b829b89"         
    ],
      MinCount=1,
      MaxCount=1,
      TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": name_of_instance
                }
            ]
        }
    ]
)

   print(response)


def stop_machine():
   response = ec2_client.stop_instances(InstanceIds=['i-0e5ccc649401324ae'])
   print(response)


create_machine("my_profile")