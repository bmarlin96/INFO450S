import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import random
import seaborn as sns
import streamlit as st

##Setting a theme
st.set_page_config(
    page_title="Badgers Rock",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;  /* Dark Mode */
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    .css-1d391kg {
        background-color: #333333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


###Here we just want to introduce you to streamlit
st.title("Badgers Rock" )
###Bring in and clean the data
df=pd.read_csv('/content/badgers_dataset.csv')
df=df.dropna()

###Interactive Check boxes are helpful to give the user options
if st.checkbox("Please press if you want to see the data"):
    st.header("This is our data")
    st.dataframe(df)

 ####This is how we can write to our app
st.text("Penguins Rock")
st.write("Penguins Rock")
st.markdown("## Penguins Rock")

#Copy and Paste our First Box Plot
#Notice how we use st.plotly_chart
df['island'].value_counts().reset_index()
badger_counts=df['island'].value_counts().reset_index()
badger_counts.columns=["island","count"]
fig=px.bar(badger_counts,x="island",y="count",color="island",color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig)

#Lets look at the stacked barchart
fig=px.bar(df,x="island",color="sex",title="penguin count by sex",barmode="stack",color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)

###We can assign a selectbox to a figure here we make the select box
box_metric=st.selectbox("Choose the measurement to display", ["weight_kg","snout_length_mm", "tail_length_mm"])

###Here we connect it to a box plot (notice our y value is the selectbox objkect - also notice that colors are a pain in the butt)
fig=px.box(df,x="species",y=box_metric, color_discrete_sequence=["blue"],title="Body Mass Distribution By Species")
st.plotly_chart(fig)

###Just bring in the stacked bar chart and notice the filtering!
fig = px.histogram(df, x="weight_kg", color="species",
                   title="Body Mass Distribution by Species",
                   color_discrete_map={"American Badger": "blue", "European Badger": "red", "Honey Badger": "green"})
fig.update_layout(bargap=0.1) # Update layout to set bargap
fig.show()
st.plotly_chart(fig)


#####Lets make scatter plots and a map and show them side by side.
###We use DF filtered so we can make multiselect
selected_species = st.multiselect("Select species:", df["species"].unique())
df_filtered = df[df["species"].isin(selected_species)]
fig_scatter=px.scatter(df_filtered,x="weight_kg",y="snout_length_mm", color="species", size="weight_kg",title="Penguins are scattered")
#st.plotly_chart(fig_scatter)


##Here we us a lambda function to assign coordinates to the island
##I jitter the locations to make the maps look better.
island_coords={"Biscoe":(-63.8,-63.4), "Dream":(-64.7, -62.9), "Torgersen":(-64.8,-64.1)}
df_filtered["latitude"]=df_filtered["island"].map(lambda x:island_coords[x][0]+ random.uniform(-0.1, 0.1))
df_filtered["longitude"]=df_filtered["island"].map(lambda x:island_coords[x][1]+ random.uniform(-0.1, 0.1))

fig_map=px.scatter_map(df_filtered,lat="latitude", lon="longitude",color="species",title="This is a plot of penguins based on the color of their poop", zoom=5, map_style="open-street-map")
#st.plotly_chart(fig_map)
container = st.container()
with container:
    col1,col2=st.columns(2)
    with col1:
        st.plotly_chart(fig_scatter,key='scatter_chart')
    with col2:
        st.plotly_chart(fig_map,key='map_chart')

