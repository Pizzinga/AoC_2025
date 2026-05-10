#--- Part Two ---
#The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
#
#So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.
#
#Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:
#
#3-5
#10-14
#16-20
#12-18
#The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
#
#Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

from sortedcontainers import SortedList
start_range=SortedList();
end_range=list();
S=0;
with open('Day5_input1.txt') as f:
    for l in f.readlines():
        if l=="\n":
            break;
        
        l.replace("\n","")
        s=l.split("-")
        e=int(s[1]);s=int(s[0]);
        i=start_range.bisect(s)
        start_range.add(s);
        end_range.insert(i,e);
    ranges=[(ss,ee)for ss,ee in zip(start_range,end_range)]
    #print("current Ranges(s,e):",ranges );
    max_actual=0;
    S=0;
    for s,e in ranges:
        if max_actual>s:
            s=max_actual;
        if max_actual>e:
            continue;
        S+=(e-s)+1
        max_actual=e+1

    print(f"there are {S} fresh ingredients")