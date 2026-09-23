# RestaurantIQ

RestaurantIQ is a Python-based restaurant investment recommendation system. It cleans restaurant data, performs restaurant and cuisine analysis, analyzes customer reviews, measures competition, and calculates an investment score for potential restaurant opportunities.

## Features

- Analyze restaurant data for **Bangalore** and **Hyderabad**
- Process an entire city or a specific location
- Clean and standardize restaurant data
- Generate dataset statistics and missing-value analysis
- Identify top-rated restaurants and locations
- Analyze cuisines and competition
- Perform simple review sentiment analysis
- Normalize rating, votes, competition, and sentiment
- Calculate an investment score
- Save investment-score reports as CSV files

## Project Structure

```text
RestaurantIQ/
├── data/
│   ├── bangalore_restaurant.csv
│   └── hyderabad_restaurant.csv
├── reports/
│   ├── bangalore_investment_scores.csv
│   └── hyderabad_investment_scores.csv
├── services/
│   ├── analyzer.py
│   ├── cleaner.py
│   ├── review_parser.py
│   └── scorer.py
├── column_mapping.py
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

## Technology

- Python 3.12.3
- Pandas 2.2.3
- NumPy 2.2.6

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd RestaurantIQ
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

The program will ask you to:

1. Select a city.
2. Choose whether to analyze the entire city or a particular location.
3. Run the analysis pipeline.
4. Generate an investment score.
5. Save the final report in the `reports/` directory.

## Analysis Pipeline

```text
Restaurant CSV Data
        ↓
Data Cleaning
        ↓
Restaurant Analysis
        ↓
Review / Sentiment Analysis
        ↓
Competition Analysis
        ↓
Normalization
        ↓
Investment Score
        ↓
Investment Recommendation Report
```

## Investment Score

The investment score combines four normalized factors:

- Restaurant rating
- Number of votes
- Competition level
- Review sentiment

Competition is treated inversely: lower competition receives a better normalized score.

The project uses dynamic weights based on the characteristics of the dataset.

## Output

After execution, CSV reports are generated in:

```text
reports/
```

Example:

```text
reports/bangalore_investment_scores.csv
reports/hyderabad_investment_scores.csv
```

## Important Note

The CSV files in `data/` are part of the project input data. If you intend to publish the repository publicly, verify that you have permission to redistribute the datasets and that they do not contain restricted or sensitive information.

## Author

RestaurantIQ — Restaurant Investment Recommendation System

## Dummy changes