            Data Wrangling in Pandas 


#Task 1 - Load the Pokemon dataset
import pandas as pd
filepath = pokemon
df = pd.read_csv(filepath)
print(df)


#Task 2 - Explore the dataset
# Code starts here
# head of the dataframe
head = df.head(10)
print(head)

# describe the dataframe
describe = df.describe()
print(describe)

# shape of the dataframe
shape = df.shape
print(shape)

# check for null values
null = df.isnull().sum()
print(null)

# check for unique values
unique = df.nunique()
print(unique)

# code ends here

#Task 3 - Find total powers of Pokemon
#fect the specific column in pokemon table 
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
print(df['Total'])


#Task 4 - Rename, drop and clean
# Code starts here

# Rename columns 'HP', 'Sp. Atk' and 'Sp. Def' as 'Health Points', 'Attack speed points' and 'Defense speed points'
df.rename(columns = {'HP':'Health Points', 'Sp. Atk':'Attack speed points', 
'Sp. Def':'Defense speed points'}, inplace = True )

# Remove the '#' column permanently
df.drop(['#'], inplace = True, axis=1)


# Set index as names
df.set_index('Name', inplace= True)

# Look at the first 5 observations
df.head(5)

# Code ends here

#Task 5 - Find out information of Pokemons based on `Type 2` attribute 
# Code starts here

# Different variants of `Type 2`
type_two_num = df['Type 2'].nunique()
print(type_two_num)

# Total different types of `Type 2`
type_two = df['Type 2'].unique()
print(type_two)

# Counts for different types of `Type 2`
counts_type_two = df['Type 2'].value_counts()
print(counts_type_two)

# Number of Pokemons don't have `Type 2`
no_type_two = df['Type 2'].isnull().sum()
print(no_type_two)

# Code ends here


#Task 6 - Find the pokemon with the highest points
# Code starts here

# Which pokemon has the highest 'Health Points'?
healthiest_pokemon = df['Health Points'].idxmax()
print(healthiest_pokemon)

# Which pokemon has the highest Special Atack points?
special_attack_pokemon = df['Attack speed points'].idxmax()
print(special_attack_pokemon)

# Which pokemon has the highest Special Defense points?
special_defense_pokemon = df['Defense speed points'].idxmax()
print(special_defense_pokemon)

# Which pokemon has highest Speed?
fastest_pokemon = df['Speed'].idxmax()
print(fastest_pokemon)

# Code ends here


#Task 7 - Answer questions using data


# Drop row with Name as nan
df = df[df.index.notnull()]

# Code starts here
# print(df['Legendary'])
# Find out which type of pokemons (use only `Type 1`) have the highest chances of being Legendary
highest_legendary = df[df['Legendary']==True]['Type 1'].value_counts().idxmax()
print(highest_legendary)

# Pokemons which do not have 'Type 2' but are Legendary

single_type_legendary = len(df[df['Type 2'].isnull() & df['Legendary'] == True])
print(single_type_legendary)

# Code ends here

#Task 8 - Modify Pokemon names
# Code starts here

# Convert 'Name' to uppercase
df.index = df.index.str.upper()
print(df.index)

# Convert 'Type 1' to lowercase
df['Type 1'] = df['Type 1'].apply(lambda x: x.lower())
print(df['Type 1'])
# Convert 'Type 2' to lowercase if present else 
df['Type 2'] = df['Type 2'].apply(lambda x:x.lower() if isinstance(x, str) else None)
print(df['Type 2'])

#Task 9 - Find the fastest type (`Type 1`) Pokemons
import numpy as np
# Code starts here
# print(df.groupby(['Type 1']).groups)
# Determine which type (Type 1) pokemons are the fastest(Speed)
# print(df.groupby('Type 1')[['Speed']].median())
fastest_type = df.groupby('Type 1')['Speed'].agg(np.median).sort_values(ascending=False).idxmax()
print(fastest_type)
# Code ends here

#Task 10 - Calculate mean value of attack speed points across generations and types 
# Code starts here

# mean value of 'Attack speed points' according to 'Generation' and 'Type 1'
pivot = pd.pivot_table(df,index='Type 1',values='Attack speed points',
columns='Generation')
print(pivot)

# Code ends here

#Task 11 - Combine data by merging dataframes
# Input 

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})
# print(df1)
df2 = pd.DataFrame({'product': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})
# print(df2)

# Code starts here
# pd.merge(left='fruit', right='product', on='index', how='outer')
merged = pd.merge(df1, df2 ,left_on=['fruit','weight'], right_on=['product','kilo'], suffixes=['_left', '_right'], how='inner')
print(merged)
# Code ends here

#Task 12 - Categorize Attack speed points into Low Attack, Normal Attack and High Attack
# Code starts here
# Subset the dataframe of Attack speed points
Special_attack = df[['Attack speed points']]
# print(Special_attack)

# Print first 5 rows
print(Special_attack.head(5))

# Create a function attack
def attack(num): 
  
    if num < 60: 
        return "Low Attack"
  
    elif num> 60 and num <= 120: 
        return "Normal Attack"
  
    else: 
        return "High Attack"
# apply attack function on the feature Attack speed points.
Special_attack['Attack speed points'] = Special_attack['Attack speed points'].apply(attack) 
print(Special_attack)
# Code ends here


#Task 13 - Which pokemon type is the strongest and which the weakest? (according to total stats)
# Code starts here

#Determine which type (Type 1) pokemons are the Strongest(Total)
pokemon_type_avg = df.groupby('Type 1')['Total'].agg(np.mean).sort_values(ascending=False)
print(pokemon_type_avg)

# Strongest pokemon
strongest_type = pokemon_type_avg.idxmax()
print(strongest_type)

# Weakest pokemon
weakest_type = pokemon_type_avg.idxmin()
print(weakest_type)

# Code ends here
# Code starts here
# Set index name as Name
df.index.name = 'Name'
# Create a subset of "Legendary","Generation","Attack" based on `True` Legendary

pokemon_stats = df[df['Legendary']==True][["Legendary","Generation","Attack"]]
print(pokemon_stats)

# Groupby on data to find highest Legendary pokemon
pokemon_stats_legendary = pokemon_stats.groupby(['Generation','Name'])[['Attack']].agg(np.mean).idxmax()[0]
print(pokemon_stats_legendary)
# Code ends here

