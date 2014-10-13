#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from xml.sax.handler import smallsmilhandler

class Karaoke (smallmilhandler.SmalSMILHandler)

    def __init__(self, fich):
        parser = make_parser()
        parser = make_parser()
        sHandler = shistesHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('fich'))      
        self.lista = sHandler.get_tags()
