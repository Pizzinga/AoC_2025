#--- Day 9: Movie Theater ---
#You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!
#
#The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).
#
#For example:
#
#7,1
#11,1
#11,7
#9,7
#9,5
#2,5
#2,3
#7,3
#Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:
#
#..............
#.......#...#..
#..............
#..#....#......
#..............
#..#......#....
#..............
#.........#.#..
#..............
#You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.
#
#For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:
#
#..............
#.......#...#..
#..............
#..#....#......
#..............
#..OOOOOOOO....
#..OOOOOOOO....
#..OOOOOOOO.#..
#..............
#Or, you could make a rectangle with area 35 between 7,1 and 11,7:
#
#..............
#.......OOOOO..
#.......OOOOO..
#..#....OOOOO..
#.......OOOOO..
#..#....OOOOO..
#.......OOOOO..
#.......OOOOO..
#..............
#You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:
#
#..............
#.......#...#..
#..............
#..OOOOOO......
#..............
#..#......#....
#..............
#.........#.#..
#..............
#Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:
#
#..............
#..OOOOOOOOOO..
#..OOOOOOOOOO..
#..OOOOOOOOOO..
#..OOOOOOOOOO..
#..OOOOOOOOOO..
#..............
#.........#.#..
#..............
#Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?

import numpy as np;
import scipy;
import matplotlib.pyplot as plt
#b=1
#a=np.arange(1,10,1);
#diago=b*np.sqrt(1+a);
#Area=b*b*a;
#
#plt.plot(a,Area,label="Area")
#plt.plot(a,diago,label="diagonale")
#plt.legend();
#plt.show();
#exit()


with open("Day9_input1.txt") as f:
    listo=f.readlines();
    N=len(listo);
    X=np.zeros((N,2))
    for i,l in enumerate(listo):
        tupl=l.split(",")
        X[i,:]=np.array([int(tupl[0]),int(tupl[1])]);
    #dist=scipy.spatial.distance.pdist(X, metric="cityblock");
    #dist=scipy.spatial.distance.squareform(dist);
    #sorted_indexes=np.argsort(dist,axis=None)
    #print(dist)
    #highest_dist_idx=sorted_indexes[-1];
    #i_row=highest_dist_idx//N;
    #j_col=highest_dist_idx%N
    MAX=0;
    for i_row in range(X.shape[0]):
        for j_col in range(i_row,X.shape[0]):
            Area=(np.abs(X[i_row,0]-X[j_col,0])+1)*(1+np.abs(X[i_row,1]-X[j_col,1]))
            if Area>MAX:
                MAX=Area;
    #min_x=min(X[i_row,0],X[j_col,0]);max_x=max(X[i_row,0],X[j_col,0]);
    #min_y=min(X[i_row,1],X[j_col,1]);max_y=max(X[i_row,1],X[j_col,1]);
    #print(f"After rectangle between X[{i_row}]={X[i_row,:]} and X[{j_col}]={X[j_col,:]}");


    print(f"largest area is {MAX}")