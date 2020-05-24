
from pygame import mixer
import time
valor = str

def bip():
    mixer.init()
    mixer.music.load('bip.mp3')
    mixer.music.play()

def Dig1():
    global valor
    D = str(valor)
    valor = D + '1'
    print(valor)
    bip()


def Dig2():
    global valor
    D = str(valor)
    valor = D + '2'
    print(valor)
    bip()

def Dig3():
    global valor
    D = str(valor)
    valor = D + '3'
    print(valor)
    bip()

def Dig4():
    global valor
    D = str(valor)
    valor = D + '4'
    print(valor)
    bip()

def Dig5():
    global valor
    D = str(valor)
    valor = D + '5'
    print(valor)
    bip()

def Dig6():
    global valor
    D = str(valor)
    valor = D + '6'
    print(valor)
    bip()

def Dig7():
    global valor
    D = str(valor)
    valor = D + '7'
    print(valor)
    bip()

def Dig8():
    global valor
    D = str(valor)
    valor = D + '8'
    print(valor)
    bip()

def Dig9():
    global valor
    D = str(valor)
    valor = D + '9'
    print(valor)
    bip()

def Dig0():
    global valor
    D = str(valor)
    valor = D + '0'
    print(valor)
    bip()

def DigDel():
    global valor
    D = str(valor)
    valor = D + 'apagado'
    print(valor)
    bip()

def DigMais():
    global valor
    D = str(valor)
    valor = D + ' + '
    print(valor)
    bip()

def DigMenos():
    global valor
    D = str(valor)
    valor = D + ' - '
    print(valor)
    bip()

def Digmult():
    global valor
    D = str(valor)
    valor = D + ' X '
    print(valor)
    bip()


def DigDiv():
    global valor
    D = str(valor)
    valor = D + ' / '
    print(valor)
