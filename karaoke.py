#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

def imprimirtags(sHandler):
    for etiqueta in sHandler.tags:
        print etiqueta[0], 
        atributos = etiqueta[1]
        for atributo in atributos:
            print "\t", atributo, "=", atributos[atributo],
        print
try:
    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.argv[1]))
    imprimirtags(sHandler)
except IndexError:
    print "Usage: python karaoke.py file.smil."
    raise SystemExit
