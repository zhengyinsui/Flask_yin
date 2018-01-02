from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)


def ticker(filename):

key = [] # company name
value = [] # ticker symbol

with open(filename) as f:
    lst = [line.rstrip() for line in f]

    for line in range(0, len(lst), 2):
        key.append(lst[line])

    for line in range(1, len(lst), 2):
        value.append(lst[line])

dictionary = dict(zip(key, value))

# comment, yin version
