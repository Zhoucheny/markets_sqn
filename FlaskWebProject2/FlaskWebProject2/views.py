"""
Routes and views for the flask application.
"""


from flask import Flask, render_template, request, jsonify
import yfinance as yf
from FlaskWebProject2 import app
import datetime
import dateutil.relativedelta
import json
import xlsxwriter
import pandas as pd
import csv
import openpyxl


@app.route('/')
@app.route('/home')
def hello_word():
    return render_template("index.html")

@app.route('/return', methods=['post'])
def return_home_page():
    return render_template("index.html")

@app.route("/submit_data", methods=['post'])
def submit_data():

    ename = request.form.get("ename")
    datetimeNow = datetime.date.today()

    if request.form['submit_button'] == 'research':
        date1 = request.form.get("date1")
        date2 = request.form.get("date2")
        dayA= datetime.datetime.strptime(date1, '%Y-%m-%d')
        delta=datetime.timedelta(days=150)
        dayB=dayA-delta
        souce_data = yf.download(ename, start=dayB, end=date2)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3, ename = ename  )
        #print(output_value)


        #return render_template("index.html" )

    elif request.form['submit_button'] == '2_Year':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(years=-2)
        
        souce_data = yf.download(ename, start=date1, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == '1_Month':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(months=-1,days=-150)
        souce_data = yf.download(ename, start=date1, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == '3_Monthes':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(months=-3,days=-150)
        souce_data = yf.download(ename, start=date1, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == '6_Monthes':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(months=-6,days=-150)
        souce_data = yf.download(ename, start=date1, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == '12_Monthes':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(months=-12,days=-150)
        souce_data = yf.download(ename, start=date1, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )



    elif request.form['submit_button'] == 'Year_To_Date':
        date1 = datetime.datetime(datetimeNow.year, 1, 1)
        date2 = date1 + dateutil.relativedelta.relativedelta(days=-150)
        souce_data = yf.download(ename, start=date2, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == '5_Year':
        date1 = datetimeNow + dateutil.relativedelta.relativedelta(years=-5)
        souce_data = yf.download(ename, start=date1, end=datetimeNow)        
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )


    elif request.form['submit_button'] == 'Max':
        souce_data = yf.download(ename, end=datetimeNow)
        df = pd.DataFrame(souce_data['Close'].pct_change(),souce_data.index)
        #df.schema
        df.to_csv('pandas_to_excel1.csv')
        etf_data = pd.read_csv('pandas_to_excel1.csv', engine= "python") 
        sqn_data = (etf_data["Close"].rolling(100).mean() / etf_data["Close"].rolling(100).std() * 10)
        sqn_datas = round(sqn_data,2)
        date_data = etf_data["Date"].to_json(orient= "records")
        parsed1 = json.loads(date_data)
        output_value = etf_data.to_json(orient= "records")        
        parsed2 = json.loads(output_value)
        price_data = sqn_datas.to_json(orient= "records")
        parsed3 = json.loads(price_data)
        print(parsed1) 
        print(parsed3)

        #date_datas = json.dumps(parsed1,indent=4)
        #output_values = json.dumps(parsed2,indent=4)
        #print(date_values)

        
        return render_template("result.html",parsed1 = parsed1, parsed3 = parsed3 )
    else:
        return render_template("index.html", msg = "No such data")


