import pandas as pd
import plotly.express as px

# Load the data directly from a web link to avoid 'File Not Found' errors
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-04-20/netflix_titles.csv"
df = pd.read_csv(url)

print("Data Loaded Successfully!")
print(df.head()) # Shows the first 5 rows
# Check for missing values
print(df.isnull().sum())

# Fill missing 'country' with 'Unknown' so the map doesn't have holes
df['country'] = df['country'].fillna('Unknown')

# Drop rows where we don't have a 'date_added'
df.dropna(subset=['date_added'], inplace=True)
# Count the 'type' column
type_counts = df['type'].value_counts().reset_index()

fig1 = px.pie(type_counts, values='count', names='type', 
             title='Content Type Distribution: Movies vs TV Shows',
             color_discrete_sequence=px.colors.sequential.RdBu)
fig1.show()
# Get the top 10 countries producing content
top_countries = df['country'].value_counts().head(10).reset_index()

fig2 = px.bar(top_countries, x='country', y='count', 
             title='Top 10 Content Producing Countries',
             labels={'count': 'Number of Titles', 'country': 'Country'},
             color='count')
fig2.show()