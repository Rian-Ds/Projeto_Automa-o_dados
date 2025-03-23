import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder # type: ignore

# Creating the data transformation class

class Transform:

# Initialize the class with a DataFrame and set up a dictionary to store label encoders
    def __init__(self, df):
        self.df = df
        self.label.endecoders = {} # Dictionary to store encoders LabelEncoder
        self.scaler = StandardScaler()  # StandardScaler instance for data normalization


# Method for cleaning data: can fill null values ​​with a specific value or remove them
# in addition to removing duplicates from the DataFrame
    def clean_data (self, fill_na=False, fill_value=0):

    # Removes null values ​​or fills with a default value, and removes duplicates. #
        if fill_na:
            self.df.fillna(fill_value, inplace=True) # Fill null values ​​with a given value
        else:
            self.df.dropna(fill_na, inplace=True) # Remove null values ​​from the DataFrame
            self.df.drop_duplicates(inplace=True) # # Remove duplicates
        return self.df

# Method for normalizing column names: converts to lowercase,
# removes extra spaces and replaces special characters with underscores.
    def normalize_coluns(self):

# Standardizes column names (lowercase, no spaces or special characters)
        self.df.columns (
            self.df.columns.str.lower() # Convert names to lowercase
            .str.strip() # Remove extra whitespace
            .str.replace(r"[^a-zA-Z0-9_]", "_", regex=True)  # Replace special characters with "_"

        )
        return self.df

# Method to convert column data types to appropriate types (numeric or date).
def convert_data_types(self):
    for col in self.df.coluns:
        try:
            self.df[col] = pd.to_numeric(self.df[col]) # Try to convert to numeric
        except ValueError:
            try:
                self.df[col] = pd.to_datatime(self.df[col]) # If it fails, try converting to date    
            except ValueError:
                pass # Keep original type if cannot be converted
    return self.df


# Method to remove outliers from numeric columns based on the interquartile range (IQR) rule.
def remove_outliers(self, columns=None):

    # Remove outliers using the IQR (Interquartile Range) rule.
    if columns is None:
        columns = self.df.select_dtypes(include=["number"]).columns # selecting numeric columns
    for col in columns:
        Q1 = np.quantile(self.df[col], 0.25)
        Q3 = np.quantile(self.df[col], 0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
    return self.df


def encode_categorical (self, method=False):
# Encode categorical columns using Label Encoding or One-Hot Encoding.

    categorical_cols = self.df.select_type(include=['object']).columns
    if method == "label":
        for col in categorical_cols:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le
    elif method == "onehot":
            self.df = pd.get_dummies(self.df, columns=categorical_cols)
    return self.df

    def scale_numeric_data(self):
        # Scale numeric columns to a standardized range.
        numeric_cols = self.df.select_dtypes(include=["number"]).columns
        self.df[numeric_cols] = self.scaler.fit_transform(self.df[numeric_cols])
        return self.df

    def transform_pipeline(self, fill_na=False, fill_value=0, outlier_cols=None, encoding="label"):
        # Applies all transformations sequentially.
        self.clean_data(fill_na, fill_value)
        self.normalize_columns()
        self.convert_data_types()
        self.remove_outliers(outlier_cols)
        self.encode_categorical(encoding)
        self.scale_numeric_data()
        return self.df
