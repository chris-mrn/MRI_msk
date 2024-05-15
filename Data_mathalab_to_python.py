import scipy.io
import numpy as np

# Load the .mat file
mat_data = scipy.io.loadmat('/Users/christophermarouani/Desktop/'
                            'MatricesFolder/matrices_data.mat')

# Extract matrices from the loaded data
matrix1 = mat_data['matrix1']
matrix2 = mat_data['matrix2']
matrix3 = mat_data['raw_matrix']

# Convert to NumPy arrays
numpy_matrix1 = np.array(matrix1)
numpy_matrix2 = np.array(matrix2)
numpy_matrix3 = np.array(matrix3)

# Now you have NumPy arrays
print("Matrix 1:")
print(numpy_matrix1)
print("Matrix 2:")
print(numpy_matrix2)
print("Matrix 3:")
print(numpy_matrix3)
