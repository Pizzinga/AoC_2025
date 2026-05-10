#--- Day 4: Printing Department ---
#You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
#
#Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
#
#"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
#
#If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
#
#The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
#
#For example:
#
#..@@.@@@@.
#@@@.@.@.@@
#@@@@@.@.@@
#@.@@@@..@.
#@@.@@@@.@@
#.@@@@@@@.@
#.@.@.@.@@@
#@.@@@.@@@@
#.@@@@@@@@.
#@.@.@@@.@.
#The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
#
#In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
#
#..xx.xx@x.
#x@@.@.@.@@
#@@@@@.x.@@
#@.@@@@..@.
#x@.@@@@.@x
#.@@@@@@@.@
#.@.@.@.@@@
#x.@@@.@@@@
#.@@@@@@@@.
#x.x.@@@.x.
#Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
import numpy as np;

with open("Day4_part1.txt") as f:
    linee=f.readlines();
    R=len(linee);C=len(linee[0])-1
    M=np.zeros((R,C),dtype=np.bool_)
    for i,row in enumerate(linee):
        row=row.replace("\n","")
        M[i,:]=np.array([1 if c=="@" else 0 for c in row],dtype=np.bool_);
    #print(M)
    row_ind,col_ind=np.where(M)
    S=0;
    PICKED=np.zeros_like(M)
    for r,c in zip(row_ind,col_ind):
        assert M[r,c], f"M[{r},{c}] is not True. its value is {M[r,c]}";
        r_min=max(0,r-1);r_max=min(R-1,r+1);
        c_min=max(0,c-1);c_max=min(C-1,c+1)
        #print(f"{M[r_min:r_max+1,c_min:c_max+1]}--> sum is {np.sum(M[r_min:r_max,c_min:c_max],axis=None)-1}" )
        if np.sum(M[r_min:r_max+1,c_min:c_max+1],axis=None)-1 <4:
            S+=1
            PICKED[r,c]=1;
    import matplotlib.pyplot as plt
    print(f"you can pick {S} rolls")
    plt.subplot(2,1,1)
    plt.imshow(M);plt.title("Original ROLLS")
    plt.subplot(2,1,2)
    plt.imshow(PICKED);plt.title("PICKED ONES")
    plt.show();
