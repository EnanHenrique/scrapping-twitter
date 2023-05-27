import json
import pandas as pd
from transformers import pipeline
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

from mysql_connection import MysqlConnection
load_dotenv()

with open('./scrapper_soybean_twitter.json', encoding='utf-8') as fh:
    data = json.load(fh)

sentiment_pipeline = pipeline("sentiment-analysis")
df = pd.DataFrame()
for search in data:
    for idx, line in enumerate(data[search]):
        dict_sentiment: dict = sentiment_pipeline(data[search][idx])[0]
        dict_sentiment.update({'search': search, 'date': datetime.now()})
        df_dict = pd.DataFrame([dict_sentiment])
        df = pd.concat([df, df_dict], ignore_index=True)

print(df)

mysql = MysqlConnection(user=getenv('BD_USER'), 
                            passwd=getenv('BD_PASS'),
                            host=getenv('BD_HOST'))
mysql.connect()
mysql.insert_dataframe(df, 'sentiment', 'twitter')
mysql.disconnect()

