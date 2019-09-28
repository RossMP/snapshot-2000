# snapshot-2000
Demo project to manage AWS EC2 instance snapshots

## about
This project is a demo and uses boto3 to manage AWS EC2 instance snapshots

## configuring
shotty uses the configuration file created by the AWS cli

'aws configure --profile shotty'

## running
'pipenv run python shotty/shotty.py <command>
<--project=PROJECT>'

*command* is list, start or stopping
*project* is optional
