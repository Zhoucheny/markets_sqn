import yfinance as yf
import json
import xlsxwriter
import datetime
import pandas as pd
import csv
import openpyxl
import re
import dateutil.relativedelta




#name = input("Which etf do you want: ")
#date1 = input("The day from: ")
#date2 = input("The day end: ")
#dayA= datetime.datetime.strptime(date1, '%Y-%m-%d')
#delta=datetime.timedelta(days=200)
#dayB=dayA-delta
datetimeNow = datetime.date.today()
date1 = datetimeNow + dateutil.relativedelta.relativedelta(months=-1,days=-150)
        
souce_data = yf.download("SPY", start=date1, end=datetimeNow)
#souce_data = yf.download("SPY", start=dayB, end=date2)

#workbook = xlsxwriter.Workbook('test2.csv')
#worksheet = workbook.add_worksheet()
#worksheet.write_column('A1',souce_data.index.strftime('%Y-%m-%d'))
#worksheet.write_column('B1', souce_data['Close'])
#workbook.close()
#print(souce_data['Close'])

df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
df.to_csv('pandas_to_excel1.csv')
etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
expectancy_data = etf_data["Close"].rolling(100).mean().apply(lambda x: '%.2f%%' % (x*100))
standerd_data = etf_data["Close"].rolling(100).std().apply(lambda x: '%.2f%%' % (x*100))
sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
#print(etf_df["Close"])
print(expectancy_data)
print(standerd_data)
print(sqn_data)
sqn_data.to_csv('pandas_to_excel2.csv')
etf_data123 = pd.read_csv('pandas_to_excel2.csv', engine= "python") 
print(etf_data123)








#print(souce_data['Close'])
#print(type(souce_data['Close']))
#print(souce_data.index)
#print(etf_df)

#print(etf_df["Close"], etf_df["Date"])

#etf_df[["Close","Date"]]



#df.count()
#souce_data.schema


