import pandas as pd
import os

df_dic = dict()
for file in os.listdir():
    if file.endswith('.json'):
        df_dic[file.replace('.json','')] = pd.read_json(file)


for college in df_dic:
    df_dic[college]['name_college'] = college
    df_dic[college].reset_index(inplace=True)
    df_dic[college].set_index('name_college',inplace=True)
    df_dic[college].rename({'index':'major',0:'text'},axis=1,inplace=True)


df_lst = list(df_dic.values())
merge_df = df_lst[0]
for df in df_lst[1:]:
    merge_df = pd.concat([merge_df, df], axis=0)

merge_df.to_csv('merged.csv')
merge_df.to_json('merged.json',orient='records') # change orient if you need diferrent type of json