#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import small
import sys

if __name__ == "__main__":
	
    parser = make_parser()
    small = small.SmallSMILHandler()
    parser.setContentHandler(small)

    try:
        fich = open(sys.argv[1],'r')
    except IOError:
        print "Usage: python karaoke.py file.smil"
        raise SystemExit
	
    parser.parse(fich)
    lista = small.get_tags()

    for diccionario in lista:
        print diccionario["name"],
        for tags in diccionario:
            if diccionario[tags] and tags != "name":
                print "\t", tags , "=" , diccionario[tags] + "",
		print
