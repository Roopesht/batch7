import pandas as pd
import numpy as np
# GEt the data
## Read the data from data.csv
df= pd.read_csv("data.csv")

# Clean up
## Get only Nifty
df = df[df["SYMBOL"] == 'NIFTY']
## Check if there is null values
## Check if there is sudden spikes (more than 5% up or down) and remove them
## Keep only necessary columns
df=df[["ADATE","SYMBOL","OPEN","HIGH","LOW","CLOSE", "TOTTRDQTY"]]
## convert the column names to lower case
df.columns = ["date","symbol","open","high","low","close", "volume"]
## Make adjustments (Out of scope)

#print (df)

# Create features
## Moving average for 7,20,50 days
df['ma_7']= df['close'].rolling(7).mean()
df['ma_20']= df['close'].rolling(20).mean()
df['ma_50']= df['close'].rolling(50).mean()

## Convert the values in to percentage - Because the predictions works well with %age instead of absolute values


# Create labels

# Split the data

# Train the model

# Calc accuracy

# Improvise

# Save the model
df.to_csv('data_new.csv')
#print (df)