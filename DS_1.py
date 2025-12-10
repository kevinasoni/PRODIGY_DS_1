import pandas as pd
import matplotlib.pyplot as plt

# Load dataset 
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_2461.csv', skiprows=4)

# Get latest year available
years = [col for col in df.columns if col.isdigit()]
latest_year = sorted(years)[-1]

# Get population values for that year
population = df[latest_year].dropna()

# Plot histogram
plt.figure(figsize=(12,6))
plt.hist(population / 1e6, bins=30)   # convert to millions
plt.xlabel("Population (in millions)")
plt.ylabel("Number of Countries")
plt.title(f"Distribution of Country Populations ({latest_year})")
plt.grid(True, linestyle="--", alpha=0.4)
plt.show()
