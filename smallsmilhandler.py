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
        self.img = ""
        self.im-src = ""
        self.im-region = ""
        self.im-begin = ""
        self.im-dur = ""
        self.audio = ""
        self.aud-src = ""
        self.aud-begin = ""
        self.aud-dur = "" 
        self.textstream = ""
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
            
        elif name == 'img':
            self.inRespuesta = 1
        elif name == 'audio':
        elif name == 'texstream':


