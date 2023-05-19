import pandas as pd

data = pd.read_csv("C:/Users/Work/Downloads/Ecommerce Customers.csv")

def data_transformation(data):
    
    data["Email"] = data["Email"].str.replace("@", "").astype(str)
    
    return data

data_transformed = data_transformation(data)
