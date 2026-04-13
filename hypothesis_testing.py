import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
data = pd.read_csv("C:\\Users\\Shravya\\OneDrive - Malla Reddy Engineering College for Women\\Desktop\\apexxx\\TASK 4\\dataset.csv")

# Separate profit values
tech_profit = data[data["Category"] == "Technology"]["Profit"]
furniture_profit = data[data["Category"] == "Furniture"]["Profit"]

# Perform T-test
t_stat, p_value = ttest_ind(tech_profit, furniture_profit)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Interpretation
if p_value < 0.05:
    print("Result: Significant difference in profit between categories.")
else:
    print("Result: No significant difference in profit.")