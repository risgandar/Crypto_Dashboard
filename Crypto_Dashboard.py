import streamlit as st 
from api_key import api_key
from coinpaprika import client as Coinpaprika
import pandas as pd

client=Coinpaprika.Client(api_key=api_key)

st.header('CoinPaprika Dashboard')
instrument = st.sidebar.selectbox('Instrument Type', options=
                                  ('coins','coin','events','exchange_list','exchanges','global_market','markets',
                                   'today','ticker','tickers','twitter','historical','ohlcv','price_converter','exchange_markets'))

if (instrument == 'coins') or (instrument == 'exchange_list') or (instrument == 'global_market') or (instrument == 'tickers'):
    data = getattr(client, instrument)()
    try:
        df = pd.DataFrame(data)
    except:
        df = pd.DataFrame(data,index=[0]).T
    st.write(df)
    
if (instrument == 'coin') or (instrument == 'events') or (instrument == 'exchanges') or (instrument == 'today') or (instrument == 'ticker') or (instrument == 'twitter') or (instrument == 'markets') or (instrument == 'historical') or (instrument == 'ohlcv') or (instrument == 'price_converter'):
    id = st.sidebar.text_input('Coin ID','btc-bitcoin')
    try:
        data = getattr(client, instrument)(id)
    except:    
        if instrument == 'historical':
            date = st.sidebar.text_input('Date','2024-02-27T00:00;00Z')
            data = client.historical(id,start=date)
        if (instrument == 'ohlcv'):
            date = st.sidebar.text_input('Date','2024-02-27T00:00;00Z')
            data = client.historical(id,start=date)
        if (instrument == 'price_converter'):
            quote_curr = st.sidebar.text_input('Quote Currensy ID','usd-us-dollars')
            amount = st.sidebar.text_input('Amount',1000)
            data = client.price_converter(base_currency_id=id, quote_currency_id=quote_curr, amount=amount)
    try:
        df = pd.DataFrame(data)
    except:
        df = data
    st.write(df)
    
    if (instrument == 'exchange_markets'):
        exchange = st.sidebar.text_input('Exchange','binance')
        data = getattr(client,instrument)(exchange)
        df = data
        st.write(df)