#import numpy
import numpy as np

# 2. Open the CSV file using open()
file = open('loan_data.csv', 'r')

# 3. Load data with numpy.genfromtxt
data = np.genfromtxt(
    file,
    delimiter=',',           # Comma-separated values
    skip_header=1,           # Skip the header row
    usecols=(8),             # LoanAmount column (0-based index 8)
    dtype=float,
    missing_values='',       # Handle empty/missing values
    filling_values=0.0
)

# Close the file after reading (important for resource management)
file.close()

# Perform statistical analysis
mean_loan = np.mean(data)
median_loan = np.median(data)
std_loan = np.std(data)

# Display results
print("=== Loan Amount Statistical Analysis ===")
print(f"Mean Loan Amount     : ${mean_loan:,.2f}")
print(f"Median Loan Amount   : ${median_loan:,.2f}")
print(f"Standard Deviation   : ${std_loan:,.2f}")
print(f"Total Records Analyzed: {len(data)}")
