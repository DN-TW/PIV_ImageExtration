import pandas as pd
import os
from tqdm import tqdm

# Set the file paths and column names
file_paths = []
column_names = []

for file_name in os.listdir():
    if file_name.endswith(".txt"):
        file_paths.append(file_name)
        start_index = file_name.index("]_") + 2
        end_index = file_name.index(".txt")
        segment = file_name[start_index:end_index]
        column_names.append(segment)

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each file path and column name
for file_path, column_name in tqdm(zip(file_paths, column_names),
                                   total=len(file_paths),
                                   desc="Merging files",
                                   ):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Rename the column containing the values to the corresponding column name
    data = data.rename(columns={data.columns[1]: column_name})

    # Merge the data into the merged_data DataFrame
    if merged_data.empty:
        merged_data = data
    else:
        merged_data = pd.merge(merged_data, data, on="Frame Nr.")

# Calculate the "Time (sec.)" values based on the relationship T = (F-1)*0.01
merged_data["Time (sec.)"] = (merged_data["Frame Nr."] - 1) * 0.1

# Move the "Time (sec.)" column to the position between "Frame Nr." and "A"
time_column = merged_data.pop("Time (sec.)")
merged_data.insert(1, "Time (sec.)", time_column)

# Save the merged data to a new CSV file
merged_data.to_csv("merged_data.csv", index=False)
