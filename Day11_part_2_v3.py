
from itertools import count
import numpy as np
from queue import Queue
import copy
from collections import deque
#stack.append('a')
#stack.append('b')
#stack.append('c')
#
#print('Initial stack:')
#print(stack)
#
## pop() function to pop element from stack in LIFO order
#print('\nElements popped from stack:')
#print(stack.pop())
#print(stack.pop())
#print(stack.pop())

counto_ID=count();
TOT=0;
Wanted_N=0;
Dict_nomi_to_ID=dict();
with open("Day11_input1.txt") as f:
    li=f.readlines();
    N_VERT=len(li)+1;
    A=np.zeros((N_VERT,N_VERT),dtype=np.bool_)
    for r in li:
        r=r.replace("\n","").replace("\r","")
        r_l=r.split(":")
        #print(r_l)
        nodo_from=r_l[0];
        if nodo_from not in Dict_nomi_to_ID.keys():
            Dict_nomi_to_ID[nodo_from]=next(counto_ID);
            
        for nodo_to in r_l[1][1:].split(" "):
            if nodo_to not in Dict_nomi_to_ID.keys():
                Dict_nomi_to_ID[nodo_to]=next(counto_ID);
            A[Dict_nomi_to_ID[nodo_from],Dict_nomi_to_ID[nodo_to]]=1;




    print("dict at the end",Dict_nomi_to_ID)
    SRC=Dict_nomi_to_ID["svr"]
    DEST=Dict_nomi_to_ID["out"]
    print(f"indice SOURCE (\"srv\") is {SRC};  the Destination(\"out\") is {DEST} ")
    Value_nodes=np.zeros((N_VERT,),dtype=np.bool);
    TOT=0;
    idx_dac=Dict_nomi_to_ID["dac"];
    idx_fft=Dict_nomi_to_ID["fft"];
    print("idx DAC ",idx_dac," idx FFT ",idx_fft)

    stack=deque();
    stack.append((SRC,False,False,[]));
    #stack.append((idx_dac,False,False,[[],[]]));
    #stack.append((idx_fft,False,False,[[],[]]));
    Outdegree_nodo=np.sum(A,axis=1) # sum all the exiting
    print(sum(Outdegree_nodo))
    TERMINALI=[DEST]
    assert Outdegree_nodo[DEST]==0, "the dest node should have out-degree =0 "
    A_delete=np.zeros_like(A);
    nodi_visitati_questa_ricerca=[];
    KK=0;
    while len(stack)>0:#stack.qsize()>0:
        nodo_actual,trovato_DAC,trovato_FFT,nodi_visitati_questa_ricerca=stack.pop()
        #print(sum(Outdegree_nodo))
        #print(nodo_actual, "len nodi_visitati_in_quest_ricerca=",len(nodi_visitati_questa_ricerca),f"|| DAC {int(trovato_DAC)} , FFT {int(trovato_FFT)}")
        KK+=1;
        if nodo_actual not in nodi_visitati_questa_ricerca:
            nodi_visitati_questa_ricerca.append(int(nodo_actual));
        else:
            print(">OOOO< loop detected")
            continue;

        trovato_DAC=trovato_DAC or nodo_actual==idx_dac;
        trovato_FFT=trovato_FFT or nodo_actual==idx_fft;
        if nodo_actual in TERMINALI:
            print(f"#nodi_visited {len(nodi_visitati_questa_ricerca)} ||len TERMINALI={len(TERMINALI)}|| DAC {int(trovato_DAC)} , FFT {int(trovato_FFT)}")
            print(f"**** ",end="")
            if trovato_FFT and trovato_DAC:
                TOT+=1
                print("X")
            else:
                if Outdegree_nodo[nodi_visitati_questa_ricerca[-2]]<=1:
                    TERMINALI.append(nodi_visitati_questa_ricerca[-2]);
                    Outdegree_nodo[nodi_visitati_questa_ricerca[-2]]=0;
                print("NON")
            continue;
        
        locco=np.where(A[nodo_actual,:]!=0)[0]
  
        for nodo_dest in locco:
            lollo=copy.deepcopy(nodi_visitati_questa_ricerca);
            stack.append((int(nodo_dest),trovato_DAC,trovato_FFT,lollo))

print(f"volte che trovo sia FFT che DAC è {TOT}")