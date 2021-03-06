# -*- coding:  utf-8 -*-
#!/usr/bin/python
# author: wangxiaogang02@baidu.com
from urllib import urlopen
import sys

dataFilePath = sys.argv[1]
readFile = open(dataFilePath, "r")

currentNum = 0

for eachLine in readFile:
	currentNum += 1
	lineArray = eachLine.split('\t')
	ubmcid = lineArray[20]
	versionid = lineArray[21]
	shotedPngName = "flash_" + ubmcid + "_" + versionid + ".png";

	urlHead = "http://qapi.baidu.com/api/UBMC/search_related_api/V1/search_material?"
	urlTail = "&app_id=3&user_id=1&cluster_id=0&show_flash=1&raw=0&qapikey=ad72d2f95ac7a39fd96b0e4febe548ed"
	urlAll = urlHead + "mc_id=" + ubmcid + "&version_id=" + versionid + urlTail

	print urlAll

	doc = urlopen(urlAll)
	print doc.info()
	print doc.info().getheader('Content-Type')

	flashUrl = "hh"

	screenshotScript = "python saveScreenshot.py " + flashUrl + " ./flashShot/" + shotedPngName
	print shotedPngName


class RunScript(threading.Thread):
    def __init__(self,target,p):
        threading.Thread.__init__(self)
        self.target = target
        self.p = p

    def getProxy(self):
        print "目标网站：" + self.target
        req = urllib2.urlopen(self.target)
        result = req.read()
        matchs = self.p.findall(result)
        for row in matchs:
            ip = row[0]
            port = row[1]
            # 英文省份名称
            province_en = row[2]
            # 中文所在城市名称
            city_cn = row[3]
            speed = row[4]
            proxy = [ip,port,province_en,city_cn,speed]
            # print(proxy)
            rawProxyList.append(proxy)

    def run(self):
        self.getProxy()