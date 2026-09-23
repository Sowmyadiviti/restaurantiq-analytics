import pandas as pd
import numpy as np

class RestaurantAnalyzer:
    def __init__(self, df):
        self.df = df

    # ------------------------------------------
    # Dataset Summary
    # ------------------------------------------
    def dataset_summary(self):
        print("="*60)
        print("DATASET SUMMARY")
        print("="*60)
        print(f"Rows : {self.df.shape[0]}")
        print(f"Columns : {self.df.shape[1]}")
        print("\nColumns")
        for column in self.df.columns:
            print(column)

    # ------------------------------------------
    # Missing Values
    # ------------------------------------------
    def missing_values(self):
        print("\nMissing Values")
        print(self.df.isnull().sum())

    # ------------------------------------------
    # Statistics
    # ------------------------------------------
    def statistics(self):
        print("\nStatistics")
        print(f"Average Rating : {self.df['rate'].mean():.2f}")
        print(f"Maximum Rating : {self.df['rate'].max()}")
        print(f"Minimum Rating : {self.df['rate'].min()}")
        print(f"Average Votes : {self.df['votes'].mean():.2f}")
        print(f"Maximum Votes : {self.df['votes'].max()}")
        print(f"Minimum Votes : {self.df['votes'].min()}")
        print(f"Average Cost : {self.df['approx_cost(for two people)'].mean():.2f}")
        
    # ------------------------------------------
    # Top Rated Restaurants
    # ------------------------------------------
    def top_restaurants(self):
        print("\nTop Rated Restaurants")
        top = self.df.sort_values(
            by="rate",
            ascending=False
        )
        print(
            top[
                [
                    "name",
                    "location",
                    "rate",
                    "votes"
                ]
            ].head(10)
        )

    # ------------------------------------------
    # Top Locations
    # ------------------------------------------
    def top_locations(self):
        print("\nTop Locations")
        location = (
            self.df
            .groupby("location")
            .agg(
                Restaurants=("name","count"),
                Average_Rating=("rate","mean"),
                Average_Votes=("votes","mean")
            )
            .sort_values(
                by="Restaurants",
                ascending=False
            )
        )
        print(location.head(10))
        
    # ------------------------------------------
    # Cuisine Analysis
    # ------------------------------------------
    def cuisine_analysis(self):
        print("\nCuisine Analysis")
        cuisine = (
            self.df
            .groupby("cuisines")
            .agg(
                Restaurants=("name","count"),
                Average_Rating=("rate","mean"),
                Average_Votes=("votes","mean"),
                Average_Cost=("approx_cost(for two people)","mean")
            )
            .sort_values(
                by="Restaurants",
                ascending=False
            )
        )
        print(cuisine.head(15))        
        
    # ------------------------------------------
    # Competition Analysis
    # ------------------------------------------
    def competition_analysis(self):
        print("\nCompetition Analysis")
        competition = (
            self.df
            .groupby(
                ["location", "cuisines"]
            )
            .size()
            .reset_index(name="competition")
        )
        print(
            competition
            .sort_values(
                by="competition",
                ascending=False
            )
            .head(20)
        )
        return competition
    
    # ------------------------------------------
    # Merge Competition
    # ------------------------------------------
    def merge_competition(self):
        competition = self.competition_analysis()
        self.df = self.df.merge(
            competition,
            on=["location", "cuisines"],
            how="left"
        )
        print("\nCompetition Merged Successfully")
        return self.df
    
    # ------------------------------------------
    # High Demand Cuisines
    # ------------------------------------------
    def high_demand_cuisines(self):
        print("\nHigh Demand Cuisines")
        result = (
            self.df
            .groupby("cuisines")
            .agg(
                Average_Rating=("rate", "mean"),
                Average_Votes=("votes", "mean"),
                Restaurants=("name", "count")
            )
        )
        result = result[
            (result["Average_Rating"] >= 4)
            &
            (result["Average_Votes"] >= 500)
        ]
        print(result.sort_values(
            by="Average_Rating",
            ascending=False
        ))
        return result
    
    # ------------------------------------------
    # Low Competition Cuisines
    # ------------------------------------------
    def low_competition(self):
        print("\nLow Competition")
        result = (
            self.df
            .groupby("cuisines")
            .agg(
                Competition=("name", "count"),
                Average_Rating=("rate", "mean")
            )
        )
        result = result[
            result["Competition"] <= 20
        ]
        print(result)
        return result
    
    # ------------------------------------------
    # Investment Opportunities
    # ------------------------------------------
    def investment_opportunities(self):
        print("\nInvestment Opportunities")
        result = (
            self.df
            .groupby(
                ["location", "cuisines"]
            )
            .agg(
                Rating=("rate", "mean"),
                Votes=("votes", "mean"),
                Competition=("name", "count")
            )
        )
        result = result[
            (result["Rating"] >= 4)
            &
            (result["Competition"] <= 20)
        ]
        print(
            result.sort_values(
                by="Rating",
                ascending=False
            )
            .head(20)
        )
        return result
    
    # ------------------------------------------
    # Recommendation
    # ------------------------------------------
    def recommendation(self):
        print("\nRecommended Investment")
        result = self.investment_opportunities()

        if len(result) == 0:
            print("No Opportunity Found")
        else:
            print(result.head(5))
            
    # ------------------------------------------
    # Run Analyzer
    # ------------------------------------------
    def run(self):
        self.dataset_summary()
        self.missing_values()
        self.statistics()
        self.top_restaurants()
        self.top_locations()
        self.cuisine_analysis()
        self.merge_competition()
        self.high_demand_cuisines()
        self.low_competition()
        self.recommendation()
        return self.df