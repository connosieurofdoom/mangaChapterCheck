from setup import setup 
setup()
import pandas as pd
from modules.mangaCheck import chapterCheck



data = pd.read_csv("List.csv", index_col="Index")
pd.set_option('display.max_colwidth', None)
data['UpdatedDate'] = pd.to_datetime(data['UpdatedDate'])
# print(data)
liAr = list()
for index, row in data.iterrows():
    data.at[index, "LatestChapter"] = chapterCheck(row)
    if int(row["LastReadChapter"]) < int(row["LatestChapter"]):
        liAr.append(row["Title"])

from modules.msgBox import msgBox
msgBox(liAr)

# print(data)
data.to_csv("List.csv")