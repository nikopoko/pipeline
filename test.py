# Constants for direction indices
UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

# Mapping of pipe characters to their hole arrays
PIPE_MAPPING = {
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

# Opposite direction indices for easy checking
OPPOSITE_DIRECTIONS = {
    'up': 'down',
    'down': 'up',
    'left': 'right',
    'right': 'left'
}

def read_input_file(file_path):
    """Read and process the input file to extract items."""
    items = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                items.append({
                    'item': parts[0],
                    'x': int(parts[1]),
                    'y': int(parts[2])
                })
    return items

def create_2d_array(items):
    """Create a 2D array based on the items."""
    max_x = max(item['x'] for item in items) + 1
    max_y = max(item['y'] for item in items) + 1
    
    array = [[0 for _ in range(max_x)] for _ in range(max_y)]
    
    for item in items:
        array[item['y']][item['x']] = item['item']
    
    array.reverse()
    
    return array, max_y

def add_border(array):
    """Add a border of zeros around the 2D array."""
    num_rows = len(array)
    num_cols = len(array[0])
    
    bordered_array = [[0] * (num_cols + 2)]
    for row in array:
        bordered_array.append([0] + row + [0])
    bordered_array.append([0] * (num_cols + 2))
    
    return bordered_array

def replace_pipes_with_holes(array):
    """Replace pipe characters with their corresponding hole representations."""
    replaced_array = []
    for row in array:
        replaced_row = []
        for cell in row:
            replaced_row.append(PIPE_MAPPING.get(cell, [0, 0, 0, 0]))
        replaced_array.append(replaced_row)
    return replaced_array

def create_letter_array(items, max_y):
    """Create an array with item names, coordinates, and letters."""
    letter_array = []
    star = None

    for item in items:
        if item['item'].isalpha():
            letter_array.append({
                'name': item['item'],
                'x': item['x'] + 1,  # Adjust for border
                'y': max_y - item['y']  # Adjust for border
            })
        elif item['item'] == '*':
            star = {
                'name': item['item'],
                'x': item['x'] + 1,
                'y': max_y - item['y']
            }

    return star, letter_array

def is_within_bounds(y, x):
    """Check if the coordinates are within the bounds of the final_array."""
    return 0 <= y < len(final_array) and 0 <= x < len(final_array[0])

def start(y, x):
    """Start the recursion process from the given coordinates."""
    directions = [
        (y - 1, x, 'down', UP),
        (y + 1, x, 'up', DOWN),
        (y, x + 1, 'left', RIGHT),
        (y, x - 1, 'right', LEFT)
    ]

    for new_y, new_x, direction, check_idx in directions:
        if is_within_bounds(new_y, new_x) and final_array[new_y][new_x][check_idx] == 1:
            result = recurse(new_y, new_x, direction)
            if result != 0:
                return 1

    return 0

def recurse(y, x, direction):
    """Recursive function to explore paths."""
    if final_array[y][x] == 0:
        return 0
    if final_array[y][x] == [1, 1, 1, 1]:
        return 1

    up, down, right, left = final_array[y][x]

    directions = {
        'up': (y - 1, x, 'down', UP, down),
        'down': (y + 1, x, 'up', DOWN, up),
        'left': (y, x - 1, 'right', LEFT, right),
        'right': (y, x + 1, 'left', RIGHT, left)
    }

    for new_direction, (new_y, new_x, opp_direction, check_idx, can_move) in directions.items():
        if can_move and is_within_bounds(new_y, new_x) and final_array[new_y][new_x][OPPOSITE_DIRECTIONS[new_direction]] == 1 and direction != new_direction:
            result = recurse(new_y, new_x, new_direction)
            if result != 0:
                return 1

    return 0

# Define the file path
file_path = 'input.txt'

# Read and process the input file
items = read_input_file(file_path)

# Create the 2D array
array, max_y = create_2d_array(items)

# Add a border to the 2D array
bordered_array = add_border(array)

# Replace pipes with their hole representation
final_array = replace_pipes_with_holes(bordered_array)

# Create the array with name, coordinates, and letter
stars, letter_array = create_letter_array(items, max_y)

# Print the final array
print("Final Array with Holes:")
for row in final_array:
    print(row)

# Print the array with name, coordinates, and letters
print("\nArray with Names, Coordinates, and Letters:")
print(stars)
for item in letter_array:
    print(item)
    print(start(item['y'], item['x']))
