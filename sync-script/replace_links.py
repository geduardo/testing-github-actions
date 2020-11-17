#!/bin/env python
# -*- coding: utf-8 -*-
##
# replace_links.py: replaces the relevant links with uid cross references.  
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
##

"""
Replaces GitHub links with uid cross references for the files specified 
in the map.csv file. This script is used to create a usable copy of 
the files to be used in the documentation repository.

"""

import csv
def main():
    with open('map.csv') as f:
        reader = csv.reader(f, skipinitialspace=True)
        map_urls = dict(reader)
    for path in map_urls:
        with open("../Language/"+path, "rt", encoding='utf-8') as f:
            text = f.readlines()
            new_text = []
            for line in text:
                for url in map_urls:
                    uid = map_urls[url]
                    full_url = 'https://github.com/microsoft/qsharp-language/blob/main/Specifications/Language/'+url
                    full_uid = 'xref:'+ uid
                    line = line.replace(full_url, full_uid)
                    line = line.replace('← [Back to Index](https://github.com/microsoft/qsharp-language/tree/main/Specifications/Language#index)','')
                new_text.append(line)
        with open("../Language/"+path, "wt", encoding='utf-8') as f:
            for line in new_text:
                f.write(line)
                
if __name__ == "__main__":
    main()