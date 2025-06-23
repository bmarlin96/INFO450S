import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("tips")

st.title("Tips Dataset Explorer 💵")

# Show data preview
st.write("Here's a preview of the data:")
st.dataframe(df.head())

# Column selector
numeric_cols = df.select_dtypes(include='number').columns
col = st.selectbox("Select a numeric column to plot:", numeric_cols)

# Plot
fig, ax = plt.subplots()
ax.hist(df[col], bins=20, edgecolor='black')
ax.set_title(f"Histogram of {col}")
st.pyplot(fig)
