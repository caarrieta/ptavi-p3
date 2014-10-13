#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


try:
    parser = make_parser()
    SHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open(sys.arg[1]))
    imprimirtags(sHandler)
except IndexError:
    print "Usage: python karaoke.py file.smil."
    raise SystemExit
