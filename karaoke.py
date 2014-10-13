#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import small
import sys
import os

class KaraokeLocal():

    def __init__(self, fich):
        parser = make_parser()
        sHandler = small.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(fich)
        self.lista = sHandler.get_tags()
  
    def __str__(self):

        for diccionario in self.lista:
            salida = diccionario["name"]
            for tags in diccionario:
                if diccionario[tags] and tags != "name":
                    salida = "\t", tags, "=", diccionario[tags] + "", "\n"
            return salida

    def do_local(self):
        for diccionario in self.lista:
            if diccionario[tags].find("http://") == 0:
                recurso = diccionario[tags]
                os.system("wget -q " + recurso)
                new = diccionario[tags].split('/')[-1]
                diccionario[tags] = new

if __name__ == "__main__":

    try:
        fich = open(sys.argv[1], 'r')
    except IOError:
        print "Usage: python karaoke.py file.smil"
        raise SystemExit

    Karaoke = KaraokeLocal(fich)
    print Karaoke
    Karaoke.do_local()
    print Karaoke

