from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

path = 'C:/Users/egm94/PycharmProjects/Website/MySite/models'

@app.route('/auth')
def authentication():
    return render_template('authentication.html')


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


overview_bot = pd.read_csv(f'{path}/bot.csv')


@app.route("/table")
def overview():
    return render_template('bot_overview.html', column_names=overview_bot.columns.values,
                           row_data=list(overview_bot.values.tolist()),
                           zip=zip)


trading_historic = pd.read_csv(f'{path}/trading_historic.csv')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', column_names=trading_historic.columns.values,
                           row_data=list(trading_historic.values.tolist()),
                           zip=zip)


# sending datas to templates


if __name__ == '__main__':
    app.run(debug=True)
