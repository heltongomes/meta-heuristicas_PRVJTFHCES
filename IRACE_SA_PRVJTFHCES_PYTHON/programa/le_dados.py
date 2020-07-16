# -*- coding: utf-8 -*-
"""
LEITURA DE DADOS

@author: helton gomes
"""

import numpy as np
from copy import deepcopy

def leitura_dados():

    nmq = np.loadtxt('nmq.txt', dtype=np.int) 
    cid = nmq[0] # numero de cidades
    veic = nmq[1] # numero de veiculos

    cap = np.loadtxt( 'cap.txt', dtype=np.int) # capacidades dos veiculos     
    pic = np.loadtxt( 'p.txt', dtype=np.int) # pickup
    dem = np.loadtxt( 'd.txt', dtype=np.int) # demand
    ts = np.loadtxt('ts.txt', dtype=np.int) # tempos de serviço
    ti = np.loadtxt('a.txt', dtype=np.int) # inicio janela de tempo 
    tf = np.loadtxt('b.txt', dtype=np.int) # fim janela de tempo

    c = np.zeros((cid + 1, cid + 1), dtype=np.int) # criação de uma matriz vazia de tamanho cid x cid
    c = np.loadtxt('c.txt') # custos de transporte entre as cidades
    
    t = np.zeros((cid + 1, cid + 1), dtype=np.int) # criação de uma matriz vazia de tamanho cid x cid
    t = np.loadtxt('t.txt') # tempos de viagem entre as cidades
    
    return cid, veic, cap, pic, dem, ts, ti, tf, c, t

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
            # print(ret)
            ret = ret.split(" ")
            for i, coluna in enumerate(ret):
                ret[i] = int(ret[i])
            lista.append(ret)
            #print(ret)
    # arquivo.close()
    #print(lista)
    cid = lista[0][0]# número de cidades
    #print(f"Numero cidades = {cid}")
    veic = lista[1][0]# número de veículos
    #print(f"Numero veiculos = {veic}")
    # Capacidade dos Veículos
    for i in range(veic):
        cap.append(lista[2][i])
    #print(cap)
    # Lendo demais dados do problema
    for i in range(cid+1):
        dem.append(lista[i+3][0]) # demanda de entrega
        pic.append(lista[i+3][1]) # demanda de coleta
        ts.append(lista[i+3][2])  # tempo de serviço
        ti.append(lista[i+3][3])  # inicio da janela de tempo
        tf.append(lista[i+3][4]) # final da janela de tempo
    #print(dem)
    #print(pic)
    #print(ts)
    #print(ti)
    #print(tf)
    c = deepcopy(lista)
    #print(c)
    c.remove(c[0])
    #print(c)
    c.remove(c[0])
    #print(c)
    c.remove(c[0])
    #print(c)
    for i in range(cid+1):
        c.remove(c[0])
    #print(c)
    t = deepcopy(c)

    return cid, veic, cap, pic, dem, ts, ti, tf, c, t

def imprimir_dados(nomearq1, nomearq2, ncid, nvei, fo_ini, fo, tcomp):
    with open(nomearq1, "a") as arquivo:
        arquivo.write(f"{nomearq2} \t {ncid} \t {nvei} \t {fo_ini} \t {fo} \t {tcomp:5.2f} segundos \n")


