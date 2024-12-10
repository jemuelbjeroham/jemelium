import csv

def append_to_csv(file_path, inc, case):
    # Open the file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append the data
        writer.writerow([inc, case])

# File path to your .csv file
file_path = "inc_case_data.csv"

# Input the INC and CASE values
inc = input("Enter the INC value: ")
case = input("Enter the CASE value: ")

# Append the data to the CSV file
append_to_csv(file_path, inc, case)

print(f"Data appended: {inc}, {case}")
