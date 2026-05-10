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
def Fill_border_v3(Bordo,i_c_start,NNZ_Bordo):
    R=Bordo.shape[0];C=Bordo.shape[1];
    i_true=i_c_start[0];j_true=i_c_start[1]
    if Bordo[i_true+1,j_true]==2:i_true=i_true+1;
    elif Bordo[i_true,j_true+1]==2:j_true=j_true+1;
    elif Bordo[i_true-1,j_true]==2:i_true=i_true-1;
    elif Bordo[i_true,j_true-1]==2:j_true=j_true-1;
    else:
        raise(ValueError("Starting point does not have a neighbor with value 2"))
    kk=0;
    while i_true!=i_c_start[0] or j_true!=i_c_start[1]:
    #for i_true,j_true in zip(li[0],li[1]):
        Bordo[i_true,j_true]=3;
        print(f"{kk} / {NNZ_Bordo}  ({i_true},{j_true}) != ({i_c_start[0]},{i_c_start[1]})  ||         value of Bordo[{i_true},{j_true}]={Bordo[i_true,j_true]}")
        kk+=1
        #print("i_true,j_true=",i_true,j_true)
        #print(Mappa.astype(np.int8))
        #print("------------------------")
        #lungo_i_increasing_
        i=i_true+1
        while i<R and not(Bordo[i,j_true]): #finchè siamo false
            i+=1;
        if i<R:
            i_range=[ii for ii in range(i_true+1,i+1) if Bordo[ii,j_true]==0]
            Bordo[i_range,j_true]=1;
        #lungo i_decreasing
        i=i_true-1
        while i>0 and not(Bordo[i,j_true]): #finchè siamo false
            i-=1;
        if i>0:
            i_range=[ii for ii in range(i,i_true) if Bordo[ii,j_true]==0]
            Bordo[i_range,j_true]=1;
        #lungo j_increasing
        j=j_true+1
        while j<C and not(Bordo[i_true,j]): #finchè siamo false
            j+=1;
        if j<C:
            j_range=[jj for jj in range(j_true+1,j+1) if Bordo[i_true,jj]==0]
            Bordo[i_true,j_range]=1;
        #lungo j_decreasing
        j=j_true-1
        while j>0 and not(Bordo[i_true,j]): #finchè siamo false
            j-=1;
        if j>0:
            j_range=[jj for jj in range(j,j_true) if Bordo[i_true,jj]==0]
            Bordo[i_true,j_range]=1;

        #print(f"value of Bordo[{i_true},{j_true}]={Bordo[i_true,j_true]}")
        #print(Bordo[i_true-1:i_true+2,j_true-1:j_true+2])
        if Bordo[i_true+1,j_true]==2:i_true=i_true+1;
        elif Bordo[i_true,j_true+1]==2:j_true=j_true+1;
        elif Bordo[i_true-1,j_true]==2:i_true=i_true-1;
        elif Bordo[i_true,j_true-1]==2:j_true=j_true-1;
        else:
            raise(ValueError("Starting point does not have a neighbor with value 2"))
    return;
def valid_area_filledfast(Bordo,min_x,max_x,min_y,max_y):
    bordi_rettangolo=[(min_x,max_y),(max_x,min_y),(min_x,min_y),(max_x,max_y)]
    for x_punto,y_punto in bordi_rettangolo:
        if not(Bordo[x_punto,y_punto]):
            return False;
    return True;
def valid_area_v1(Bordo,min_x,max_x,min_y,max_y):
    bordi_rettangolo=[(min_x,max_y),(max_x,min_y),(min_x,min_y),(max_x,max_y)]
    Bordo=Bordo.astype(np.int8)
    Printo=Bordo.copy()
    #for x_punto,y_punto in bordi_rettangolo:
    #    Bordo[x_punto,y_punto]=1;
    #    Printo[x_punto,y_punto]=2
    #print(Printo)
    #print("________")
    diff_1=np.diff(np.concatenate([np.ones((1,)),Bordo[min_x+1:max_x-1,min_y]]));
    #print(f"diff_1 X-dir (min_Y)= {diff_1}")
    if np.sum(diff_1)==0 and np.any(diff_1!=0):
        #print("return non-VALID")
        return False;


    diff_2=np.diff(np.concatenate([np.ones((1,)),Bordo[min_x+1:max_x-1,max_y]]))
    #print(f"diff_2 X-dir (max_Y)= {diff_2}")
    if np.sum(diff_2)==0 and np.any(diff_2!=0):
        #print("return non-VALID")
        return False;


    diff_3=np.diff(np.concatenate([np.ones((1,)),Bordo[min_x,min_y+1:max_y-1]]))
    #print(f"diff_3 Y-dir (min_X)= {diff_3}")
    if np.sum(diff_3)==0 and np.any(diff_3!=0):
        #print("return non-VALID")
        return False;


    diff_4=np.diff(np.concatenate([np.ones((1,)),Bordo[max_x,min_y:max_y-1]]));
    #print(f"diff_4 Y-dir (max_X)= {diff_4}")
    if np.sum(diff_4)==0 and np.any(diff_4!=0):
        #print("return non-VALID")
        return False;

    #print("return VALID")
    #print("---")
    return True;

def valid_area(Bordo,min_x,max_x,min_y,max_y):
    #return True;
    Vuoto_incontrato=False
    for i in range(min_x,max_x-1):
        if Vuoto_incontrato and Bordo[i,min_y]:
            return False;
        if not(Bordo[i,min_y]):
            Vuoto_incontrato=True;

    Vuoto_incontrato=False
    for j in range(min_y,max_y-1):
        if Vuoto_incontrato and Bordo[max_x,j]:
            return False;
        if not(Bordo[max_x,j]):
            Vuoto_incontrato=True
    
    Vuoto_incontrato=False
    for j in range(min_y,max_y-1):
        if Vuoto_incontrato and Bordo[min_x,j]:
            return False;
        if not(Bordo[min_x,j]):
            Vuoto_incontrato=True

    Vuoto_incontrato=False
    for i in range(min_x,max_x-1):
        if Vuoto_incontrato and Bordo[i,max_y]:
            return False;
        if not(Bordo[i,max_y]):
            Vuoto_incontrato=True;
    return True;

with open("Day9_input1.txt") as f:
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
        Bordo[int(X[i,0]),int(X[i,1])]=2;
        if X[i,0]==X[(i+1)%N,0]:
            questo_lato=list(range(min(X[i,1],X[(i+1)%N,1]),         1+max(X[i,1],X[(i+1)%N,1]) ))
            Bordo[X[i,0],questo_lato]=2;
        else:
            questo_lato=list(range(min(X[i,0],X[(i+1)%N,0]),         1+max(X[i,0],X[(i+1)%N,0]) ))
            Bordo[questo_lato,X[i,1]]=2;
        NNZ_Bordo+=len(questo_lato);
    Fill_border_v3(Bordo,X[0,:],NNZ_Bordo);
    print("fine border creation and FILLING")

    #Printo=Bordo.astype(np.uint8);
    #print(Printo)

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