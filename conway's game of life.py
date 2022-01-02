import random
import os
import time

x = 5
y = 5
clear = lambda: os.system('cls')

def main():
    world = []
    for i in range (0,x):
        row = []
        for j in range(0,y):
            row.append(random.randint(0,1))
        world.append(row)
    while(True):
        print_world(world,x,y)
        world = rules(world,x,y)
        time.sleep(0.2)
        
def print_world(world,x,y):
    clear()
    for i in range (0,x):
        for j in range(0,y):
            if(world[i][j] == 1):
                print("@", end =" ")
            else :
                print(" ", end =" ")
        print("")
    
def rules(world,x,y):
    alive = []
    for i in range (0,x):
        row = []
        for j in range(0,y):
            counter = 0
            if(i+1 < x and world[i+1][j] == 1):
                    counter = counter + 1
            if(i-1 >= 0 and world[i-1][j] == 1):
                counter = counter + 1
            if(j+1 < y and world[i][j+1] == 1):
                counter = counter + 1
            if(j-1 >= 0 and world[i][j-1] == 1):
                counter = counter + 1
            if(j-1 >= 0 and i-1 >= 0 and world[i-1][j-1] == 1):
                counter = counter + 1
            if(j+1 < y and i+1 < x and world[i+1][j+1] == 1):
                counter = counter + 1
            if(j-1 >= 0 and i+1 < x and world[i+1][j-1] == 1):
                counter = counter + 1
            if(j+1 < y and i-1 >= 0 and world[i-1][j+1] == 1):
                counter = counter + 1
            if(counter == 3):
                row.append(1)
            elif(counter == 2 and world[i][j] == 1):
                row.append(1)
            else :
                row.append(0)
        alive.append(row)
    return alive

main()
       
