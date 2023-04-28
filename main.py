from flask import Flask, render_template, request, redirect, url_for
from tweepy_streamer import main_func

app = Flask(__name__)
app.config['MY_VARIABLE'] = []


@app.route('/')
def index():
  return render_template('mainpage.html')


@app.route('/<company_name>')
def company_info(company_name):
  lol = main_func(company_name)
  return render_template("company.html", lol=lol, company_name=company_name)


app.run(debug=True, host='0.0.0.0', port=8080)
