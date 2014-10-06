#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContenHandler):

    def __init__(self):
    """
    Constructor. Inicializamos las variables
    """
        self.lo-width = ""
        self.lo-height = ""
        self.lo-background-color = ""

        self.rg.id = ""
        self.rg-top = ""
        self.rg-bottom = ""
        self.rg-left = ""
        self.rg-right = ""

        self.im-src = ""
        self.im-region = ""
        self.im-begin = ""
        self.im-dur = ""

        self.aud-src = ""
        self.aud-begin = ""
        self.aud-dur = "" 

        self.ts-src = ""
        self.ts-region = ""

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.lo-width = attrs.get('width', "")
            self.lo-height = attrs.get('height', "")
            self.lo-background-color = attrs.get('background-color', "")
        elif name == 'region':
            self.rg.id = attrs.get('id', "")
            self.rg-top = attrs.get('top', "")
            self.rg-bottom = attrs.get('bottom', "")
            self.rg-left = attrs.get('left', "")
            self.rg-right = attrs.get('right', "")
        elif name == 'img':
            self.im-src = attrs.get('src', "")
            self.im-region = attrs.get('region', "")
            self.im-begin = attrs.get('begin', "")
            self.im-dur = attrs.get('dur', "")
        elif name == 'audio':
            self.aud-src = attrs.get('src', "")
            self.aud-begin = attrs.get('begin', "")
            self.aud-dur = attrs.get('dur', "")
        elif name == 'texstream':
            self.ts-src = attrs.get('src', "")
            self.ts-region = attrs.get('region', "")


