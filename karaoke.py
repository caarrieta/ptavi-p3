#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


def imprmirtags(sHandler):
    str_total = ""
    for dicc in self.lista_dic:
        etiqueta = dicc['name']
        attr = ""
        for key in dicc:
            if key != 'name' and dicc[key]:
                attr = attr + '\t' + key + "=" + '"' + dicc[key] + '"'
                str_total = str_total + etiqueta + attr + '\n'
    print str_total

try:

except IndexError:
    print "Usage: python karaoke.py file.smil."
    raise SystemExit
