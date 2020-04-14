#!/usr/bin/env python3

import cgxinit
from cloudgenix import jd, API
import sys

sdk, args = cgxinit.go()

print(sdk.tenant_id)
response = sdk.get.sites()

site_list = response.cgx_content.get("items")

for site in site_list:
    print("SITE NAME: ", site['name'])
    print("SITE TAGS: ", site['tags'])
    print(" ")
    user_input = ""
    if site['tags']:
        while (user_input != "y" and user_input != "n"):
            user_input = str(input("Would you like to delete all tags at this site (y/n) "))
        if user_input == "y":
            site['tags'] = []
            put_response = sdk.put.sites(site['id'],site,sdk.tenant_id)
            print("Success, deleted all tags at site", site['name'])