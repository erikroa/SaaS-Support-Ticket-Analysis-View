import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("suraj520/customer-support-ticket-dataset")
print("Path to dataset files:", path)

# Load the data
df = pd.read_csv(path + '/customer_support_tickets.csv')
print(df.columns)
print(df.head())