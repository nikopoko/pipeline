def read_text_file_to_2d_list(file_path):
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Strip the line to remove leading/trailing whitespace and split by spaces
            row = line.strip().split()
            # Append the row to the matrix
            matrix.append(row)
    return matrix


# Specify the path to your text file
file_path = 'input.txt'

# Read the text file and create the matrix
matrix = read_text_file_to_2d_list(file_path)

# Print the matrix
for row in matrix:
    print(row)
