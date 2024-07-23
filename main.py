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

# Specify the path to your text file
file_path = 'input.txt'

# Read the text file and create the matrix
matrix = read_text_file_to_2d_list(file_path)
massive = []
max_x=1
max_y=1
for row in matrix:
    if (int(row[1])>max_x):
        max_x=int(row[1])
    if (int(row[2])>max_y):
        max_y=int(row[2])
print(max_y)
print(max_x)
for i in range(max_y):
    new_massive = []
    for j in range(max_x):
        new_massive.append('0')
    massive.append(new_massive)

for i in matrix:
    x = int(i[1])-1
    y = int(i[2])-1
    massive[y][x] = i[0]
output()
print(massive[16][33])