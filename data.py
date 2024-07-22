#### Author: Pradyumna Rao, <pradyumna.rao@colorado.edu>
# MSA Source: https://edx.netl.doe.gov/resource/13454403-ef6b-479b-b720-d5e3eaefbb91/intended_use
# IRA Source: https://edx.netl.doe.gov/resource/28a8eb09-619e-49e5-8ae3-6ddd3969e845/intended_use
import zipfile
import pandas as pd
import os


def list_zip_contents(zip_path):
    """
    This function lists the contents of a zip archive.

    Parameters:
    zip_path (str): The file path to the zip archive.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        return zip_ref.namelist()


def read_csv_from_zip(zip_path, csv_filename):
    """
    This function reads a CSV file from a zip archive and returns a DataFrame.
    
    Parameters:
    zip_path (str): The file path to the zip archive.
    csv_filename (str): The name of the CSV file inside the zip archive.
    
    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with zip_ref.open(csv_filename) as file:
            df = pd.read_csv(file)
    return df


def csv_to_dataframe(csv_filepath):
    """
    This function reads a CSV file from the given file path and returns a DataFrame.
    
    Parameters:
    csv_filepath (str): The file path to the CSV file.
    
    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(csv_filepath)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_ira_coal_closure():
    """
    This function reads the IRA Coal closures data from the zip file and returns a DataFrame.

    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    # This is the path to the zip file containing the IRA Coal closures
    zip_path = 'input_data/itc_input_data/ira_coal_closure_energy_comm_2023v2.zip'
    
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


def get_msa_nmsa_ec_ffe():
    """
    This function reads the MSA Non-MSA Energy Communities Fossil Fuel Employment data from the zip file and returns a DataFrame.
    
    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    # This is the path to the zip file containing the MSA Non-MSA Energy Communities Fossil Fuel Employment
    zip_path = 'input_data/itc_input_data/MSA_NMSA_EC_FFE_v2024_1.zip'
    
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


def get_eia_coal_operable_units():
    """
    This function reads the EIA Coal Operable Units data from the inputs folder and returns a DataFrame.

    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    
    # Return the DataFrame
    return csv_to_dataframe('input_data/eia_860_coal_data/eia860_2022_coal_operable_units.csv')


def get_eia_coal_retired_units():
    """
    This function reads the EIA Coal Retired Units data from the inputs folder and returns a DataFrame.

    Returns:
    DataFrame: The DataFrame containing the data from the CSV file.
    """
    
    # Return the DataFrame
    return csv_to_dataframe('input_data/eia_860_coal_data/eia860_2022_coal_retired_units.csv')