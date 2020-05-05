# AWS Service Public IP Fetcher
## Summary 
This Python script fetches JSON-formated AWS Service public IP ranges in an interactive way providing a menu and navigation instructions
**Source:** https://ip-ranges.amazonaws.com/ip-ranges.json
## Prerequisites
### RHEL and the likes
`sudo yum install python3`
`sudo dnf install python3-pip`
`pip3 install PTable`
### Ubuntu
`sudo apt-get install python3`
`sudo apt-get install python3-pip`
`pip3 install PTable`
## Recommendations
The script can be executed from any directory.security appliances and their External Dynamic Lists
## How to
`python3 aws-service-pub-ip-fetcher.py`
then follow the instructions on the screen by selecting the required numbered menu item and commiting by pressing "Enter" key
### Initial menu sample
"1. Display AWS Regions"
"2. Exit"
### AWS Regions menu sample
+----+----------------+
| #  |   AWS Region   |
+----+----------------+
| 1  |   eu-west-3    |
| 2  |   us-west-2    |
| 3  | ap-southeast-2 |
| 4  |     GLOBAL     |
| 5  |   eu-west-1    |
| 6  | ap-southeast-1 |
| 7  |   eu-west-2    |
| 8  | ap-northeast-2 |
| 9  |   ap-east-1    |
| 10 |   ap-south-1   |
| 11 |  eu-central-1  |
| 12 |   us-west-1    |
| 13 |   us-east-1    |
| 14 | ap-northeast-1 |
| 15 |   sa-east-1    |
| 16 |   eu-south-1   |
| 17 |   af-south-1   |
| 18 | us-gov-west-1  |
| 19 | cn-northwest-1 |
| 20 |   eu-north-1   |
| 21 |   me-south-1   |
| 22 |   us-east-2    |
| 23 |  ca-central-1  |
| 24 | ap-northeast-3 |
| 25 |   cn-north-1   |
| 26 | us-gov-east-1  |
+----+----------------+
### AWS Service menu sample
+----+---------------------------------+
| #  |           AWS Service           |
+----+---------------------------------+
| 1  |              AMAZON             |
| 2  |       ROUTE53_HEALTHCHECKS      |
| 3  |                S3               |
| 4  |             DYNAMODB            |
| 5  |               EC2               |
| 6  |             ROUTE53             |
| 7  |            CLOUDFRONT           |
| 8  |            CODEBUILD            |
| 9  |        GLOBALACCELERATOR        |
| 10 |          AMAZON_CONNECT         |
| 11 | ROUTE53_HEALTHCHECKS_PUBLISHING |
| 12 |           API_GATEWAY           |
| 13 |              CLOUD9             |
| 14 |       EC2_INSTANCE_CONNECT      |
| 15 |       WORKSPACES_GATEWAYS       |
+----+---------------------------------+
### IP Prefix menu sample
+-----------------+
|    IP Prefix    |
+-----------------+
|  15.193.3.0/24  |
|  13.236.0.0/14  |
|  15.177.83.0/24 |
|  54.206.0.0/16  |
| 54.153.128.0/17 |
| 52.95.255.16/28 |
|  54.252.0.0/16  |
|   3.104.0.0/14  |
| 64.252.108.0/24 |
|   3.24.0.0/14   |
| 64.252.107.0/24 |
|   52.64.0.0/17  |
|   13.54.0.0/15  |
|  52.95.241.0/24 |
|  99.77.144.0/24 |
| 64.252.106.0/24 |
|  52.64.128.0/17 |
|   54.66.0.0/16  |
|  13.210.0.0/15  |
|   52.62.0.0/15  |
|  54.253.0.0/16  |
| 52.94.248.64/28 |
|   52.65.0.0/16  |
| 64.252.109.0/24 |
|   54.79.0.0/16  |
+-----------------+
## License
MIT License
## Author
Ivan Gladushko
