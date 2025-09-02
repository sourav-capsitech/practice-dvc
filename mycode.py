import pandas as pd
import os

#create a sample dataframe with column names
data={"Name":["Alice","Bob","Charlie"],
      "Age":[25,30,35],
      "City":["New York","Los Angeles","Chicago"]
      }
df=pd.DataFrame(data)

#ensures the data exist at the rrot level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path =os.path.join(data_dir, "people.csv")

#Save the DataFrame to a csv file, including column names
df.to_csv(file_path, index=False)

print(f"DataFrame saved to {file_path}")
