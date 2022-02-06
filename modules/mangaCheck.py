import pandas as pd
from modules.pg404Check import pg404Check

li = "{}/chapter-{}"

def chapterCheck(row):    
    lin = str(row["Link"])
    lc = int(row["LatestChapter"])
    lrc = int(row["LastReadChapter"])
    while(pg404Check(li.format(lin, str(lc)))):
        lc = lc+1
    lc = lc - 1
    if lc > lrc:
        print("Latest Chapter for '{}' is {}".format(row["Title"], lc))
    
    return lc

# data = pd.read_csv("List.csv")
# pd.set_option('display.max_colwidth', None)
# data['UpdatedDate'] = pd.to_datetime(data['UpdatedDate'])
# print(data)

# for index, row in data.iterrows():
#     #print(row["Link"])
#     chapterCheck(row)