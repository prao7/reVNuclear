# Author: Pradyumna Rao, <pradyumna.rao@colorado.edu>
import zipfile
import pandas as pd
import os

# Define a function to list the contents of the zip file
def list_zip_contents(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return zip_ref.namelist()

# Define a function to unzip and extract a csv file into a DataFrame
def unzip_to_dataframe(zip_path, csv_filename, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract the specified CSV file from the zip file
        zip_ref.extract(csv_filename, extract_path)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(os.path.join(extract_path, csv_filename))
    return df

# Path to the uploaded zip file
zip_path = '/Users/pradyrao/VSCode/smrsupplycurve/input_data/itc_input_data/MSA_NMSA_EC_FFE_v2024_1.zip'
# Correct CSV filename inside the zip file
csv_filename_correct = 'MSA_NMSA_EC_FFE_v2024_1/MSA_NonMSA_EnergyCommunities_FossilFuelEmp_v2024_1.csv'

# List the contents of the zip file to verify the correct path
file_list = list_zip_contents(zip_path)
print("Contents of the zip file:", file_list)

# Define the extraction path (current working directory)
extract_path = '.'

# Check if the correct CSV file path exists in the zip
if csv_filename_correct in file_list:
    # Call the function and get the DataFrame with the correct path
    df_correct = unzip_to_dataframe(zip_path, csv_filename_correct, extract_path)
    # Display the first few rows of the DataFrame
    print(df_correct.head())
else:
    print(f"File '{csv_filename_correct}' not found in the zip archive.")
