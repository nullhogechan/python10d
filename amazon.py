#! /usr/bin/env python
# coding: utf-8

import urllib
from xml.etree.ElementTree import ElementTree

def main(url):
    xmlfile = urllib.urlopen(url)
    tree = ElementTree(file=xmlfile)
    root = tree.getroot()
    for node in root.getchildren():
        if node.tag == "{http://webservices.amazon.com/AWSECommerceService/2005-10-05}Items":
            for subnode in node.getchildren():
                if subnode.tag == "{http://webservices.amazon.com/AWSECommerceService/2005-10-05}TotalResults":
                    print subnode.text
                elif subnode.tag == "{http://webservices.amazon.com/AWSECommerceService/2005-10-05}Item":
                    for item in subnode:
                        if item.tag == "{http://webservices.amazon.com/AWSECommerceService/2005-10-05}ASIN":
                            print item.text

if __name__ == "__main__":
    amazon_api_url = "http://ecs.amazonaws.jp/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&"
    AWSAccessKeyId = "717601448625"
    Keywords = "Python"
    url = amazon_api_url + "AWSAccessKeyId=" + AWSAccessKeyId + "&SearchIndex=Books&Keywords=" + Keywords
    main(url)
