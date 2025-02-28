import yfinance as yf
import streamlit as st

import datetime
################################################################
## VERSION 2
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Nhập ticker symbol và xem biểu đồ giá đóng cửa và khối lượng giao dịch.
""")

# INPUT

# Nhận ticker symbol từ người dùng, mặc định là 'GOOGL'
tickerSymbol = st.text_input('Nhập ticker symbol:', 'GOOGL')

start_date = st.date_input("Chọn ngày bắt đầu:", datetime.date(2010, 5, 31))
end_date = st.date_input("Chọn ngày kết thúc:", datetime.date(2020, 5, 31))

# ----------------------------------------------------------------

# Lấy dữ liệu của ticker từ yfinance
tickerData = yf.Ticker(tickerSymbol)

# Lấy dữ liệu lịch sử từ ngày 31/05/2010 đến 31/05/2020
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

# Hiển thị biểu đồ giá đóng cửa
st.write(f"### Giá đóng cửa của {tickerSymbol}")
st.line_chart(tickerDf.Close)

# Hiển thị biểu đồ khối lượng giao dịch
st.write(f"### Khối lượng giao dịch của {tickerSymbol}")
st.line_chart(tickerDf.Volume)
