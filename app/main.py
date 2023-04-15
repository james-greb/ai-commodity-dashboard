from flask import Blueprint, render_template
import yfinance as yf

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    symbols = ['CL=F', 'GC=F', 'SI=F'] # Sample symbols for crude oil, gold, and silver futures
    prices = {}
    
    for symbol in symbols:
        data = yf.Ticker(symbol).info
        prices[symbol] = data['regularMarketOpen']
    
    return render_template('index.html', prices=prices)
