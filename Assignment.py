# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import plotly.express as px
import streamlit as st

df= pd.read_csv(r'Assignment.csv')
df

fig1=px.line(df,x= 'Date', y= "GOLD", title = 'Change in Price of GOLD')
st.plotly_chart(fig1)
st.metric(label="GOLD Price", value="1675.5 USD", delta=" 9.64 %")

fig2=px.line(df,x= 'Date', y= ["GOLD","BRENT CRUDE"], title = 'Change in Price of GOLD & Crude Oil ')
st.plotly_chart(fig2)

fig3=px.histogram(df,x= "Date", y= 'NATURAL GAS', title = 'Change in the price of GAS')
st.plotly_chart(fig3)
st.metric(label="GAS Price", value="8.0290 USD", delta=" 278.3 %")

fig4=px.scatter(df, x='GOLD', y="Date")
st.plotly_chart(fig4)
 
fig5=px.bar(df, x='BRENT CRUDE', y='Date', title = 'Price Of Oil')
st.plotly_chart(fig5)