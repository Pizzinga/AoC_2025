#The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

#In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.
#
#Using the same example as before, the tiles marked X would be green:
#
#..............
#.......#XXX#..
#.......X...X..
#..#XXXX#...X..
#..X........X..
#..#XXXXXX#.X..
#.........X.X..
#.........#X#..
#..............
#In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:
#
#..............
#.......#XXX#..
#.......XXXXX..
#..#XXXX#XXXX..
#..XXXXXXXXXX..
#..#XXXXXX#XX..
#.........XXX..
#.........#X#..
#..............
#The remaining tiles are never red nor green.
#
#The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.
#
#For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:
#
#..............
#.......OOOOO..
#.......OOOOO..
#..#XXXXOOOOO..
#..XXXXXXXXXX..
#..#XXXXXX#XX..
#.........XXX..
#.........#X#..
#..............
#Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:
#
#..............
#.......#XXX#..
#.......XXXXX..
#..#XXXX#XXXX..
#..XXXXXXXXXX..
#..#XXXXXXOXX..
#.........OXX..
#.........OX#..
#..............
#The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:
#
#..............
#.......#XXX#..
#.......XXXXX..
#..OOOOOOOOXX..
#..OOOOOOOOXX..
#..OOOOOOOOXX..
#.........XXX..
#.........#X#..
#..............
#Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?

import time
import numpy as np;
import scipy;
import matplotlib.pyplot as plt
def Fill_border_v2(Bordo,i_c_start,NNZ_Bordo):
    R=Bordo.shape[0];C=Bordo.shape[1];
    for i in range(R):
        esterni=True;
        for j in range(C):
            if Bordo[i,j]==1:
                esterni=False;
            if not(esterni):
                if Bordo[i,j]==0:
                    if j<C//2:
                        Bordo[i,j]=np.sum(Bordo[i,:j+1])%2;
                        #if np.sum(Bordo[i,:j])%2==0:
                        #    Bordo[i,j]=0;
                        #else:
                        #    Bordo[i,j]=1
                    else:
                        Bordo[i,j]=np.sum(Bordo[i,j-1:])%2;
                if Bordo[i,j]==0:
                    esterni=True



def Fill_border(Bordo,i_c_start,NNZ_Bordo):
    R=Bordo.shape[0];C=Bordo.shape[1];
    for i in range(R):
        riempi=False;
        delay=False;
        for j in range(C):
            if delay:
                if Bordo[i,j]==0:
                    delay=False;
            else:
                if Bordo[i,j]:
                    riempi=not(riempi);
                    delay=True;
            
            if not(delay):
                Bordo[i,j]=int(riempi)
    
    ripulisci(Bordo)
def ripulisci(Bordo):
    continua=True;
    R=Bordo.shape[0];C=Bordo.shape[1];
    while(continua):
        continua=False;
        for i in range(R):
            for j in range(C):
                if Bordo[i,j]:
                    if not np.sum(Bordo[i-1:i+2,j-1:j+2])>3:
                        Bordo[i,j]=0
                        continua=True

def valid_area_filledfast(Bordo,min_x,max_x,min_y,max_y):
    bordi_rettangolo=[(min_x,max_y),(max_x,min_y),(min_x,min_y),(max_x,max_y)]
    for x_punto,y_punto in bordi_rettangolo:
        if not(Bordo[x_punto,y_punto]):
            return False;
    return True;

with open("Day9_input1_1.txt") as f:
    listo=f.readlines();
    N=len(listo);
    X=np.zeros((N,2),dtype=np.uint32)
    for i,l in enumerate(listo):
        tupl=l.split(",")
        X[i,:]=np.array([int(tupl[0]),int(tupl[1])],dtype=np.uint32);
    NNZ_Bordo=0

    Bordo=np.zeros([int(max(X[:,0])+2),int(max(X[:,1])+2)], dtype=np.uint8);
    #COCCO=0;
    differenze_stessa_dir=0;
    prev_dire="NULL";
    i_max_lista=[]
    for i in range(N):
        #print(f"{X[i,0]},{int(X[i,1])}")
        Bordo[int(X[i,0]),int(X[i,1])]=1;
        if X[i,0]==X[(i+1)%N,0]:
            questo_lato=list(range(min(X[i,1],X[(i+1)%N,1]),         1+max(X[i,1],X[(i+1)%N,1]) ))
            Bordo[X[i,0],questo_lato]=1;
        else:
            questo_lato=list(range(min(X[i,0],X[(i+1)%N,0]),         1+max(X[i,0],X[(i+1)%N,0]) ))
            Bordo[questo_lato,X[i,1]]=1;
        NNZ_Bordo+=len(questo_lato);
    Fill_border_v2(Bordo,X[0,:],NNZ_Bordo);
    print("fine border creation and FILLING")

    Printo=Bordo.astype(np.uint8);
    print(Printo)

    MAX=0;
    X=X.astype(np.float64)
    start_cumu = time.time()

    for i_row in range(N):
        start = time.time()
        for j_col in range(i_row+1,N):
            Area=(np.abs(X[i_row,0]-X[j_col,0])+1)*(1+np.abs(X[i_row,1]-X[j_col,1]))
            if Area>MAX: #and np.all(Mappa[min_x:max_x,min_y:max_y]):
                min_x=int(min(X[i_row,0],X[j_col,0]));max_x=int(max(X[i_row,0],X[j_col,0]));
                min_y=int(min(X[i_row,1],X[j_col,1]));max_y=int(max(X[i_row,1],X[j_col,1]));
                if valid_area_filledfast(Bordo,min_x,max_x,min_y,max_y):#valid_area_v2(Bordo,min_x,max_x,min_y,max_y):
                    MAX=Area;
                    #print(f"{o}/{len(sorted_indexes)}: computed value={Area};   MAX value={MAX}")
        print (f"i_row ({i_row}/{N}) , MAX is {MAX} ,time spent this cycle={time.time()-start}s, total time spent={time.time()-start_cumu}s")

    
    #min_x=min(X[i_row,0],X[j_col,0]);max_x=max(X[i_row,0],X[j_col,0]);
    #min_y=min(X[i_row,1],X[j_col,1]);max_y=max(X[i_row,1],X[j_col,1]);
    #print(f"After rectangle between X[{i_row}]={X[i_row,:]} and X[{j_col}]={X[j_col,:]}");


    print(f"largest area is {MAX}")