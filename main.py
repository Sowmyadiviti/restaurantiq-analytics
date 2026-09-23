import pandas as pd
from config import AVAILABLE_CITIES
from services.cleaner import DataCleaner
from services.analyzer import RestaurantAnalyzer
from services.review_parser import ReviewParser
from services.scorer import InvestmentScorer

def main():
    print("=" * 70)
    print("RestaurantIQ - Investment Recommendation System")
    print("=" * 70)

    # ------------------------------------------------
    # Step 1 : Show Cities
    # ------------------------------------------------
    print("\nAvailable Cities\n")
    for i, city in enumerate(AVAILABLE_CITIES.keys(), start=1):
        print(f"{i}. {city}")
    city = input("\nEnter City Name : ").strip().title()

    if city not in AVAILABLE_CITIES:
        print("\nSorry! This city is not available at the moment.")
        return
    print(f"\n{city} is available.")
    DATA_FILE = AVAILABLE_CITIES[city]

    # ------------------------------------------------
    # Step 2 : Ask User
    # ------------------------------------------------
    print(f"\nChoose Option for {city}")
    print("1. Entire City")
    print("2. Particular Location")
    choice = input("\nEnter Choice : ")

    # ====================================================
    # OPTION 1 : ENTIRE CITY
    # ====================================================
    if choice == "1":
        print(f"\nLoading Complete {city} Dataset...\n")
        cleaner = DataCleaner(DATA_FILE)
        cleaner.load_dataset()
        df = cleaner.clean_dataset()

    # ====================================================
    # OPTION 2 : PARTICULAR LOCATION
    # ====================================================
    elif choice == "2":
        print("\nReading Location Column...\n")
        location_df = pd.read_csv(
            DATA_FILE,
            usecols=["location"]
        )
        locations = sorted(location_df["location"].dropna().unique())
        print(f"\nLocations Available in {city}\n")
        for i, loc in enumerate(locations, start=1):
            print(f"{i}. {loc}")
        while True:

            try:
                num = int(input("\nEnter Location Number : "))
                if 1 <= num <= len(locations):
                    selected_location = locations[num - 1]
                    break
                else:
                    print("Invalid Location Number.")
            except ValueError:
                print("Enter a valid number.")

        print(f"\nSelected Location : {selected_location}")
        print(f"\nLoading {selected_location} restaurants from {city}...\n")
        df = pd.read_csv(DATA_FILE)
        df = df[df["location"] == selected_location].copy()
        cleaner = DataCleaner(DATA_FILE)
        cleaner.df = df
        df = cleaner.clean_dataset()
    else:
        print("\nInvalid Choice.")
        return

    # ------------------------------------------------
    # Step 3 : Analysis
    # ------------------------------------------------
    analyzer = RestaurantAnalyzer(df)
    df = analyzer.run()

    # ------------------------------------------------
    # Step 4 : Review Analysis
    # ------------------------------------------------ 
    parser = ReviewParser(df)
    df = parser.run()

    # ------------------------------------------------
    # Step 5 : Investment Score
    # ------------------------------------------------
    scorer = InvestmentScorer(df, city)
    df = scorer.run()

    print("\n" + "=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print("=" * 70)

if __name__ == "__main__":
    main()