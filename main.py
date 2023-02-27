import numpy as np
from itertools import zip_longest

board=np.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,2,0,0,0,0],
    [0,0,0,0,2,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ])

def list2board(at:list):
    return board[at[0]][at[1]]

def set(which:int,where:list):
    if not where in [i[0] for i in get_settable(which)]:
        return False
    place=[i for i in get_settable(which) if i[0]==where][0][1]
    print(where[0],place[0],where[1],place[1])
    abs(place[0]-where[0])
    step_x=1 if place[0]-where[0]>0 else -1 if place[0]-where[0]<0 else 0
    step_y=1 if place[1]-where[1]>0 else -1 if place[1]-where[1]<0 else 0
    repx=range(where[0],place[0]+1,step_x) if step_x else [where[0]]*(abs(place[1]-where[1])+1)
    repy=range(where[1],place[1]+1,step_y) if step_y else [where[1]]*(abs(place[0]-where[0])+1)
    print(repx,repy)
    for i,j in zip(repx,repy):
        board[i][j]=which
    print(board)

def get_sequence(which:int,at:list):
    opponent=3-which
    sequence=[]
    place=[]
    for i in at:
        if list2board(i)==opponent:
            sequence.append(list2board(i))
            place.append(i)
        else:
            sequence.append(list2board(i)) if list2board(i)!=0 else ...
            place.append(i)
            break
    return [sequence,place]

def get_settable(which:int):
    opponent=3-which
    settable=[]
    for i in range(1,9):
        for j in range(1,9):
            cross=[i for i in get_cross([i,j]) if i]
            for k in cross:
                around=get_sequence(which,k)
                if around[0] and around[0][0]==opponent and around[0][-1]==which:
                    settable.append([[i,j],around[1][-1]])
    return settable
                

def get_around(where:list):
    return [i[0] for i in get_cross(where) if i]

def get_cross(where:list):
    cross_around_up_left=[]
    cross_around_up_right=[]
    vertical=[]
    horizontal=[]
    if where[0]>where[1]:
        for i,j in zip(range(1+(where[0]-where[1]),9),range(1,9)):
            cross_around_up_left.append([i,j])
    elif where[0]<where[1]:
        for i,j in zip(range(1,9),range(1+(where[1]-where[0]),9)):
            cross_around_up_left.append([i,j])
    else:
        for i in range(1,9):
            cross_around_up_left.append([i,i])

    if sum(where)<=8:
        for i,j in zip(range(1,sum(where)),range(sum(where)-1,0,-1)):
            cross_around_up_right.append([i,j])
    elif sum(where)>8:
        for i,j in zip(range(sum(where)-8,9),range(8,sum(where)-9,-1)):
            cross_around_up_right.append([i,j])

    for i in range(1,9):
        vertical.append([i,where[1]])
        horizontal.append([where[0],i])

    v_index=vertical.index(where)
    h_index=horizontal.index(where)
    up_left_index=cross_around_up_left.index(where)
    up_right_index=cross_around_up_right.index(where)

    return [
            list(reversed(vertical[:v_index])),
            list(reversed(cross_around_up_right[:up_right_index])),
            horizontal[h_index+1:],
            cross_around_up_left[up_left_index+1:],
            vertical[v_index+1:],
            cross_around_up_right[up_right_index+1:],
            list(reversed(horizontal[:h_index])),
            list(reversed(cross_around_up_left[:up_left_index])),
            ]

set(2,[3,4])
    