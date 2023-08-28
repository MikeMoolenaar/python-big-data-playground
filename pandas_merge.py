import pandas as pd
from PandaTools import PandaTools

df = pd.read_csv('assets/genshin_weapons.csv')

df = df.query('rarity == "5 Stars" and type == "Bow"')

dfRareBowComments = pd.DataFrame({
    'name': ['Skyward Harp', 'Amos\' Bow', 'Elegy for the End'],
    'comment': ['Best bow for DPS', 'Best bow for DPS', 'Best bow for support']
})

merged = pd.merge(df, dfRareBowComments, how='left', left_on='weapon_name', right_on='name')

merged = merged[['weapon_name', 'comment', 'base_atk', 'max_atk']]
PandaTools.open_df_in_libre_office(merged, path='assets/genshin_weapons_merged', filetype='ods')