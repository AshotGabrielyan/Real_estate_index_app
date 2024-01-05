import streamlit as st
import pandas as pd
import plotly.express as px
from params import *
from utils import *





st.set_page_config(page_title = 'Real Estate Market in Yerevan', page_icon = ":tada:", layout = "wide")
st.title('Real Estate Market in Yerevan')
with st.sidebar:
        st.title('Price and Rent Changes')
        temp_cat = st.selectbox('Select the Index:',('Select','Real Estate Price Index', 'Real Estate Rent Index'))
        temp_indice_type = st.selectbox('Select Comparison Baseline:',('Select','Previous month', 'Base month'))
        temp_indice = st.selectbox('Select Index Measure:',('Select','Laspeyres index', 'Paasche index', 'Fisher index'))
        st.title('Data Info')
        temp_date = st.selectbox('Select the date:',DATES_TO_SELECT)


if temp_cat == 'Real Estate Price Index' and temp_indice_type == 'Previous month':
        df = pd.read_csv('app_data/house_price_index_previous.csv')
        if temp_indice == 'Laspeyres index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Paasche index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Fisher index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))


if temp_cat == 'Real Estate Price Index' and temp_indice_type == 'Base month':
        df = pd.read_csv('app_data/house_price_index_base.csv')
        if temp_indice == 'Laspeyres index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Paasche index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Fisher index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
                
if temp_cat == 'Real Estate Rent Index' and temp_indice_type == 'Previous month':
        df = pd.read_csv('app_data/house_rent_index_previous.csv')
        if temp_indice == 'Laspeyres index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Paasche index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Fisher index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
                

if temp_cat == 'Real Estate Rent Index' and temp_indice_type == 'Base month':
        df = pd.read_csv('app_data/house_rent_index_base.csv')
        if temp_indice == 'Laspeyres index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Paasche index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
        if temp_indice == 'Fisher index':
                st.write(get_line_fig(df,temp_cat, temp_indice, temp_indice_type))
                


if temp_date in DATES and temp_cat == 'Real Estate Price Index':
        df = pd.read_csv('app_data/house_price_groupbied.csv')
        st.write(get_bar_fig(df, temp_date))

if temp_date in DATES and temp_cat == 'Real Estate Rent Index':
        df = pd.read_csv('app_data/house_rent_groupbied.csv')
        st.write(get_bar_fig(df, temp_date))



