import pandas as pd
import re

class ReviewParser:
    def __init__(self, df):
        self.df = df
        self.positive_words = [
            "good",
            "great",
            "excellent",
            "awesome",
            "best",
            "love",
            "amazing",
            "tasty",
            "nice",
            "perfect",
            "delicious",
            "friendly"
        ]
        self.negative_words = [
            "bad",
            "worst",
            "poor",
            "dirty",
            "slow",
            "late",
            "cold",
            "average",
            "waste",
            "rude"
        ]
        
    # -----------------------------------------
    # Generator
    # -----------------------------------------
    def review_generator(self):
        for review in self.df["reviews_list"]:
            yield str(review)

    # -----------------------------------------
    # Extract Ratings
    # -----------------------------------------
    def extract_rating(self, review):
        pattern = r"Rated\s([0-9]\.[0-9])"
        rating = re.findall(pattern, review)
        return rating

    # -----------------------------------------
    # Extract Review Text
    # -----------------------------------------
    def extract_review_text(self, review):
        pattern = r"Rated\s[0-9]\.[0-9](.*)"
        text = re.findall(pattern, review)
        return text
    
    # -----------------------------------------
    # Positive Word Count
    # -----------------------------------------
    def positive_count(self, review):
        review = review.lower()
        count = 0
        for word in self.positive_words:
            if word in review:
                count += 1
        return count

    # -----------------------------------------
    # Negative Word Count
    # -----------------------------------------
    def negative_count(self, review):
        review = review.lower()
        count = 0
        for word in self.negative_words:
            if word in review:
                count += 1
        return count
    
    # -----------------------------------------
    # Calculate Sentiment Score
    # -----------------------------------------
    def calculate_sentiment(self):
        scores = []
        for review in self.review_generator():
            positive = self.positive_count(review)
            negative = self.negative_count(review)
            score = positive - negative
            scores.append(score)
        self.df["sentiment_score"] = scores
        print("Sentiment Score Created")
        
    # -----------------------------------------
    # Average Review Length
    # -----------------------------------------
    def average_review_length(self):
        lengths = [
            len(str(review))
            for review in self.df["reviews_list"]
        ]
        average = sum(lengths) / len(lengths)
        print(f"\nAverage Review Length : {average:.2f}")

    # -----------------------------------------
    # Positive Word Frequency
    # -----------------------------------------
    def positive_frequency(self):
        frequency = {}
        for review in self.review_generator():
            review = review.lower()
            for word in self.positive_words:
                if word in review:
                    frequency[word] = frequency.get(word, 0) + 1
        print("\nPositive Word Frequency")
        print(frequency)

    # -----------------------------------------
    # Negative Word Frequency
    # -----------------------------------------
    def negative_frequency(self):
        frequency = {}
        for review in self.review_generator():
            review = review.lower()
            for word in self.negative_words:
                if word in review:
                    frequency[word] = frequency.get(word, 0) + 1
        print("\nNegative Word Frequency")
        print(frequency)
        
    # -----------------------------------------
    # Rating Distribution
    # -----------------------------------------
    def rating_distribution(self):
        ratings = []
        for review in self.review_generator():
            ratings.extend(
                self.extract_rating(review)
            )
        rating_series = pd.Series(ratings)
        print("\nReview Rating Distribution")
        print(rating_series.value_counts())

    # -----------------------------------------
    # Run
    # -----------------------------------------
    def run(self):
        print("\n========== REVIEW ANALYSIS ==========")
        self.calculate_sentiment()
        self.average_review_length()
        self.positive_frequency()
        self.negative_frequency()
        self.rating_distribution()
        return self.df
    