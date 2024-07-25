class pair:
    x= None
    y= None
def read_text_file_to_2d_list(file_path):
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Strip the line to remove leading/trailing whitespace and split by spaces
            row = line.strip().split()
            # Append the row to the matrix
            matrix.append(row)
    return matrix
def output():
    for i in range(max_y):  
        print(massive[i])
file_path = 'test2.txt'

def treatment(inp): # [0] means up, [1] means down, [2] means right, [3] means left
    if inp == '═':
        return[0,0,1,1]
    if inp =='║':
        return[1,1,0,0]
    if inp =='╔':
        return[0,1,1,0]
    if inp =='╗':
        return[0,1,0,1]
    if inp =='╚':
        return[1,0,1,0]
    if inp =='╝':
        return[1,0,1,0]
    if inp =='╠':
        return[1,1,1,0]
    if inp == '╣':
        return[1,1,0,1]
    if inp =='╦':
        return[0,1,1,1]
    if inp == '╩':
        return[1,0,1,1]
    return inp
def origin(inp,x,y):
    
    if inp == '*':
        source = pair()
        source.x=x
        source.y=y
        return 0
    if (inp!='0'):
        sinks.append([inp,y,x])


# Read the text file and create the matrix
matrix = read_text_file_to_2d_list(file_path)
massive = []
sinks = []

max_x=1
max_y=1
for row in matrix:
    if (int(row[1])>max_x):
        max_x=int(row[1])
    if (int(row[2])>max_y):
        max_y=int(row[2])
max_x+=1
max_y+=1
#print(max_y)
#print(max_x)
map=[]
for i in range(max_y+2):
    new_massive = []
    for j in range(max_x+2):
        new_massive.append('0')
    massive.append(new_massive)
    map.append(new_massive)

for i in matrix:
    x = int(i[1])+1
    y = max_y+1 - int(i[2])-1 
    item = treatment(i[0])
    if item == i[0]:
        origin(i[0],i[1],i[2])
    massive[y][x] = item

def reqursion(y,x):


    pipe = massive[y][x]
    print("look here",pipe,y,x)
    if (pipe is (str or chr) and pipe=='*') or pipe==1:
        return 1
        
    if pipe=='0':
        return 0
    ans = 0
    print([pipe,str(max_y-y),str(x-1)])
    if [pipe,str(max_y-y),str(x-1)] in sinks:
        if(massive[y+1][x]==1) or (massive[y-1][x]==1) or (massive[y][x+1]==1) or (massive[y][x-1]==1):
            return 1
        if (type(massive[y+1][x]) is list and massive[y+1][x][0]!=0) or massive[y+1][x]=='*':
            ans += reqursion(y+1,x)
        if (type(massive[y-1][x]) is list and massive[y-1][x][1]!=0) or massive[y-1][x]=='*':
            ans +=reqursion(y-1,x)
        if (type(massive[y][x+1]) is list and massive[y][x+1][2]!=0) or massive[y][x+1]=='*':
            ans +=reqursion(y,x+1)
        if (type(massive[y][x-1]) is list and massive[y][x-1][3]!=0) or massive[y][x-1]=='*':
            ans +=reqursion(y,x-1)
        print("this function works")
        return ans
    else:
        up = pipe[0]
        down = pipe[1]
        right = pipe[2]
        left = pipe[3]
    if(up and massive[y+1][x]==1) or (down and massive[y-1][x]==1) or (right and massive[y][x+1]==1) or (left and massive[y][x-1]==1):
        massive[y][x]=1
        return 1
 

    if up and massive[y+1][x][0]!=0:
        ans += reqursion(y+1,x)
    if down and (type(massive[y-1][x]) is list and massive[y-1][x][1]!=0) :
        ans +=reqursion(y-1,x)
    if right and (type(massive[y][x+1]) is list and massive[y][x+1][2]!=0):
        ans +=reqursion(y,x+1)
    if left and (type(massive[y][x-1]) is list and massive[y][x-1][3]!=0):
        ans +=reqursion(y,x-1)
    if ans>0:
        massive[y][x]=1
    return ans

for i in massive:
    print(i)
for i in sinks:
    print(i)
print(reqursion(1,1))
#print(reqursion(3,2))


