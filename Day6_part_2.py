#--- Part Two ---
#The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.
#
#Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)
#
#Here's the example worksheet again:
#
#123 328  51 64 
# 45 64  387 23 
#  6 98  215 314
#*   +   *   +  
#Reading the problems right-to-left one column at a time, the problems are now quite different:
#
#The rightmost problem is 4 + 431 + 623 = 1058
#The second problem from the right is 175 * 581 * 32 = 3253600
#The third problem from the right is 8 + 248 + 369 = 625
#Finally, the leftmost problem is 356 * 24 * 1 = 8544
#Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
#
#Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
import numpy as np;
S=0;
with open("Day6_input1.txt") as f:
    l=f.readlines();
    R=len(l);C=len(l[0]);
    M=np.zeros((R,C),dtype="U1")
    print("shape di M:", M.shape)
    for i,r in enumerate(l):
        r.replace("\n","")
        for j,char in enumerate(list(r)):
            print(f"{i},{j}={char}")
            M[i,j]=char;
    ACCUMUL=[];
    segno="";
    for j in range(C):
        if np.all(M[:,j]==" ") or np.any(M[:,j]=="\n"):
            if segno=="*":
                Mol=1;
                for aa in ACCUMUL:
                    Mol*=aa;
                S+=Mol
            if segno=="+":
                S+=sum(ACCUMUL);
            ACCUMUL=[];
            segno=""
        else:
            print("to convert to int",M[:-1,j])
            as_str="".join(M[:-1,j])
            
            ACCUMUL.append(int(as_str));

            if M[-1,j]=="+":
                segno="+";
            if M[-1,j]=="*":
                segno="*"
    print(f"the sum is {S}")
    