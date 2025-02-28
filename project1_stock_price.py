import yfinance as yf
import streamlit as st

################################################################
## VERSION SIMPLE

# st.write("""
# # Simple Stock Price App

# Shown are the stock closing price and volume of Google!

# """)

# #define the ticker symbol
# tickerSymbol = 'GOOGL'

# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)

# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# # Open	High	Low	Close	Volume	Dividends	Stock Splits

# st.line_chart(tickerDf.Close)

# st.line_chart(tickerDf.Volume)

################################################################
## VERSION 2
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Nhập ticker symbol và xem biểu đồ giá đóng cửa và khối lượng giao dịch.
""")

# Nhận ticker symbol từ người dùng, mặc định là 'GOOGL'
tickerSymbol = st.text_input('Nhập ticker symbol:', 'GOOGL')

# Lấy dữ liệu của ticker từ yfinance
tickerData = yf.Ticker(tickerSymbol)

# Lấy dữ liệu lịch sử từ ngày 31/05/2010 đến 31/05/2020
tickerDf = tickerData.history(period='1d', start='2025-02-20', end='2025-05-27')

# Hiển thị biểu đồ giá đóng cửa
st.write(f"### Giá đóng cửa của {tickerSymbol}")
st.line_chart(tickerDf.Close)

# Hiển thị biểu đồ khối lượng giao dịch
st.write(f"### Khối lượng giao dịch của {tickerSymbol}")
st.line_chart(tickerDf.Volume)
