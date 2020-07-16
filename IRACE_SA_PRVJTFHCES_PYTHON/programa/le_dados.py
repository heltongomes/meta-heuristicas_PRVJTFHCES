# -*- coding: utf-8 -*-
"""
LEITURA DE DADOS DAS INSTÂNCIAS

@author: Helton Gomes
"""

# IMPORTANDO BIBLIOTECAS
import numpy as np
from copy import deepcopy

# FUNÇÃO PARA LEITURA DOS DADOS EM UM ARQUIVO TXT
def ler_dados(nomearq):
    lista = []
    cap = []
    dem = []
    pic = []
    ts = []
    ti = []
    tf = []
    with open(nomearq, "r") as arquivo:
        for linha in arquivo.readlines():
            ret = linha
            ret = ret.split(" ")
            for i, coluna in enumerate(ret):
                ret[i] = int(ret[i])
            lista.append(ret)
    
    # NÚMERO DE CIDADES
    cid = lista[0][0]
    
    # NÚMERO DE VEÍCULOS
    veic = lista[1][0]
    
    # CAPACIDADES DOS VEÍCULOS
    for i in range(veic):
        cap.append(lista[2][i])
    
    # DEMAIS DADOS DAS INSTÂNCIAS
    for i in range(cid+1):
        dem.append(lista[i+3][0]) # DEMANDA DE ENTREGA
        pic.append(lista[i+3][1]) # DEMANDA DE COLETA
        ts.append(lista[i+3][2])  # TEMPO DE SERVIÇO
        ti.append(lista[i+3][3])  # INÍCIO DA JANELA DE TEMPO
        tf.append(lista[i+3][4]) # FINAL DA JANELA DE TEMPO
    
    c = deepcopy(lista)
    c.remove(c[0])
    c.remove(c[0])
    c.remove(c[0])

    for i in range(cid+1):
        c.remove(c[0])

    t = deepcopy(c)

    return cid, veic, cap, pic, dem, ts, ti, tf, c, t