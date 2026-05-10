#--- Day 10: Factory ---
#Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.
#
#The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.
#
#For example:
#
#[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
#[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
#The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.
#
#To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.
#
#So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.
#
#You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).
#
#So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.
#
#Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.
#
#You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.
#
#There are a few ways to correctly configure the first machine:
#
#[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#You could press the first three buttons once each, a total of 3 button presses.
#You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
#You could press all of the buttons except (1,3) once each, a total of 5 button presses.
#However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.
#
#The second machine can be configured with as few as 3 button presses:
#
#[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
#One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.
#
#The third machine has a total of six indicator lights that need to be configured correctly:
#
#[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
#The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.
#
#So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.
#
#Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?
import numpy as np;
import heapq
# EXAMPLE PRIORITY QUEUE
##customers = []
##heapq.heappush(customers, (2, "Harry"))
##heapq.heappush(customers, (3, "Charles"))
##heapq.heappush(customers, (1, "Riya"))
##heapq.heappush(customers, (4, "Stacy"))
##while customers:
##     print(heapq.heappop(customers))

TOT=0;
Wanted_N=0;
with open("Day10_input1.txt") as f:
    for kk_machine,r in enumerate(f.readlines()):
        r=r.split(" ");
        # reading the wanted state
        Wanted_STATE_STR=r[0];
        Wanted_STATE_STR=Wanted_STATE_STR[1:-1].replace(".","0").replace("#","1")
        Wanted_N=int(Wanted_STATE_STR, base=2);
        N_BIT=len(Wanted_STATE_STR)
        print(f"N_BIT {N_BIT}; value wanted {Wanted_N}")
        # Filling adjacency matrix
        Vertices=[i for i in range(2**N_BIT)];
        A=np.zeros((2**N_BIT,2**N_BIT),dtype=np.bool_);
        for command in r[1:-1]:
            command=command[1:-1]
            for v in Vertices:
                str=list(format(v,f"0{N_BIT}b"));
                #print(str)
                for idx in command.split(","):
                    #if len(command)==1:
                    #    print(idx) # ok prende bene anche i comandi singoli
                    idx=int(idx);
                    str[idx]='1' if str[idx]=='0' else '0'
                str="".join(str)
                converted=int(str,base=2)
                A[v,converted]=1
                A[converted,v]=1
        #print("dtype(A)=",A.dtype, "N_BYTES ", A.nbytes)
        #JOLTAGE IS NOT USED IN PART 1    
        joltage_list=r[-1]

        #INIZIO CON DJIKSTRA
        Coda=[]
        SRC=0;
        min_dist_to_dest=np.inf;
        min_dist_to_node=np.inf*np.ones((2**N_BIT,));
        heapq.heappush(Coda,(0,SRC));
        while len(Coda)>0:
            actual_dist,nodo_actual=heapq.heappop(Coda)
            #print("nodo actual=",nodo_actual, "   wanted=",Wanted_N)
            #print("actual_dist=",actual_dist,"   nodo actual=",nodo_actual)
            if nodo_actual==Wanted_N:
                if actual_dist<min_dist_to_dest:
                    min_dist_to_dest=actual_dist;
                continue;
            if actual_dist>=min_dist_to_dest or actual_dist>min_dist_to_node[nodo_actual]:
                continue;
            locco=np.where(A[nodo_actual,:]!=0)[0]
            for nodo_dest in locco:
                #print("nodo dest in the for_loop",nodo_dest)
                somma=actual_dist+A[nodo_actual,nodo_dest]
                if somma<min_dist_to_node[nodo_dest]:
                    min_dist_to_node[nodo_dest]=somma;
                if somma<min_dist_to_dest:
                    heapq.heappush(Coda,(somma,nodo_dest))
        
        print(f"{kk_machine}------->    min dist from {format(0,f"0{N_BIT}b")} to  {format(Wanted_N,f"0{N_BIT}b")} is {min_dist_to_dest} ")
        TOT+=min_dist_to_dest;
    print(f"total sum = {TOT}");