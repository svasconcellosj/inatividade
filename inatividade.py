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

def abreArquivoContador(arquivo):
    arqInativo = open(arquivo, 'w')
    tempoAcumulado = 0
    arqInativo.write(str(tempoAcumulado))
    arqInativo.close()
    return int(tempoAcumulado)
    
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
teclaPressionada = ""
arqInativo = "inativo"
espera = 300

threads = [Thread(target=funcs.listen, kwargs={"tecla":tecla}) for tecla in teclado]
for thread in threads:
	thread.start()

tempoAcumulado = funcs.abreArquivoContador(arqInativo)
inativo = 0
grava = False
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
            if ( inativo > 300 ):
                tempoAcumulado += inativo
                funcs.gravaInatividade(arqInativo,tempoAcumulado)
                inativo = 0
    else:
        if ( teclaPressionada == ultimaTecla ):
            teclaPressionada = ""
        if inativo != 0:
            grava = True    
    if grava:
        tempoAcumulado += inativo
        funcs.gravaInatividade(arqInativo,tempoAcumulado)
        inativo = 0
        teclaPressionada = ""
        grava = False

