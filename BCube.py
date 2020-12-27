#!/usr/bin/env python
# coding: utf-8

#ServerPorts 
k = int(input("enter number of server ports(better be less than 4) :"))
#SwitchPorts
n= int(input("enter number of switch ports(better be less than 10) :"))
#No_of_first_switch
NOFS=n**(k)
print(f'NOFS = {NOFS}')
RowSwitches=n**(k-1)
linked_list = []

for Level in range(k):
    hop = n**Level
    max_coverage = n**(Level+1)
    current_coverage = max_coverage
    count = 0
   # print(f'hop = {hop}')
    
    for switch in range(RowSwitches):
        if current_coverage == 0 :
            count+=1
            current_coverage = max_coverage
        else:
              pass
        currentSwitch = NOFS + Level*RowSwitches + switch
        
        for port in range(n):
            
            connected_host= int(switch%(max_coverage/n))+ port*hop+ count*max_coverage
            
     #       print(currentSwitch,connected_host)
            linked_list.append((currentSwitch,connected_host))
            
            current_coverage-=1
    #    print("Next Switch")
   # print("Next Level")  
#print(linked_list) 
total_nodes = NOFS+n**(k-1)*k
open('connections.txt','w+').close()
connections_file = open('connections.txt','w+')
for x in range(total_nodes):
    for y in range(total_nodes):
        if (x,y) in linked_list or x ==y or (y,x) in linked_list:
           # print(f'{x}   {y}  1')
            connections_file.write(f'{y}   {x}  1\n')
        else:
            #print(f'{x}   {y}   999999')
            connections_file.write(f'{y}   {x}  99999\n')
connections_file.close()

    
            
            
        


# In[ ]:




