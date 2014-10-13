#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

class karaokelocal():

    def __init__(self, fichero):
       parser = make_parser()
       sHandler = smallsmilhandler.SmallSMILHandler()
       parser.setContentHandler(sHandler)
       parser.parse(open(karaoke.py))
       self.lista_dic = sHandler.get_tags()

if __name__ == "__main__":

try:
    fichero = sys.argv[1]
except IndexError:
    print "Usage: python karaoke.py file.smil."
raise SystemExit

