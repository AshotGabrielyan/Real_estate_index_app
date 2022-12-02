import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from params import *


def get_line_fig(df,temp_cat, temp_indice, temp_indice_type):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df[temp_indice], mode='lines', name=temp_indice))
        fig.update_layout(title=temp_cat.replace('Index','') + temp_indice + ' compared to ' + temp_indice_type, title_x=0.5, xaxis_title="Date", yaxis_title=temp_indice)
        fig.update_xaxes(tickangle= 45)
        return fig


def get_bar_fig(df, temp_date):
        fig = px.bar(df[df.Date == temp_date], x="District", y="Price_USD")
        fig.update_layout(title_text="Average Price per District", title_x=0.5, yaxis_title = 'Price in USD')
        return fig
