import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Fetch Live Data from a Free API
print("Fetching live market data...")
url = "https://coingecko.com"
response = requests.get(url)
data = response.survey_json() if hasattr(response, 'survey_json') else response.json()

# 2. Structure and Clean Data using Pandas
# Convert the messy JSON format into a clean DataFrame (table)
df = pd.DataFrame(data).T
df.index.name = 'Asset'
df = df.reset_index()

# Add a timestamp column so we know exactly when the data was captured
df['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Capitalize asset names for professional presentation
df['Asset'] = df['Asset'].str.upper()

print("\n--- Cleaned Data Table ---")
print(df)

# 3. Save to a CSV Database
csv_file = "market_prices.csv"
# If the file already exists, append to it; otherwise, create a new one
if not os.path.isfile(csv_file):
    df.to_csv(csv_file, index=False)
else:
    df.to_csv(csv_file, mode='a', header=False, index=False)
print(f"\nSuccessfully saved data to {csv_file}")

# 4. Generate a Visual Visual Chart
plt.figure(figsize=(8, 5))
plt.bar(df['Asset'], df['usd'], color=['#F2A900', '#3C3C3D', '#00C6FF'])
plt.title('Live Asset Prices in USD')
plt.xlabel('Cryptocurrency')
plt.ylabel('Price ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the chart as an image file
plt.savefig('price_chart.png')
print("Chart generated and saved as 'price_chart.png'!")
