# Python-Public-Ip-R53-Updater
A simple Python script to update a Route53 record.

## Setup Steps
+ Rename vars-template.py to vars.py
+ Update vars.py  With the follow
    + Hosted Zone ID from R53
    + R53Record full FQDN www.example.com
    + aws profile name in your credentials file.
+ pip3 install -r requirements.txt


### To Do

- [ ] Error Handeling
- [ ] Update Discord / Mattermost / Slack option?
- [ ] Make into service?
- [ ] Basic SystemD config