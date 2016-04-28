#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv;

import gdata.docs.service
import gdata.spreadsheet.service

from xml.etree.ElementTree import ElementTree, Element, SubElement, dump

def get_local_information_android():
    gdoc_id = sys.argv[1]
    headerIdx = sys.argv[2]
    contentIdx = sys.argv[3]
    downloadpath = sys.argv[4]

    try:
        file_path = download(gdoc_id)
        readCSV(downloadpath, file_path, headerIdx, contentIdx)
    except Exception, e:
        print "----- error -----"
        print(e)
        #raise e

def download(gdoc_id, download_path=None, ):
    print "Downloading the CVS file with id %s" % gdoc_id

    gd_client = gdata.docs.service.DocsService()

    # auth using ClientLogin
    gs_client = gdata.spreadsheet.service.SpreadsheetsService()
    # gs_client.ClientLogin(email, password)

    # getting the key(resource id and tab id from the ID)
    resource = gdoc_id.split('#')[0]
    tab = gdoc_id.split('#')[1].split('=')[1]
    resource_id = 'spreadsheet:' + resource

    if download_path is None:
        download_path = os.path.abspath(os.path.dirname(__file__))

    file_name = os.path.join(download_path, '%s.csv' % (gdoc_id))

    print 'download_path : %s' % download_path;
    print 'Downloading spreadsheet to %s' % file_name

    docs_token = gd_client.GetClientLoginToken()
    gd_client.SetClientLoginToken(gs_client.GetClientLoginToken())
    gd_client.Export(resource_id, file_name, gid=tab)
    gd_client.SetClientLoginToken(docs_token)

    print "Download Completed!"

    return file_name

def indent(elem, level=0):
    i = "\n" + level*"    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def readCSV(savepath, file_name, headerIdx, contentIdx):
    print "read csv file : %s" % file_name
    # open
    SourceCSV= open(file_name,"r")
    csvReader = csv.reader(SourceCSV)
    rows = list(csvReader)

    # get header from specific row
    header = rows[int(headerIdx)]

    # find each column index
    androidkey_idx = header.index("Android Key")
    eng_idx = header.index("한국어")
    idn_idx = header.index("영어")

    # Make an empty Element
    resources_kor = Element("resources")
    resources_eng = Element("resources")

    # Loop through the lines in the file and get each coordinate
    for row in rows[int(contentIdx):]:
        androidkey = row[androidkey_idx].lower()
        eng = row[eng_idx]

        idn = row[idn_idx]
        if not row[idn_idx]:
            idn = row[eng_idx]

        #append eng resource
        if row[eng_idx]:
            string_eng = Element("string")
            string_eng.attrib["name"] = androidkey.decode('utf-8')
            string_eng.text = eng.decode('utf-8')
            resources_kor.append(string_eng)

            #append idn resource
            string_idn = Element("string")
            string_idn.attrib["name"] = androidkey.decode('utf-8')
            string_idn.text =  idn.decode('utf-8')
            resources_eng.append(string_idn)

    indent(resources_kor)
    indent(resources_eng)

    # Print the coordinate list    
    #dump(resources_eng)
    #dump(resources_idn)

    #Make Resource Folder
    newpath_ko = savepath+r'\values'
    if not os.path.exists(newpath_ko):
        os.makedirs(newpath_ko)

    newpath_en = savepath+r'\values-en'
    if not os.path.exists(newpath_en):
        os.makedirs(newpath_en)

    #make Xml file
    ElementTree(resources_kor).write(newpath_ko+"\\strings.xml", "utf-8")
    ElementTree(resources_eng).write(newpath_en+"\\strings.xml", "utf-8")

    SourceCSV.close()
    os.remove(file_name)

if __name__=='__main__':
    if len(sys.argv) == 5:
        get_local_information_android()
    else:
        print '----- usage -----'
        print '=> python languagepack.py srcPath headerIndex contentIndex destPath'
        print '=> ex) python languagepack.py doc/example.csv 2 4 src/main/res\n'
