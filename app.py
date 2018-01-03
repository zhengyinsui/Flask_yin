from flask import Flask, render_template, request, redirect,session
import requests, json
import urllib2
import simplejson as json
import pandas as pd
import bokeh
from bokeh.plotting import figure
from bokeh.embed import components


#app_lulu.vars={}
app = Flask(__name__)
#com

#print (test)

#json_object = r.json


#print(json_object)
@app.route('/main')
def main():
  return redirect('/')

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/graph',methods=['POST'])
def graph():

  ticker= request.form['ticker']

  # url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?api_key=sZHH2h365tvNXxTvQzMu'
  #api_key = 'sZHH2h365tvNXxTvQzMu'

  # r = requests.get(url).json()
  #df= pd.DataFrame({col: dict(vals) for col, vals in r.items()})
  # json_object=json.loads(r)
  #test = r['datatable']
  #df=pd.DataFrame(r['datatable']['data'], columns=r['datatable']['data'].columns)
  #df['Date'] = pandas.to_datetime(df['Date'])

  df= pd.read_csv('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?api_key=wNAMU_EAudzbWW6zxay_')



  df = df[['ticker','date' ,'open', 'high', 'low', 'close']]


  plot = figure(title='Stock prices',
             x_axis_label='date',
             x_axis_type='datetime')


  if request.form.get('open'):
    plot.line(x=df['date'].values, y=df['open'].values, line_width=2, line_color="red", legend='Open')

  script, div = components(plot)
  return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
