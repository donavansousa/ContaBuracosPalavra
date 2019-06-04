#! /usr/bin/env python 
# -*- coding: utf-8 -*
from __future__ import unicode_literals
import re

import unicodedata

valoresLetras= {'a':1,'A':1, 'b':1,'B':2,'d':1,'D':1,'e':1,'g':1,'o':1,'O':1,'p':1,'P':1,'q':1,'Q':1,'R':1}

def contaBuracoPalavra(palavra):
        palavra=removeAcentos(palavra)
        buracos=0
        for letra in palavra:
                if letra in valoresLetras:
                        buracos = buracos + valoresLetras[letra]
        return buracos

def removeAcentos(palavra):
        nfkd=unicodedata.normalize('NFKD',palavra)
        palavraSemAcento=u"".join([c for c in nfkd if not unicodedata.combining(c)])
        return re.sub('[^a-zA-Z0-9 \\\]','',palavraSemAcento)

if __name__ == '__main__':
        palavra = input('Entre com a palavra: ')
        print(contaBuracoPalavra(palavra))
        
