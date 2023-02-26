import numpy as np
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

def set(which:int,where:list):
    board[where[0]][where[1]]=which

def get_settable(which:int):
    ...
    for i in range(1,9):
        for j in range(1,9):
            around=get_around([i,j])
            cross=get_cross([i,j])

def get_around(where:list):
    around=[]
    around_place=[
        [where[0]-1,where[1]-1],
        [where[0]-1,where[1]],
        [where[0]-1,where[1]+1],
        [where[0],where[1]-1],
        [where[0],where[1]+1],
        [where[0]+1,where[1]-1],
        [where[0]+1,where[1]],
        [where[0]+1,where[1]+1]
        ]
    print(around_place)
    for i in around_place:
        if any([i[0]<1,i[0]>8,i[1]<1,i[1]>8]):
            pass
        else:
            around.append(board[i[0]][i[1]])
    return around

def get_cross(where:list):
    cross_around_up_left=[]
    cross_around_up_right=[]
    vertical=[]
    horizontal=[]
    if where[0]>where[1]:
        for i,j in zip(range(1+(where[0]-where[1]),10-(where[0]-where[1])),range(1,9)):
            cross_around_up_left.append([i,j])
    elif where[0]<where[1]:
        for i,j in zip(range(1,9),range(1+(where[1]-where[0]),10-(where[1]-where[0]))):
            cross_around_up_left.append([i,j])
    else:
        for i in range(1,9):
            cross_around_up_left.append([i,i])
    
    for i,j in zip(range(1,sum(where)),range(sum(where)-1,0,-1)):
        cross_around_up_right.append([i,j])

    for i in range(1,9):
        vertical.append([i,where[1]])
        horizontal.append([where[0],i])

    v_index=vertical.index(where)
    h_index=horizontal.index(where)
    up_left_index=cross_around_up_left.index(where)
    up_right_index=cross_around_up_right.index(where)

    return [
            vertical[:v_index],
            reversed(cross_around_up_right[:up_right_index]),
            horizontal[h_index+1:],
            cross_around_up_left[up_left_index+1:],
            vertical[v_index+1:],
            cross_around_up_right[up_right_index+1:],
            reversed(horizontal[:h_index]),
            reversed(cross_around_up_left[:up_left_index]),
            ]

print(get_cross([4,4]))
    