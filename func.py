def test_start(y,x):
    ans = 0
    print(final_array[y-1][x][1]==1)
    if final_array[y-1][x][1]==1:
        result = test_requrs(y-1,x)
        if result == 0:
            final_array[y-1][x]=0
        else:
            final_array[y-1][x]=[1,1,1,1]
            final_array[y][x]=[1,1,1,1]
            return 1
    
    return 0
def test_requrs(y,x):
    if final_array[y][x]==0:
        return 0
    if final_array[y][x]==[1,1,1,1]:
        return 1
    up=final_array[y][x][0]
    next_up = final_array[y-1][x][1]
    left=final_array[y][x][3]
    next_left = final_array[y][x][2]
    print(final_array[y][x])
    if up and next_up:
        result = test_requrs(y-1,x)
        if result==0:
            final_array[y][x]=0
            final_array[y-1][x][0]=0
        else:
            final_array[y-1][x]=[1,1,1,1]
            final_array[y][x]=[1,1,1,1]
            return 1
    if left and next_left:
        result=test_requrs(y,x-1)
        if result==0:
            final_array[y][x-1]=0
            final_array[y][x][3]=0
        else:
            final_array[y][x-1]=[1,1,1,1]
            final_array[y][x]=[1,1,1,1]
            return 1