#Just an external vars file
import boto3

#Name of Hosted Zone ID
HostedZoneId = ""
#Example www.example.com
R53Record = ""
#Enter profile from ~/.aws/credentials
boto3.setup_default_session(profile_name='')