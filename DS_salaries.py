import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

 
st.write("""# This is an application about Data Science Salaries 2023 💸 """)

 
df = pd.read_csv("ds_salaries (1).csv")

 
st.write("### **Head of DataFrame**")
st.write("---")
st.write(df.head())

 
job_title_filter = st.sidebar.selectbox("Select Job Title", df['job_title'].unique())

 
filtered_df = df[df['job_title'] == job_title_filter]

 
st.write("## **Data Visualization**")
st.write("#### Salary Distribution by Job Title")

 
fig, ax = plt.subplots()
sns.histplot(filtered_df['salary_in_usd'], kde=True, bins=20, ax=ax)
ax.set_xlabel('Salary in USD')
ax.set_ylabel('Frequency')
st.pyplot(fig)

 
st.sidebar.write("### **Filter by Salary Currency**")
selected_currency = st.sidebar.radio("Select Salary Currency", df['salary_currency'].unique())

 
filtered_df_currency = df[df['salary_currency'] == selected_currency]

 
if st.button("Show Table"):
    st.write("You selected salary currency:", selected_currency)
    st.dataframe(filtered_df_currency)
else:
    pass

 
st.write("### **Bar Chart of Salaries in Selected Currency**")
chart_data = filtered_df_currency[['job_title', 'salary_in_usd']].copy()
chart_data['salary_in_usd'] = chart_data['salary_in_usd'].astype(float)

st.bar_chart(chart_data, x='job_title', y='salary_in_usd')

 
st.sidebar.write("### **Filter by Salary (USD)**")
salary_min = st.sidebar.slider('Minimum Salary', int(df['salary_in_usd'].min()), int(df['salary_in_usd'].max()), int(df['salary_in_usd'].min()))
salary_max = st.sidebar.slider('Maximum Salary', int(df['salary_in_usd'].min()), int(df['salary_in_usd'].max()), int(df['salary_in_usd'].max()))

 
st.sidebar.write("### **Select Job Title**")
job_title = st.sidebar.radio("Job Title", df['job_title'].unique())

 
filtered_df_salary = df[(df['job_title'] == job_title) & (df['salary_in_usd'] >= salary_min) & (df['salary_in_usd'] <= salary_max)]

if st.button("Show Experience Level Table"):
    genre = st.selectbox("Select Experience Level", df['experience_level'].unique())
    st.write("You selected:", genre)
    st.dataframe(df[df["experience_level"] == genre])
else:
    pass

 
st.sidebar.write("### **Salary Visualization (USD)**")
st.sidebar.line_chart(df["salary_in_usd"])

with st.sidebar:
    st.write("### **Echoed Code Example**")
    with st.echo():
        st.write("This code will be printed to the sidebar.")
    
    st.write("### **Spinner Example**")
    with st.spinner("Loading..."):
        time.sleep(5)  
    st.success("Done!")

fig, ax = plt.subplots()
sns.histplot(filtered_df_salary['salary_in_usd'], kde=True, bins=20, ax=ax)
ax.set_xlabel('Salary in USD')
ax.set_ylabel('Frequency')
st.pyplot(fig)


st.write("#### Salary vs Experience Level")
fig = px.scatter(filtered_df_salary, x='experience_level', y='salary_in_usd', color='experience_level',
                 title=f'Salary vs Experience Level for {job_title}')
st.plotly_chart(fig)

st.write("### **Conclusion**")
st.write("Explore and analyze data science salaries from 2023 with interactive visualizations.")
