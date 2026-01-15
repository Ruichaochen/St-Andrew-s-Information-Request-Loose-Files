cipher_text = ("")

# Number of columns and rows in a grid
num_columns = 30  # Trying with a 30-column grid as a common factor of 1800 characters
num_rows = len(cipher_text) // num_columns

# Initialize a matrix to store the rows
matrix = ['' for _ in range(num_rows)]

# Fill in the matrix row by row from the cipher text
for i in range(num_rows):
    matrix[i] = cipher_text[i * num_columns:(i + 1) * num_columns]

# Now to read the grid by columns, assemble the plaintext by reading down each column in order
decrypted_text_by_columns = ''.join(matrix[row][col] for col in range(num_columns) for row in range(num_rows))
decrypted_text_by_columns[:500]  # Display the first 500 characters to see if it forms readable text
print(decrypted_text_by_columns)
