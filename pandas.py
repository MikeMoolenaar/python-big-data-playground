import pandas as pd
from PandaTools import PandaTools

df = pd.read_csv('assets/genshin_weapons.csv')

# <START> Some handy functions
# Print columns and their data types
df.info()

# Print the first and last 5 rows (you can also specify the number)
print(df.head())
print(df.tail())

# Print the possible values of a column
print(df['rarity'].unique())


# <END> Some handy functions

# <START> Main functions

# Drop unnecessary columns
df = df.drop(columns=['general_enemy_drop_3'])
# Also works:
df.drop(['general_enemy_drop_3'], axis=1, inplace=True)

# Filter
dfVeryRare = df[df['rarity'] == '5 Stars']
dfNotRare = df[df['rarity'] != '5 Stars']

# Filter with multiple conditions
dfVeryRareBow = df[(df['rarity'] == '5 Stars') & (df['type'] == 'Bow')]
# Also works with query (more readable imo)
dfVeryRareBow = df.query('rarity == "5 Stars" and type == "Bow"')

# Filter by contains (case-insensitive) and not contains
dfSkywardWeapons = df[df['weapon_name'].str.contains('skyward', case=False)]
dfNotSkywardWeapons = df[~df['weapon_name'].str.contains('skyward', case=False)]

# Filter where field is nan / not defined
dfWeaponNotDefined = df[df["weapon_name"].isna()]

# Only get row with distinct names (remove duplicates)
dfDistinct = df.drop_duplicates(subset=['weapon_name'])

# Iterate over rows
print('Very rare bows:')
for index, row in dfVeryRare[dfVeryRare['type'] == 'Bow'].iterrows():
    print(f'{row["weapon_name"]} with base attack of {row["base_atk"]}')

# Execute function when value is defined
for index, row in dfVeryRare.iterrows():
    if pd.notna(row["weapon_name"]):
        print("weapon_name is defined")

# Create a new computed column
def calculate(x):
    return round((x["max_atk"] - x["base_atk"]) / x["max_atk"] * 100, 2)
df["percentage_of_max_atk_is_base"] = df.apply(lambda x: calculate(x), axis=1)

# Drop rows where certain column is null
dfNaPassiveName = df.dropna(subset=['passive_name'])

# group by
dfGroupedCount = df.groupby('type').size().reset_index(name='count')
dfGrouped = df.groupby('type').agg({'weapon_name': 'count', 'base_atk': 'mean'}).reset_index()

# Sort (ascending is the default, from lowest to highest)
dfSortBaseAtk = df.sort_values(by=['base_atk'], ascending=False)

# Only get rows where multiple columns are duplicated
dfDuplicates = df[df.duplicated(subset=['type', 'max_atk', 'base_atk'], keep=False)]

# Get all weapon names that are not in a dataframe
dfTemp = pd.DataFrame({'name': ['Skyward Harp', 'A Thousand Floating Dreams', 'Amos\' Bow']})
dfNotIn = df[~df['weapon_name'].isin(dfTemp['name'])]

# Rename multiple columns
dfRenames = df.rename(columns={
    'weapon_name': 'name',
    'rarity': 'stars'
})

PandaTools.open_df_in_libre_office(df, path='assets/genshin_weapons_output', filetype='ods')
