import csv

def extract_inc_case(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check if the row is not empty
                inc, case = row
                yield inc, case  # Yield the INC and CASE pair one by one

# File path to your .csv file
file_path = "inc_case_data.csv"

# Example usage: looping through the extracted pairs
for inc, case in extract_inc_case(file_path):
    print(f"INC: {inc}, CASE: {case}")
