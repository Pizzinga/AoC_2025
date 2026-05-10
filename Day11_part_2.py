#--- Day 11: Reactor ---
#You hear some loud beeping coming from a hatch in the floor of the factory, so you decide to check it out. Inside, you find several large electrical conduits and a ladder.
#
#Climbing down the ladder, you discover the source of the beeping: a large, toroidal reactor which powers the factory above. Some Elves here are hurriedly running between the reactor and a nearby server rack, apparently trying to fix something.
#
#One of the Elves notices you and rushes over. "It's a good thing you're here! We just installed a new server rack, but we aren't having any luck getting the reactor to communicate with it!" You glance around the room and see a tangle of cables and devices running from the server rack to the reactor. She rushes off, returning a moment later with a list of the devices and their outputs (your puzzle input).
#
#For example:
#
#aaa: you hhh
#you: bbb ccc
#bbb: ddd eee
#ccc: ddd eee fff
#ddd: ggg
#eee: out
#fff: out
#ggg: out
#hhh: ccc fff iii
#iii: out
#Each line gives the name of a device followed by a list of the devices to which its outputs are attached. So, bbb: ddd eee means that device bbb has two outputs, one leading to device ddd and the other leading to device eee.
#
#The Elves are pretty sure that the issue isn't due to any specific device, but rather that the issue is triggered by data following some specific path through the devices. Data only ever flows from a device through its outputs; it can't flow backwards.
#
#After dividing up the work, the Elves would like you to focus on the devices starting with the one next to you (an Elf hastily attaches a label which just says you) and ending with the main output to the reactor (which is the device with the label out).
#
#To help the Elves figure out which path is causing the issue, they need you to find every path from you to out.
#
#In this example, these are all of the paths from you to out:
#
#Data could take the connection from you to bbb, then from bbb to ddd, then from ddd to ggg, then from ggg to out.
#Data could take the connection to bbb, then to eee, then to out.
#Data could go to ccc, then ddd, then ggg, then out.
#Data could go to ccc, then eee, then out.
#Data could go to ccc, then fff, then out.
#In total, there are 5 different paths leading from you to out.
#
#How many different paths lead from you to out?
from itertools import count
import numpy as np
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
    print(f"indice SOURCE (\"you\") is {SRC};  the Destination(\"out\") is {DEST} ")
    Value_nodes=np.zeros((N_VERT,),dtype=np.uint64);
    TOT=0;
    idx_dac=Dict_nomi_to_ID["dac"];
    idx_fft=Dict_nomi_to_ID["fft"];
    print("idx DAC ",idx_dac," idx FFT ",idx_fft)
    #print("----")
    #print(A.astype(np.uint8))
    #print("----")
    stack=deque();
    Value_nodes=np.zeros((N_VERT,),dtype=np.bool_);
    stack.append((SRC,Value_nodes));
    while len(stack)>0:
        #print("Len STACK: ",len(stack))
        nodo_actual,Value_nodes=stack.pop()
        if nodo_actual==DEST:
            if Value_nodes[idx_dac] and Value_nodes[idx_fft]:
                TOT+=1
                #print(Value_nodes.astype(np.uint8),"****")
            else:
                #print(Value_nodes.astype(np.uint8))
                pass;
            del Value_nodes
            continue;
        else:
            Value_nodes[nodo_actual]+=1;
        
        locco=np.where(A[nodo_actual,:]!=0)[0]
        for nodo_dest in locco:
            if Value_nodes[nodo_dest]==0:
                stack.append((nodo_dest,Value_nodes.copy()))
            
print(f" number of path che passano per \"dac\" e \"fft\" sono",TOT)
