# # Author: Pradyumna Rao, <pradyumna.rao@colorado.edu>
# MSA Source: https://edx.netl.doe.gov/resource/13454403-ef6b-479b-b720-d5e3eaefbb91/intended_use
# IRA Source: https://edx.netl.doe.gov/resource/28a8eb09-619e-49e5-8ae3-6ddd3969e845/intended_use
import zipfile
import pandas as pd
import os


# Define a function to list the contents of the zip file
def list_zip_contents(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return zip_ref.namelist()


# Define a function to read a CSV file from a zip archive into a DataFrame
def read_csv_from_zip(zip_path, csv_filename):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with zip_ref.open(csv_filename) as file:
            df = pd.read_csv(file)
    return df


# Defining a function to export the IRA Coal closures to a DataFrame
def get_ira_coal_closure():
    # This is the path to the zip file containing the IRA Coal closures
    zip_path = '/Users/pradyrao/VSCode/smrsupplycurve/input_data/itc_input_data/ira_coal_closure_energy_comm_2023v2.zip'
    
    # This is the correct CSV filename inside the zip file
    csv_filename_correct = 'IRA_Coal_Closure_Energy_Comm_2023v2/Coal_Closure_Energy_Communities_2023v2.csv'

    # List the contents of the zip file to verify the correct path
    file_list = list_zip_contents(zip_path)
    
    # Check if the correct CSV file path exists in the zip
    if csv_filename_correct in file_list:
        # Call the function and get the DataFrame with the correct path
        df_correct = read_csv_from_zip(zip_path, csv_filename_correct)
        # Display the first few rows of the DataFrame
        print(df_correct.head())
    else:
        print(f"File '{csv_filename_correct}' not found in the zip archive.")
    
    return df_correct


# Defining a function to export the MSA Non-MSA Energy Communities Fossil Fuel Employment to a DataFrame
def get_msa_nmsa_ec_ffe():
    # This is the path to the zip file containing the MSA Non-MSA Energy Communities Fossil Fuel Employment
    zip_path = '/Users/pradyrao/VSCode/smrsupplycurve/input_data/itc_input_data/MSA_NMSA_EC_FFE_v2024_1.zip'
    
    # This is the correct CSV filename inside the zip file
    csv_filename_correct = 'MSA_NMSA_EC_FFE_v2024_1/MSA_NonMSA_EnergyCommunities_FossilFuelEmp_v2024_1.csv'
    
    # List the contents of the zip file to verify the correct path
    file_list = list_zip_contents(zip_path)

    # Check if the correct CSV file path exists in the zip
    if csv_filename_correct in file_list:
        # Call the function and get the DataFrame with the correct path
        df_correct = read_csv_from_zip(zip_path, csv_filename_correct)
        # Display the first few rows of the DataFrame
        print(df_correct.head())
    else:
        print(f"File '{csv_filename_correct}' not found in the zip archive.")
    
    return df_correct