#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.tags = []

    def StartElement(self, name, attrs):

        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.root_layout = {}
            self.atributos = (attrs, self.root_layout)
            self.tags.append([name, self.root_layout])
        elif name == 'region':
            self.region = {}
            self.atributos = (attrs, self.region)
            self.tags.append = ([name, self.region])
        elif name == 'img':
            self.img = {}
            self.atributos = (attrs, self.img)
            self.tags.append = ([name, self.img])
        elif name == 'audio':
            self.audio = {}
            self.atributos = (attrs, self.audio)
            self.tags.append = ([name, self.audio])
        elif name == 'texstream':
            self.textream = {}
            self.atributos = (attrs, self.region)
            self.tags.append = ([name, self.region])

    def atributos(self, attrs, dic):
        atrib = attrs.keys()
        n = 0
        while n < len(atrib):
            dic[str(atrib)]
            n = n + 1

    def get_tags(self):
        return self.tags

if __name__ == "__main__":

    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
