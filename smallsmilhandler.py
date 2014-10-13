#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContenHandler):

    def __init__(self):

        self.root_lo = []
        self.rg = []
        self.im = []
	self.aud-src = []
        self.aud-begin = []
        self.ts = [] 


    def get_tags(self, name, attrs):

        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.root_layout = {}
            self.atributos = (attrs, self.root_layout)
            self.root_lo.append([name, 
        elif name == 'region':
      
        elif name == 'img':

        elif name == 'audio':

        elif name == 'texstream':



