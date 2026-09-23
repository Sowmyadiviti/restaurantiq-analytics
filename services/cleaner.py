from column_mapping import COLUMN_MAPPING
import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    # ---------------------------------------
    # Load Dataset
    # ---------------------------------------
    def load_dataset(self):
        self.df = pd.read_csv(self.file_path)
        self.df.rename(
            columns=COLUMN_MAPPING,
            inplace=True
        )
        print("=" * 60)
        print("DATASET LOADED SUCCESSFULLY")
        print("=" * 60)
        print(f"Rows    : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")

    # ---------------------------------------
    # Clean Dataset
    # ---------------------------------------
    def clean_dataset(self):
        print("\nCleaning Started...\n")
        df = self.df

        # Remove duplicates
        duplicates = self.df.duplicated().sum()
        self.df.drop_duplicates(inplace=True)
        print(f"Duplicates Removed : {duplicates}")

        # Replace missing values
        self.df.replace(["", " ", "NULL", "null", "None", np.nan], pd.NA, inplace=True)

        # Rating
        self.df["rate"] = (
            self.df["rate"]
            .astype(str)
            .str.replace("/5", "", regex=False)
            .replace("NEW", pd.NA)
            .replace("-", pd.NA)
        )
        self.df["rate"] = pd.to_numeric(self.df["rate"], errors="coerce")

        # Votes
        self.df["votes"] = pd.to_numeric(self.df["votes"], errors="coerce")

        # Cost
        self.df["approx_cost(for two people)"] = (
            self.df["approx_cost(for two people)"]
            .astype(str)
            .str.replace(",", "", regex=False)
        )
        self.df["approx_cost(for two people)"] = pd.to_numeric(
            self.df["approx_cost(for two people)"],
            errors="coerce",
        )

        # Fill missing text values
        text_columns = [
            "location",
            "rest_type",
            "cuisines",
            "reviews_list",
            "listed_in(type)",
            "listed_in(city)",
        ]
        for column in text_columns:
            self.df[column] = self.df[column].fillna("Not Available")
            self.df[column] = self.df[column].astype(str).str.strip()

        print("Dataset Cleaned Successfully")

        return self.df