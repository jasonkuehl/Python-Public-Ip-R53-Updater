## Author: Jason W Kuehl
## Email: jason@jasonkuehl.com

import urllib.request
import boto3

#import all vars from file
from vars import *

#get static ip
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#umcomment to debug if needed
#print(external_ip)

#update route53 record, note this will also create a record if needed.
client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': R53Record,
                    'ResourceRecords': [
                        {
                            'Value': external_ip,
                        },
                    ],
                    'TTL': 900,
                    'Type': 'A',
                },
            },
        ],
    },
    HostedZoneId= HostedZoneId,
)

#umcomment to debug if needed
#print(response)

print("Yep, its updated to " + (external_ip) + " on url " + (R53Record))