import pandas as pd

class Extractor:

# Initializes the Extractor class with a file path or a DataFrame
#Parameters:
#- file_path (str): Path of the file to be loaded (CSV, Excel, JSON).
#- df (pd.DataFrame): Optional DataFrame already loaded.

    def __init__(self,file_path = None, df=None):
        if file_path:
            self.df = self.load_data(file_path)
        elif file_path is not None:
            self.df = df
        else:
            raise ValueError ("You must provide a file path or a DataFrame.")
        
    def load_data(self, file_path):

# Loads data from a CSV, Excel or JSON file
# Parameters: - file_path (str): File path.
# Returns:- pd.DataFrame: Loaded DataFrame

        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
            return pd.read_excel(file_path)
        elif file_path.endswith(".json"):
            return pd.read_json(file_path)
        else:
            raise ValueError("Formato de arquivo não suportado. Use CSV, Excel ou JSON.")
    
    def filter_colmns(self, columns_to_keep=None):

# Filters specific columns of the DataFrame.
# Parameters: - columns_to_keep (list): List with the names of the desired columns.
# Returns:- pd.DataFrame: Filtered DataFrame.

        if columns_to_keep:
            self.df = self.df[columns_to_keep]
        return self.df
    
    def check_missing_values(self):
        
#  Displays the count of missing values ​​per column.
        
        missing_counts = self.df.isnull().sum()
        print("Valores ausentes por coluna:")
        print(missing_counts)
        return missing_counts

    def convert_dtypes(self, conversions=None):
         #Converts column data types.

#Parameters:- conversions (dict): Dictionary mapping columns to desired types.

#Returns:- pd.DataFrame: DataFrame with converted types.
        if conversions:
            self.df = self.df.astype(conversions)
        return self.df

    def extract_pipeline(self, columns_to_keep=None, conversions=None):
# Performs full extraction: filters columns and converts data types.

#Parameters: - columns_to_keep (list): List of desired columns.
# - conversions (dict): Dictionary of data type conversions.

#Returns:
        self.filter_columns(columns_to_keep)
        self.convert_dtypes(conversions)
        return self.df
