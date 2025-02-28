# ################################################################
# ## VERSION 2
import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
import pandas as pd
import plotly.graph_objects as go


# Sidebar: nhập liệu
st.sidebar.header("Tùy chọn nhập liệu")
stock_options = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
selected_stocks = st.sidebar.multiselect("Chọn cổ phiếu:", stock_options, default=['AAPL', 'GOOGL', 'MSFT'])
start_date = st.sidebar.date_input("Chọn ngày bắt đầu:", datetime.date(2010, 5, 31))
end_date = st.sidebar.date_input("Chọn ngày kết thúc:", datetime.date(2025, 2, 28))

# # ----------------------------------------------------------------
# # GET DATA

# Lấy dữ liệu giá đóng cửa cho các cổ phiếu đã chọn
if selected_stocks:
    data = yf.download(selected_stocks, start=start_date, end=end_date)['Close']
else:
    data = pd.DataFrame()


# # ----------------------------------------------------------------
# # SHOW DATA
    
# Tạo tabs: một cho biểu đồ, một cho bảng dữ liệu
tab_chart, tab_table, tab_candle = st.tabs(["Chart", "Table Data", "Candlestick Chart"])

with tab_chart:
    st.write("### Biểu đồ giá đóng cửa")
    st.line_chart(data)

with tab_table:
    st.write("### Dữ liệu bảng")
    st.dataframe(data)


# Tab 3: Biểu đồ nến cho ticker riêng
with tab_candle:
    st.header("Biểu đồ nến")
    # Nhập ticker cho biểu đồ nến (mặc định là AAPL)
    candlestick_ticker = st.text_input("Nhập ticker cho biểu đồ nến:", "AAPL", key="candlestick_ticker")
    
    if candlestick_ticker:
        data = yf.download(candlestick_ticker, start=start_date, end=end_date)

        # Nếu chỉ có 1 ticker, ta gộp tên cột bằng cách lấy level 0
        # Kết quả: "Open", "High", "Low", "Close", "Adj Close", "Volume"
        # GỘP CỘT VÀ LÀM PHẲNG

        data.columns = data.columns.droplevel(1)

        # Tạo biểu đồ nến với Plotly
        fig = go.Figure(
            data=[go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name=candlestick_ticker
            )]
        )

        fig.update_layout(
            title=f"Biểu đồ nến: {candlestick_ticker}",
            xaxis_title="Ngày",
            yaxis_title="Giá (USD)"
        )

        st.plotly_chart(fig)
    else:
        st.write("Không có dữ liệu cho ticker này.")