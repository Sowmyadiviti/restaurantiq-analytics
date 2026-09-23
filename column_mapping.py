CITIES = {
    "Bangalore": {
        "file": "data/bangalore_restaurant.csv",
        "encoding": "latin-1",
        "mapping": {
            "name":                                "name",
            "location":                            "location",
            "listed_in(city)":                     "area",
            "rest_type":                           "rest_type",
            "cuisines":                            "cuisines",
            "approx_cost(for two people)":         "approx_cost",
            "rate":                                "rate",
            "votes":                               "votes",
            "online_order":                        "online_order",
            "book_table":                          "book_table",
            "reviews_list":                        "reviews_list",
            "listed_in(type)":                     "listing_type",
        }
    },
    "Hyderabad": {
        "file": "data/hyderabad_restaurant.csv",
        "encoding": "latin-1",
        "mapping": {
            "name":                                "name",
            "location":                            "location",
            "listed_in(city)":                     "area",
            "rest_type":                           "rest_type",
            "cuisines":                            "cuisines",
            "approx_cost(for two people)":         "approx_cost",
            "rate":                                "rate",
            "votes":                               "votes",
            "online_order":                        "online_order",
            "book_table":                          "book_table",
            "reviews_list":                        "reviews_list",
            "listed_in(type)":                     "listing_type",
        }
    }
    
}   

COLUMN_MAPPING = CITIES["Bangalore"] ["mapping"]