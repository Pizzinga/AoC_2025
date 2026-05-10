#--- Part Two ---
#The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes 
# together until they're all in one large circuit.
#
#Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is
#  between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from
#  the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117)
#  produces 25272.
#
#Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do
#  you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

import numpy as np;
import scipy;
with open("Day8_input1.txt") as f:
    listo=f.readlines();
    N=len(listo);
    X=np.zeros((N,3))
    for i,l in enumerate(listo):
        tupl=l.split(",")
        X[i,:]=np.array([int(tupl[0]),int(tupl[1]),int(tupl[2])]);
    dist=scipy.spatial.distance.pdist(X, metric='euclidean');
    dist=scipy.spatial.distance.squareform(dist);
    for i in range(N):
        dist[i,:i+1]=np.inf;
    sorted_indexes=np.argsort(dist,axis=None)

    #print(f"N={N} and the shape of the dist matrix is {dist.shape}")
    ##print(dist);
    #print(f"to sort it use sorted indexes with shape {sorted_indexes.shape}")
    joined_groups=[];
    for ind in sorted_indexes:
        
        i_row=ind//N;
        j_col=ind%N;
        
        #print(f"piu' vicini sono {ind}==> i_ROW={i_row}, j_COL={j_col}")
        GIA_PRESENTE=False;
        #print("the current joined groups are: ",joined_groups)
        k_i=-1;k_j=-1;
        for k in range(len(joined_groups)):
            if (i_row in joined_groups[k]) and (j_col in joined_groups[k]):
                GIA_PRESENTE=True;break;
            if i_row in joined_groups[k]:
                k_i=k;
                GIA_PRESENTE=True;
            elif j_col in joined_groups[k]:
                k_j=k;
                GIA_PRESENTE=True;
        if GIA_PRESENTE:
            if k_i!=-1 and k_j!=-1:
                joined_groups[k_i]=joined_groups[k_i]+joined_groups[k_j];
                joined_groups[k_j]=[];
            elif k_i!=-1:
                joined_groups[k_i].append(j_col)
            elif k_j!=-1:
                joined_groups[k_j].append(i_row)
            
            if len(joined_groups[k_i])==N or len(joined_groups[k_j])==N:
                print(f"--------> DONE the last 2 connected pairs were {i_row} and {j_col}: product of Xs is {X[i_row,0]*X[j_col,0]}")
                break;
        
        if not(GIA_PRESENTE):
            joined_groups.append([i_row,j_col]);
        #print(f"I want to join {i_row}({X[i_row,:]})<->{j_col}({X[j_col,:]})")
        #print("\nAfter joining the result is: ",joined_groups)
        #print("---------------------");