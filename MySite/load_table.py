from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)
path ='C:/Users/egm94/PycharmProjects/Website/MySite/models'
df = pd.read_csv(f'{path}/df_result.csv')


@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('bot_overview.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
    #return render_template('bot_overview.html',  tables=[df.to_html(classes='data', header="true")])

@app.route("/table")
def home():
    return render_template('bot_overview.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)

'''
@app.route("/table")
def update():
    pass
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0')