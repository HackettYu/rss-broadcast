#-*- coding:utf-8 -*-
from lxml import etree
from io import StringIO, BytesIO
import urllib.request as request
import lxml.html

# https://rsshub.app/jianshu/home

# BytesIO
# xml = '<a xmlns="test"><b xmlns="test"/></a>'
# root = etree.fromstring(xml)

# StringIo
# tree = etree.parse(StringIO(xml))
# etree.tostring(tree.getroot())

# file
# tree = etree.parse(r"dysfz.xml")

# ftp http gz
# root = etree.fromstring(xml, base_url="https://rsshub.app/wikipedia/mainland")

# parser = etree.XMLParser(ns_clean=True)
# tree = etree.parse

# bash gbk | powershell gb2312 or utf-8

# print all node
# result = etree.tostring(tree.getroot(), encoding="gbk")
# print(result.decode("gbk"))


# utf8_parser = etree.XMLParser(encoding='utf8')
# etree.parse(r"dysfz.xml", parser=utf8_parser)

def parseXMLByFile(xmlFile):
    """
    Parse the xml
    """
    # f = open(xmlFile, "rb")     # "rb" open file
    # xml = f.read()
    # f.close()

    tree = etree.parse(xmlFile)
    context = etree.iterparse(xmlFile, encoding="utf-8")  # 可以直接用文件名作为参数
    # context = etree.iterparse(StringIO(xml), encoding="utf-8") #中文需要设定字符集
    """
    retrun (action, elem)
    """
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print(elem.tag + " => " + text)


def parseXMLByUrl(url):
    """
    parse xml in http
    """
    req = request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        })
    page = request.urlopen(req).read()
    # tree = etree.parse(BytesIO(page))
    context = etree.iterparse(BytesIO(page), encoding="utf-8")  # 中文需要设定字符集
    """
    retrun (action, elem)
    """
    for action, elem in context:
        if not elem.text:
            text = "None"
        else:
            text = elem.text
        print(elem.tag + " => " + text)

    """
    parse html in http
    """
    # doc = lxml.html.document_fromstring(page)
    # for idx, el in enumerate(doc.cssselect('img.BDE_Image')):
    #     with open('%03d.jpg' % idx, 'wb') as f:
    #         f.write(request.urlopen(el.attrib['src']).read())


parseXMLByUrl("https://rsshub.app/dysfz")
# parseXMLByFile(rb"dysfz.xml")
