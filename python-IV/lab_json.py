#!/usr/bin/env python3
# *-* coding:utf-8 *-*

"""

:mod:`lab_json` -- JSON Navigation
=========================================

LAB_JSON Learning Objective: Learn to navigate a JSON file and convert to a
                             python object. Practice file IO using with.
::

 a. Using urllib2, explore the GitHub JSON API.  Load the initial api page, parse it
    into JSON, and use it for the following tasks.

 b. Load the list of emojis from the GitHub API and print a random one from the list.
    Save the list to emojis.json

 c. Load the information for a GitHub username passed in from the command line, print
    the number of repositories the user has and what organizations they belong to.
    Save the user info to {{username}}.json

"""

# see https://docs.python.org/2/library/urllib2.html for more info on urllib2
# example use of urllib2 to get a web resource:
import urllib.request
import urllib.error
import urllib.parse
import json
import random
import sys

# Part A
token = ''

data = urllib.request.urlopen("https://api.github.com/?access_token={}".format(token))
json_obj = json.loads(data.read().decode(data.headers.get_content_charset()))

# Part B
for i in json_obj:
    if 'emoji' in i:
        emoji_data = urllib.request.urlopen(json_obj[i] + '?access_token=0ec43968dfeeb0a39d3af46ba3da8cacd4171242')
        emoji_json_obj = json.loads(emoji_data.read().decode(
                                    emoji_data.headers.get_content_charset()))
        print('Random emoji: ' + random.choice(list(emoji_json_obj.keys())))

    # Part C
    if 'user_url' in i:
        url_user = json_obj[i].replace('{user}', sys.argv[1])
        user_data = urllib.request.urlopen(url_user + '?access_token=0ec43968dfeeb0a39d3af46ba3da8cacd4171242')
        user_json_obj = json.loads(user_data.read().decode(
                                    user_data.headers.get_content_charset()))
        
        org_data = urllib.request.urlopen(user_json_obj['organizations_url'] + '?access_token=0ec43968dfeeb0a39d3af46ba3da8cacd4171242')
        org_json_obj = json.loads(org_data.read().decode(
                                    org_data.headers.get_content_charset()))

        output_dict = {'repos': user_json_obj['public_repos'], 'orgs': org_json_obj}
        output_file = open("{}.json".format(sys.argv[1]), 'w')
        json.dump(output_dict, output_file)
        output_file.write("\n")
