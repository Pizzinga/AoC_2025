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
def valid_area_v3(vertici,min_x,max_x,min_y,max_y,Bordo):
    bordi_rettangolo=[(min_x,max_y),(max_x,min_y),(min_x,min_y),(max_x,max_y)]
    print(f"rettangolo= {bordi_rettangolo[2]},{bordi_rettangolo[3]}")
    for x_punto,y_punto in bordi_rettangolo:
        #idx_tenere=np.where(np.logical_or(vertici[:,0]!=x_punto,vertici[:,1]!=y_punto))
        angoli=np.arctan2(y_punto-vertici[:,1],x_punto-vertici[:,0])
        print(angoli)
        differences=np.diff(angoli)
        print(f"shape di differences {differences.shape}")
        dodo=np.sum(differences)/(2*np.pi)
        print(f"the index  is {dodo}")
        #print(f"sum angoli={angoli}")
        if np.allclose(dodo,0.0):
            print(f"punto {x_punto},{y_punto} is outside of polygon")
            print("--->Non valido")

            return False;
        else:
            print(f"punto {x_punto},{y_punto} is INSIDE, sum_diffe_theta/2pi={dodo} ")
    print("--->Valido")
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



with open("Day9_input1.txt") as f:
    listo=f.readlines();
    N=len(listo);
    X=np.zeros((N,2),dtype=np.uint32)
    for i,l in enumerate(listo):
        tupl=l.split(",")
        X[i,:]=np.array([int(tupl[0]),int(tupl[1])],dtype=np.uint32);
    Bordo=np.zeros([int(max(X[:,0])+2),int(max(X[:,1])+2)], dtype=np.bool_);
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
    #KB=Bordo.astype(np.int8);
    #KB=np.concatenate([np.arange(0,KB.shape[1],1).reshape(1,KB.shape[1]),KB],axis=0)
    #KB=np.concatenate([np.arange(-1,KB.shape[0]-1,1).reshape(KB.shape[0],1),KB],axis=1)
    #print(KB)
    
    #dist=scipy.spatial.distance.pdist(X, metric="cityblock");
    #dist=scipy.spatial.distance.squareform(dist);
    #sorted_indexes=np.argsort(dist,axis=None)[::-1];
    MAX=0;
    X=X.astype(np.float64)
    print(X.shape)
    #X=np.row_stack([X,X[0,:]])
    print(X.shape)
    
     #for o,idx in enumerate(sorted_indexes):
        #i_row=idx//N;
        #j_col=idx%N    
    for i_row in range(N):
        for j_col in range(i_row+1,N):
            Area=(np.abs(X[i_row,0]-X[j_col,0])+1)*(1+np.abs(X[i_row,1]-X[j_col,1]))
            if Area>MAX: #and np.all(Mappa[min_x:max_x,min_y:max_y]):
                min_x=int(min(X[i_row,0],X[j_col,0]));max_x=int(max(X[i_row,0],X[j_col,0]));
                min_y=int(min(X[i_row,1],X[j_col,1]));max_y=int(max(X[i_row,1],X[j_col,1]));
                if valid_area_v1(Bordo,min_x,max_x,min_y,max_y):#valid_area_v2(Bordo,min_x,max_x,min_y,max_y):
                    MAX=Area;
                    #print(f"{o}/{len(sorted_indexes)}: computed value={Area};   MAX value={MAX}")

    
    #min_x=min(X[i_row,0],X[j_col,0]);max_x=max(X[i_row,0],X[j_col,0]);
    #min_y=min(X[i_row,1],X[j_col,1]);max_y=max(X[i_row,1],X[j_col,1]);
    #print(f"After rectangle between X[{i_row}]={X[i_row,:]} and X[{j_col}]={X[j_col,:]}");


    print(f"largest area is {MAX}")