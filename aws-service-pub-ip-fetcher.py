#!/usr/bin/python3

#version 0.6
#Date: 06/05/2020
#Author: Ivan Gladushko
#
#Description: 
# The script fetches JSON-formated AWS Service public IP ranges in an interactive way 
# providing a menu and navigation instructions
#
# Source: https://ip-ranges.amazonaws.com/ip-ranges.json
#
# The script can be executed from any directory. 
#
# How to
# python3 aws-service-pub-ip-fetcher.py
# then follow the instructions on the screen by selecting the required 
# numbered menu item and commiting by pressing "Enter" key
#
#Prerequisites:
# RHEL
# sudo yum install python3
# sudo dnf install python3-pip
# pip3 install PTable
#
# Ubuntu
# sudo apt-get install python3
# sudo apt-get install python3-pip
# pip3 install PTable


import requests
from prettytable import PrettyTable

# Variables
selector_l0 = '0'
selector_l1 = '0'
selector_l2 = '0'
selected_region = '0'
selected_service = '0'

region_list = []
service_list = []

aws_ip_ranges_url = "https://ip-ranges.amazonaws.com/ip-ranges.json"

# Attempting to get JSON
response = requests.get(aws_ip_ranges_url)

# Checking if JSON is retrieved
if response.status_code == 200:

    # Filling array with JSON's properties
    list = response.json()
    prefix_list = list['prefixes']

    # Removing region duplicates
    for region in prefix_list:
        if region['region'] not in region_list:
            region_list.append(region['region'])

    # Removing service duplicates
    for service in prefix_list:
        if service['service'] not in service_list:
            service_list.append(service['service'])

# Building interactive menu Level0
while selector_l0 == '0':
    print ("1. Display AWS Regions")
    print ("2. Exit")
    selector_l0 = input("Select Menu Item [Exit]: ")

    # Processing Level0 Option selection
    if selector_l0 == '1':
        print ("Option 1 'Display AWS Regions' selected\n")
        region_table= PrettyTable(['#', 'AWS Region'])
        region_table_count = 0
        for i in range(len(region_list)):
            region_table.add_row([str(i+1), region_list[i]])
            region_table_count = i+1
        print(region_table)

        # Building interactive menu Level1
        print ("\nEnter AWS Region # or press '0' to exit\n")
        selector_l1 = input("Select AWS Region [Exit]: ")

        # Processing Level1 exception
        if not selector_l1 :
            print("Exit Selected")
            break

        # Processing Level1 Option selection
        elif selector_l1 == "0":
            print("Exit Selected")
            break

        # Processing Level1 exception
        elif int(selector_l1) > region_table_count:
            print("Unknown Menu Item Selected, terminating\n")
            break

        # Processing Level1 Option selection
        elif int(selector_l1)> 0 and int(selector_l1) <= region_table_count:
            selector_l1_value = int(selector_l1)-1
            print("AWS Region '"+region_list[selector_l1_value]+"' Selected")
            service_table = PrettyTable(['#', 'AWS Service'])
            service_table_count = 0
            for i in range(len(service_list)):
                service_table.add_row([str(i + 1), service_list[i]])
                service_table_count = i + 1
            print(service_table)

            # Building interactive submenu
            print("\nEnter AWS Service # or press '0' to exit\n")
            selector_l2 = input("Select AWS Service [All]: ")

            # Processing Level2 default Option selection
            if not selector_l2:
                print("All AWS Services Selected\n")
                print("Region = " + region_list[selector_l1_value])
                print("Service = All")
                ip_prefix_table = PrettyTable(["Service", "IP Prefix"])

                for item in prefix_list:
                    if item['region'] == region_list[selector_l1_value]:
                        ip_prefix_table.add_row([item['service'], item['ip_prefix']])

                print(ip_prefix_table)
                print ("Completed successfully, exiting")
                break

            # Processing Level2 Option selection
            elif selector_l2 == "0":
                print("Exit Selected")
                break

            # Processing Level2 exception
            elif int(selector_l2) > service_table_count:
                print("Unknown Menu Item Selected, terminating\n")
                break

            # Processing Level2 Option selection
            elif int(selector_l2) > 0 and int(selector_l2) <= service_table_count:
                selector_l2_value = int(selector_l2) - 1
                print("AWS Service '" + service_list[selector_l2_value] + "' Selected\n")
                print("Region = " + region_list[selector_l1_value])
                print("Service = " + service_list[selector_l2_value])
                ip_prefix_table = PrettyTable(["IP Prefix"])

                for item in prefix_list:
                    if item['region'] == region_list[selector_l1_value] and item['service'] == service_list[selector_l2_value]:
                        ip_prefix_table.add_row([item['ip_prefix']])

                print(ip_prefix_table)
                print ("Completed successfully, exiting")
                break

    # Processing Level0 Option selection
    elif selector_l0 == '2':
        print ("Option 2 'Exit' selected")
        break

    # Processing Level0 exception
    else:
        print ("Unknown Menu Item Selected, terminating")
        break
