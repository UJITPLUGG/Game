import tkinter as tk
from functools import partial
import random
import time

width = 10
height = 10
playground = [[0]*width for i in range(height)]
colors = ["#333333","#FF0000","#d3db37","#85c78c"] 
window = tk.Tk()
window.geometry("240x255")
window.resizable(True, True)

def change_field(playground,x,y,number):
    colors = ["#333333","#FF0000","#d3db37","#85c78c"]
    playground[x][y]["bg"] = colors[number]
    '''
    bonus number
    if not (playground[x][y]["bg"] == "#85c78c"):
        None
    elif playground[x][y]["text"] == "":
        playground[x][y]["text"] = str(1)
    else:
        playground[x][y]["text"] = str(int(playground[x][y]["text"])+1)
    '''

def move(way,playground,player_field,colors):
    x, y = player_field
    if way == "up":
        if (-1<(player_field[0]-1)<width) and not (playground[x-1][y]["bg"] == colors[1]):
            change_field(playground,x-1,y,3)
            change_field(playground,x,y,0)
    elif way == "left":
        if (-1<(player_field[1]-1)<width) and not (playground[x][y-1]["bg"] == colors[1]):
            change_field(playground,x,y-1,3)
            change_field(playground,x,y,0)
    elif way == "down":
        if (-1<(player_field[0]+1)<width) and not (playground[x+1][y]["bg"] == colors[1]):
            change_field(playground,x+1,y,3)
            change_field(playground,x,y,0)
    elif way == "right":
        if (-1<(player_field[1]+1)<width) and not (playground[x][y+1]["bg"] == colors[1]):
            change_field(playground,x,y+1,3)
            change_field(playground,x,y,0)
    if find_field(playground,colors,2) == None:
        for i in range(10):
            for j in range(10):
                change_field(playground,i,j,3)
                window.update()
                time.sleep(0.1)
                


def find_field(playground,colors,number):
    for x in range(10):
        for y in range(10):
            if playground[x][y]["bg"] == colors[number]:
                return [x,y]
    return None
def chance(chance_num):
    if random.randint(0,100) <=chance_num:
        return True
    return False


def pressed(event,playground):
    player_field = find_field(playground,colors,3)
    if event.char == "w":
        move("up",playground,player_field,colors)
    elif event.char == "a":
        move("left",playground,player_field,colors)
    elif event.char == "s":
        move("down",playground,player_field,colors)
    elif event.char == "d":
        move("right",playground,player_field,colors)


def main():
    for x in range(width):
        for y in range(height):
            if (x==0 and y==0):
                playground[x][y] = (tk.Label(window,bg=colors[3],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            if chance(60):
                playground[x][y]= (tk.Label(window,bg=colors[0],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            if chance(40):
                playground[x][y]= (tk.Label(window,bg=colors[1],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue
            else:
                playground[x][y]= (tk.Label(window,bg=colors[2],width=6,height=3))
                playground[x][y].grid(row=x,column=y)
                continue


    window.bind('<KeyPress>', partial(pressed,playground=playground))

    window.mainloop()

if __name__ == "__main__":
    main()

