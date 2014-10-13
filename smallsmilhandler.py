#!/usr/bin/python
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista = []
        self.tags = [
            'root-layout', 'region', 'img', 'audio', 'textstream']
        self.atrib = {
            'root-layout': ['width', 'height'],
            'region': ['id', 'top', 'left'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
            }
    def startElement(self, name, attrs):
        dic = {}
        if name in self.tags:
            dic["name"] = name
            for key in self.atrib[name]:
                    dic[key] = attrs.get(key, "")
            self.lista.append(dic)
    def get_tags(self):
        return self.lista

if __name__ == "__main__":

    parser = make_parser()
    smallhandler = SmallSMILHandler()
    parser.setContentHandler(smallhandler)
    parser.parse(open('karaoke.smil'))
    print smallhandler.get_tags()
