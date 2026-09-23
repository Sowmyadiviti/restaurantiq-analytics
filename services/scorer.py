import pandas as pd
import numpy as np
class InvestmentScorer:
    def __init__(self, df,city):
        self.df = df
        self.city = city

    # ------------------------------------------
    # Min-Max Normalization
    # ------------------------------------------
    def normalize(self, column):
        minimum = self.df[column].min()
        maximum = self.df[column].max()

        if maximum == minimum:
            self.df[column + "_norm"] = 0
        else:
            self.df[column + "_norm"] = (
                self.df[column] - minimum
            ) / (
                maximum - minimum
            )
        print(f"{column} Normalized Successfully")
        
    # ------------------------------------------
    # Normalize Competition
    # ------------------------------------------
    def normalize_competition(self):

        minimum = self.df["competition"].min()
        maximum = self.df["competition"].max()

        if maximum == minimum:
            self.df["competition_norm"] = 0
        else:
            self.df["competition_norm"] = (
                maximum - self.df["competition"]
            ) / (
                maximum - minimum
            )

        print("Competition Normalized")

    # ------------------------------------------
    # Normalize Sentiment
    # ------------------------------------------
    def normalize_sentiment(self):

        minimum = self.df["sentiment_score"].min()
        maximum = self.df["sentiment_score"].max()

        if maximum == minimum:
            self.df["sentiment_norm"] = 0
        else:
            self.df["sentiment_norm"] = (
                self.df["sentiment_score"] - minimum
            ) / (
                maximum - minimum
            )

        print("Sentiment Normalized")

    # ------------------------------------------
    # Dynamic Weight Calculation
    # ------------------------------------------
    def calculate_weights(self):
        max_rating = self.df["rate"].max()
        max_votes = self.df["votes"].max()
        max_competition = self.df["competition"].max()
        max_sentiment = self.df["sentiment_score"].max()

        # -----------------------------
        # Rating Weight
        # -----------------------------
        if max_rating <= 3:
            rating_weight = 0.30
        elif max_rating <= 4:
            rating_weight = 0.35
        else:
            rating_weight = 0.40

        # -----------------------------
        # Votes Weight
        # -----------------------------
        if max_votes <= 10000:
            votes_weight = 0.25
        elif max_votes <= 20000:
            votes_weight = 0.30
        elif max_votes <= 50000:
            votes_weight = 0.35
        else:
            votes_weight = 0.40

        # -----------------------------
        # Competition Weight
        # -----------------------------
        if max_competition <= 20:
            competition_weight = 0.20
        elif max_competition <= 50:
            competition_weight = 0.25
        else:
            competition_weight = 0.30

        # -----------------------------
        # Sentiment Weight
        # -----------------------------
        if max_sentiment <= 5:
            sentiment_weight = 0.10
        elif max_sentiment <= 10:
            sentiment_weight = 0.15
        else:
            sentiment_weight = 0.20

        print("\nWeights")
        print(f"Rating      : {rating_weight}")
        print(f"Votes       : {votes_weight}")
        print(f"Competition : {competition_weight}")
        print(f"Sentiment   : {sentiment_weight}")
        return (
            rating_weight,
            votes_weight,
            competition_weight,
            sentiment_weight
        )
        
    # ------------------------------------------
    # Investment Score
    # ------------------------------------------
    def calculate_score(self):
        (
            rating_weight,
            votes_weight,
            competition_weight,
            sentiment_weight
        ) = self.calculate_weights()
        self.df["investment_score"] = (
            rating_weight * self.df["rate_norm"]
            +
            votes_weight * self.df["votes_norm"]
            +
            sentiment_weight * self.df["sentiment_norm"]
            +
            competition_weight * self.df["competition_norm"]
        )
        print("Investment Score Calculated")
        
    # ------------------------------------------
    # Top Recommendations
    # ------------------------------------------
    def top_recommendations(self):
        result = self.df.sort_values(
            by="investment_score",
            ascending=False
        )
        print("\nTop Investment Opportunities\n")
        print(
            result[
                [
                    "location",
                    "cuisines",
                    "rate",
                    "votes",
                    "competition",
                    "investment_score"
                ]
            ]
            .head(10)
        )
        return result

    # ------------------------------------------
    # Save Report
    # ------------------------------------------
    def save_results(self):
     file_name = self.city.lower().replace(" ", "_")
     self.df.to_csv(
        f"reports/{file_name}_investment_scores.csv",
        index=False
    )
    print("Investment Report Saved")
        
    # ------------------------------------------
    # Run
    # ------------------------------------------
    def run(self):
        self.normalize("rate")
        self.normalize("votes")
        self.normalize_competition()
        self.normalize_sentiment()
        self.calculate_score()
        self.top_recommendations()
        self.save_results()
        return self.df