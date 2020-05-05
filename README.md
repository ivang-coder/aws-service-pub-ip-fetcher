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
The script can be executed from any directory
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

| 4  | ... |

+----+----------------+
### AWS Service menu sample
+----+---------------------------------+

| #  |           AWS Service           |

+----+---------------------------------+

| 1  |              AMAZON             |

| 2  |       ROUTE53_HEALTHCHECKS      |

| 3  |                S3               |

| 4  | ... |

+----+---------------------------------+
### IP Prefix menu sample
+-----------------+

|    IP Prefix    |

+-----------------+

|  15.193.3.0/24  |

|  13.236.0.0/14  |

|  15.177.83.0/24 |

|  ...  |

+-----------------+
## License
MIT License
## Author
Ivan Gladushko
