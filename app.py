from flask import Flask, render_template, request, redirect, url_for, session
import requests, json
# import urllib2
import simplejson as json
import pandas as pd
import bokeh
from bokeh.plotting import figure, output_notebook, output_file, show, save, reset_output
from bokeh.embed import components

def make_plot(df_last_month, col_name, title):


    p = figure(title = '{} over Last Month'.format(title), x_axis_label = 'Date', y_axis_label = 'Price (Dollars)', x_axis_type = 'datetime')
    p.line(df_last_month['date'], df_last_month[col_name], color = 'blue')
    p.circle(df_last_month['date'], df_last_month[col_name], color = 'red')
    script, div = components(p)
    return render_template('graph.html', script = script, div = div)


app = Flask(__name__)

@app.route('/', method = ['GET'])
def index():
  return render_template('index.html')

@app.route('/graph',methods=['POST'])
def graph():
    tick_name = request.args['ticker_name']
    url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json'
    r = requets.get(url, {'ticker': tick_name,
                          'date.gt': '2010-01-01',
                          'opts.columns': 'date, close, adj_close',
                          'api_key': 'wNAMU_EAudzbWW6zxay'})
    r_new = r.json()
    r_list = r_new['datatable']['data']
    labels = ['date', 'close', 'adj_close']
    df = pd.DataFrame(r_list, columns = labels)
    df_last_month = df.iloc[-1:-22:-1, 0:3]
    df_last_month['date'] = pd.to_datetime(df_last_month['date'])
    if request.args['closing'] == 'closing_price':
        return make_plot(df_last_month, 'close', 'Closing Stock Price for {}'.format(tick_name))
    else:
        return make_plot(df_last_month, 'adj_close', 'Adj. Closing Stock Price for {}'.format(tick_name))

        # p = figure(title = 'Adj. Closing Stock Price for ' + tick_name + ' over Last Month', y_axis_label = 'Price (Dollars)', x_axis_type = 'datetime')
        # p.line(df_last_month['date'], df_last_month['adj_close'], color = 'blue')
        # p.circle(df_last_month['date'], df_last_month['adj_close'], color = 'red')
        # script, div = components(p)
        # return render_template('graph.html', script = script, div = div)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    # app.run(port=33507)
    app.run(host = '0.0.0.0', port = port)
