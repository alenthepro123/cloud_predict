

# In[4]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    df = pd.read_excel("C://Users//DATA SCIENCE LAB 20//Desktop//streamlit//Historical NBA Performance.xlsx")
    return df

df = load_data()

# Set page configuration
st.set_page_config(
    page_title="NBA Match Prediction",
    page_icon="🏀",
    layout="wide"
)


st.markdown(
    """
    <style>
    body {
        background-image: url("https://espnpressroom.com/us/files/2021/06/NBAESPN_2_Header_1600-780x470.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.title('Team Selection')
team1 = st.sidebar.selectbox('Select the first team', df['Team'].unique())
team2 = st.sidebar.selectbox('Select the second team', df['Team'].unique())


def predict_winner(team1, team2):
    team1_data = df[df['Team'] == team1]
    team2_data = df[df['Team'] == team2]
    team1_win_rate = team1_data['Winning Percentage'].mean()
    team2_win_rate = team2_data['Winning Percentage'].mean()
    
    if team1_win_rate > team2_win_rate:
        return team1
    elif team1_win_rate < team2_win_rate:
        return team2
    else:
        return "Both teams have the same winning percentage"


st.title('NBA Match Prediction')
if team1 != team2:
    winner = predict_winner(team1, team2)
    st.write(f"The predicted winner between {team1} and {team2} is: **{winner}**")
else:
    st.write("Please select two different teams.")


st.title('Historical Winning Percentages')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Team', y='Winning Percentage', ax=ax)
plt.xticks(rotation=90)
plt.xlabel('Team')
plt.ylabel('Winning Percentage')
st.pyplot(fig)





# In[ ]:




