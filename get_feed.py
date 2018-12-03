#-*- coding:utf-8 -*-
from lxml import etree
from io import StringIO, BytesIO
import urllib.request as request
import lxml.html

from baidu_tts import TTS


class Feed:

    def parseXMLByFile(self, xmlFile):

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
                if(elem.tag == "description"):
                    TTS().baidutts(text)

    def parseXMLByUrl(self, url):
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
                if(elem.tag == "description"):
                    TTS().baidutts(text)
