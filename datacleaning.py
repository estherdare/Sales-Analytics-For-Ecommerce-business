import pandas as pd 

#df is the dataframe that will be used for data cleaning

df = pd.read_csv('women_clothing_ecommerce_sales.csv') #Read the CSV file into a dataframe

df.shape #Check the shape of the dataframe
df.info() #Get information about the dataframe
df.head() #Display the first 5 rows of the dataframe

df.drop_duplicates(inplace=True) #Remove duplicate rows from the dataframe
df.dropna(subset=['order_date','unit_price','quantity'], inplace=True) #Remove rows with NaN values in specific columns 

df['order_date'] = pd.to_datetime(df['order_date']) #Convert 'order_date' to datetime format

df['revenue'] = df['unit_price'] * df['quantity'] #Calculate revenue by multiplying 'unit_price' and 'quantity'

df['order_month'] = df['order_date'].dt.to_period('M') #Extract month from 'order_date' and create a new column 'order_month'

df.to_csv('cleaned_women_clothing_ecommerce_sales.csv', index=False) #Save the cleaned dataframe to a new CSV file


# print(df.shape)
# print(df.info())
# print(df.head())



