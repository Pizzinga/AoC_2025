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


import numpy as np;
import scipy;
import matplotlib.pyplot as plt
def Fill_border(Mappa,Bordo):
    R=Bordo.shape[0];C=Bordo.shape[1];
    li=np.where(Bordo);
    kk=0;
    for i_true,j_true in zip(li[0],li[1]):
        print(f"{kk}")
        kk+=1
        #print("i_true,j_true=",i_true,j_true)
        #print(Mappa.astype(np.int8))
        #print("------------------------")
        #lungo_i_increasing_
        i=i_true+1
        while i<R and not(Bordo[i,j_true]): #finchè siamo false
            i+=1;
        if i<R:Mappa[i_true:i+1,j_true]=True;
        #lungo i_decreasing
        i=i_true-1
        while i>0 and not(Bordo[i,j_true]): #finchè siamo false
            i-=1;
        if i>0:Mappa[i:i_true+1,j_true]=True;
        #lungo j_increasing
        j=j_true+1
        while j<C and not(Bordo[i_true,j]): #finchè siamo false
            j+=1;
        if j<C:Mappa[i_true,j_true:j+1]=True;
        #lungo j_decreasing
        j=j_true-1
        while j>0 and not(Bordo[i_true,j]): #finchè siamo false
            j-=1;
        if j>0:Mappa[i_true,j:j_true+1]=True;
    return;
def Fill_border_v2(Bordo):
    R=Bordo.shape[0];C=Bordo.shape[1];
    print("dodd")
    li=np.where(Bordo);
    print("ddd where")
    kk=0;
    for i_true,j_true in zip(li[0],li[1]):
        print(f"{kk}")
        kk+=1
        #print("i_true,j_true=",i_true,j_true)
        #print(Mappa.astype(np.int8))
        #print("------------------------")
        #lungo_i_increasing_
        i=i_true+1
        while i<R and not(Bordo[i,j_true]): #finchè siamo false
            i+=1;
        if i<R:Bordo[i_true:i+1,j_true]=True;
        #lungo i_decreasing
        i=i_true-1
        while i>0 and not(Bordo[i,j_true]): #finchè siamo false
            i-=1;
        if i>0:Bordo[i:i_true+1,j_true]=True;
        #lungo j_increasing
        j=j_true+1
        while j<C and not(Bordo[i_true,j]): #finchè siamo false
            j+=1;
        if j<C:Bordo[i_true,j_true:j+1]=True;
        #lungo j_decreasing
        j=j_true-1
        while j>0 and not(Bordo[i_true,j]): #finchè siamo false
            j-=1;
        if j>0:Bordo[i_true,j:j_true+1]=True;
    return;
def valid_area_v2(Bordo,min_x,max_x,min_y,max_y):
    bordi_rettangolo=[(min_x,max_y),(max_x,min_y),(min_x,min_y),(max_x,max_y)]
    for x_punto,y_punto in bordi_rettangolo:
        if not(Bordo[x_punto,y_punto]):
            return False;
    return True;
        #if Bordo[x_punto-1:x_punto+1,y_punto-1:y_punto+1])==1:
        
def valid_area(Bordo,min_x,max_x,min_y,max_y):
    #return True;
    Vuoto_incontrato=False
    for i in range(min_x,max_x):
        if Vuoto_incontrato and Bordo[i,min_y]:
            return False;
        if not(Bordo[i,min_y]):
            Vuoto_incontrato=True;

    Vuoto_incontrato=False
    for j in range(min_y,max_y):
        if Vuoto_incontrato and Bordo[max_x,j]:
            return False;
        if not(Bordo[max_x,j]):
            Vuoto_incontrato=True
    
    Vuoto_incontrato=False
    for j in range(min_y,max_y):
        if Vuoto_incontrato and Bordo[min_x,j]:
            return False;
        if not(Bordo[min_x,j]):
            Vuoto_incontrato=True

    Vuoto_incontrato=False
    for i in range(min_x,max_x):
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
    Bordo=np.zeros([int(max(X[:,0])+2),int(max(X[:,1])+2)], dtype=np.bool_);
    print(N)
    #COCCO=0;
    for i in range(N):
        #print(f"{X[i,0]},{int(X[i,1])}")
        Bordo[int(X[i,0]),int(X[i,1])]=True;
        if X[i,0]==X[(i+1)%N,0]:
            ran=list(range(min(X[i,1],X[(i+1)%N,1]),         1+max(X[i,1],X[(i+1)%N,1]) ))
            Bordo[X[i,0],ran]=True;
        else:
            ran=list(range(min(X[i,0],X[(i+1)%N,0]),         1+max(X[i,0],X[(i+1)%N,0]) ))
            Bordo[ran,X[i,1]]=True;
    #print(Bordo.astype(np.int8))
    Fill_border_v2(Bordo);
    #print(Bordo.astype(np.int8))
    
    dist=scipy.spatial.distance.pdist(X, metric="cityblock");
    dist=scipy.spatial.distance.squareform(dist);
    sorted_indexes=np.argsort(dist,axis=None)[::-1];
    MAX=0;
    X=X.astype(np.float64)
    for o,idx in enumerate(sorted_indexes):
        i_row=idx//N;
        j_col=idx%N    
        #for i_row in range(N):
        #    for j_col in range(i_row,N):
        Area=(np.abs(X[i_row,0]-X[j_col,0])+1)*(1+np.abs(X[i_row,1]-X[j_col,1]))
        
        if Area>MAX: #and np.all(Mappa[min_x:max_x,min_y:max_y]):
            min_x=int(min(X[i_row,0],X[j_col,0]));max_x=int(max(X[i_row,0],X[j_col,0]));
            min_y=int(min(X[i_row,1],X[j_col,1]));max_y=int(max(X[i_row,1],X[j_col,1]));
            if valid_area_v2(Bordo,min_x,max_x,min_y,max_y):
                MAX=Area;
                print(f"{o}/{len(sorted_indexes)}: computed value={Area};   MAX value={MAX}")

    
    #min_x=min(X[i_row,0],X[j_col,0]);max_x=max(X[i_row,0],X[j_col,0]);
    #min_y=min(X[i_row,1],X[j_col,1]);max_y=max(X[i_row,1],X[j_col,1]);
    #print(f"After rectangle between X[{i_row}]={X[i_row,:]} and X[{j_col}]={X[j_col,:]}");


    print(f"largest area is {MAX}")