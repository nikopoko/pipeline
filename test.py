# Define the function to read the file and process the input
def read_input_file(file_path):
    items = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into parts
            parts = line.strip().split()
            if len(parts) == 3:
                item = {
                    'item': parts[0],
                    'x': int(parts[1]),
                    'y': int(parts[2])
                }
                items.append(item)
    
    return items

# Define the function to create the 2D array based on the items
def create_2d_array(items):
    # Determine the size of the array
    max_x = max(item['x'] for item in items) + 1
    max_y = max(item['y'] for item in items) + 1
    
    # Initialize the 2D array with 0
    array = [[0 for _ in range(max_x)] for _ in range(max_y)]
    
    # Populate the 2D array with the items
    for item in items:
        array[item['y']][item['x']] = item['item']
    
    # Reverse the rows to reverse the y-axis
    array.reverse()
    
    return array, max_y

# Define the function to add a border to the 2D array
def add_border(array):
    # Get the dimensions of the array
    num_rows = len(array)
    num_cols = len(array[0])
    
    # Add a border of 0s around the array
    # Add top and bottom border
    bordered_array = [[0] * (num_cols + 2)]
    for row in array:
        bordered_array.append([0] + row + [0])
    bordered_array.append([0] * (num_cols + 2))
    
    return bordered_array

# Define the function to replace pipes with their hole representation
def replace_pipes_with_holes(array):
    # Define the mapping from pipe characters to hole arrays
    pipe_mapping = {
        '═': [0, 0, 1, 1],
        '║': [1, 1, 0, 0],
        '╔': [0, 1, 1, 0],
        '╗': [0, 1, 0, 1],
        '╚': [1, 0, 1, 0],
        '╝': [1, 0, 0, 1],
        '╠': [1, 1, 1, 0],
        '╣': [1, 1, 0, 1],
        '╦': [0, 1, 1, 1],
        '╩': [1, 0, 1, 1],
        '*': [1, 1, 1, 1]
    }
    
    # Replace each pipe character in the array
    replaced_array = []
    for row in array:
        replaced_row = []
        for cell in row:
            if cell in pipe_mapping:
                replaced_row.append(pipe_mapping[cell])
            else:
                replaced_row.append([0, 0, 0, 0])
        replaced_array.append(replaced_row)
    
    return replaced_array

# Define the function to create a new array with name, coordinates, and letter
def create_letter_array(items, max_y):
    letter_array = []

    for item in items:
        if item['item'].isalpha():
            letter_array.append({
                'name': item['item'],
                'x': item['x'] + 1,  # Adjust for border
                'y': max_y - item['y']  # Adjust for border
            })
        elif item['item']=='*':
            star = {'name': item['item'],
                    'x': item['x'] +1,
                    'y': max_y-item['y']}
    return star,letter_array
def start(y,x):
    ans = 0
    if final_array[y+1][x][1]==1:
        ans += requrs(y+1,x)
    if final_array[y-1][x][0]==1:
        ans += requrs(y-1,x)
    if final_array[y][x+1][3]==1:
        ans += requrs(y,x+1)
    if final_array[y][x-1][2]==1:
        ans += requrs(y,x-1)
    return ans
def requrs(y,x):
    if final_array[y][x]==0:
        return 0
    if final_array[y][x]==[1,1,1,1]:
        return 1
    ans = 0
    up=final_array[y][x][0]
    down=final_array[y][x][1]
    right=final_array[y][x][2]
    left=final_array[y][x][3]
    next_up = final_array[y+1][x][1]==1
    next_down = final_array[y-1][x][0]==1
    next_right = final_array[y][x][3]==1
    next_left = final_array[y][x][2]==1
    if up and next_up:
        ans += requrs(y+1,x)
    if down and next_down:
        ans += requrs(y-1,x)
    if right and next_right:
        ans += requrs(y,x+1)
    if left and next_left:
        ans += requrs(y,x-1)
    if ans > 0:
        final_array[y][x]=[1,1,1,1]
    return ans


# Define the file path
file_path = 'test.txt'

# Read and process the input file
items = read_input_file(file_path)

# Create the 2D array
array, max_y = create_2d_array(items)

# Add a border to the 2D array
bordered_array = add_border(array)

# Replace pipes with their hole representation
final_array = replace_pipes_with_holes(bordered_array)

# Create the array with name, coordinates, and letter
stars,letter_array = create_letter_array(items, max_y)

# Print the final array
print("Final Array with Holes:")
for row in final_array:
    print(row)
# Print the array with name, coordinates, and letter
print("\nArray with Names, Coordinates, and Letters:")
print(start(3,2))
for item in letter_array:
    print(item)