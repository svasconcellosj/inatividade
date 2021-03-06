#
# Descricao: Script para contar o tempo do host sem está sendo utilizado
#
# Autor: Sergio Vasconcellos Junior - svascconcellosj@hotmail.com
# Data: 30/07/2020
#

import string
from threading import *
import pyautogui
import time
import os.path
import time
import keyboard
import sys


#### Funções de manipulações###    
def gravaInatividade(arquivo, tempo):
    arqInativo = open(arquivo, 'w')
    arqInativo.write(str(tempo))
    arqInativo.close()

def listen(tecla):
	global teclaPressionada
	while True:
		keyboard.wait(tecla)
		teclaPressionada = tecla

teclado = list(string.ascii_lowercase)

threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclado]
for thread in threads:
	thread.start()

### Início  ###
teclaPressionada = ""
arqInativo = "c:\zabbix\inativo"
espera = 300
tempoAcumulado = 0
inativo = 0
grava = False

gravaInatividade(arqInativo,tempoAcumulado)

while True:
    pscX, pscY = pyautogui.position()
    time.sleep(espera)
    pscZ, pscT = pyautogui.position()
    ultimaTecla = teclaPressionada
    if pscX == pscZ and teclaPressionada == "":
        while pscX == pscZ and teclaPressionada == "":
            time.sleep(1)
            inativo += 1
            pscZ, pscT = pyautogui.position()
            if ( inativo > espera ):
                tempoAcumulado += inativo
                gravaInatividade(arqInativo,tempoAcumulado)
                inativo = 0
    else:
        if ( teclaPressionada == ultimaTecla ):
            teclaPressionada = ""
        if inativo != 0:
            grava = True    
    if grava:
        tempoAcumulado += inativo
        gravaInatividade(arqInativo,tempoAcumulado)
        inativo = 0
        teclaPressionada = ""
        grava = False

