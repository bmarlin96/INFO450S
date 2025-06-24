import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


df=sns.load_dataset('penguins')
df=df.dropna()

#Add in a Title

st.title("Penguins Rock 🐧🐧🐧🐧🐧🐧")

if st.checkbox("Please press if you want to see the data"):
  st.header("this is our penguin Data")
  st.dataframe(df)


#first bar chart

penguin_counts=df['island'].value_counts().reset_index()
fig=px.bar(penguin_counts,x='island',y='count', color='island')
st.plotly_chart(fig)

#This is that box plot
fig=px.box(df,x="island",y="body_mass_g")
st.plotly_chart(fig)

#This is our scatter plot
fig_scatter=px.scatter(df,x="body_mass_g",y="bill_length_mm", color="species", size="body_mass_g", color_discrete_map={"Adelie": "blue",
                                     "Chinstrap": "red",
                                     "Gentoo": "green"}, title="Penguins are scattered")
st.plotly_chart(fig_scatter)

#This is our Map

##Here we us a lambda function to assign coordinates to the island
##I jitter the locations to make the maps look better.
import random
island_coords={"Biscoe":(-63.8,-63.4), "Dream":(-64.7, -62.9), "Torgersen":(-64.8,-64.1)}
df["latitude"]=df["island"].map(lambda x:island_coords[x][0]+ random.uniform(-0.1, 0.1))
df["longitude"]=df["island"].map(lambda x:island_coords[x][1]+ random.uniform(-0.1, 0.1))

fig_map=px.scatter_map(df,lat="latitude", lon="longitude",color="species", color_discrete_map={"Adelie": "blue",
                                     "Chinstrap": "red",
                                     "Gentoo": "green"}, title="This is a plot of penguins based on the color of their poop", zoom=5, map_style="open-street-map")
st.plotly_chart(fig_map)
