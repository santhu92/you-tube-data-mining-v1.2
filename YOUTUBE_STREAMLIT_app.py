import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
import subprocess
import sys
import os
from app import engine
cwd = os.getcwd()


st.title("Youtube Data Scrapping")

st.write("Please enter Channel Id with comma seperated")
ytb_channel_id = st.text_input("channel_ids")

button = st.button("Click to start harvesting")
if button:
    f = open("temp.txt", "w")
    st.write(ytb_channel_id)
    f.write(ytb_channel_id)
    f.close()
    subprocess.run([f"{sys.executable}", cwd + "\\ytb_data_collection.py"])
st.sidebar.title("you tube data insights ")
button1 = st.sidebar.button("Upload to MYSQL DB")
if button1:
    subprocess.run([f"{sys.executable}", cwd + "\\ytb_mng_to_mysql.py"])


Selected_channel_id = ytb_channel_id.split(",")
raw_data_option = st.sidebar.selectbox('select the harvested channel, in which you want to see raw data', (Selected_channel_id))
button2 = st.sidebar.button("display raw data")
if button2:
    cwd = os.getcwd()
    pathfile = cwd + "\\" + raw_data_option.strip()
    st.write('You selected:', raw_data_option + ".json")
    file = open(fr"{pathfile}.json", "r")
    data = file.read()
    st.write(data)

try:

    df_sql_More_comments = pd.read_sql_query("Select * from more_comments;", con=engine)

    df_sql_Channel_that_published_video_in_year2022s = pd.read_sql_query(
        "SELECT * from channel_that_published_video_in_year2022;", con=engine)

    df_sql_most_liked_videos = pd.read_sql_query("SELECT * from most_liked_videos;", con=engine)

    df_sql_channel = pd.read_sql_query("SELECT channel_views, channel_name from channel;", con=engine)

    df_sql_videos_basic_info = pd.read_sql_query("SELECT * from videos_Basic_info;", con=engine)

    df_sql_Least_Watched_videos = pd.read_sql_query("SELECT * from least_Watched_videos;", con=engine)

    df_sql_Top_videos = pd.read_sql_query("SELECT * from top_videos;", con=engine)

    df_sql_video_comment_count = pd.read_sql_query("SELECT comment_count, video_name from video;", con=engine)

    df_sql_channel_id_info = pd.read_sql_query("SELECT * from channel_id_info;", con=engine)
except BaseException as e:
    pass


option = st.sidebar.selectbox('Search By', (
    'df_sql_More_comments', 'df_sql_Channel_that_published_video_in_year2022s', 'df_sql_most_liked_videos',
    'df_sql_channel', 'df_sql_videos_basic_info', 'df_sql_Least_Watched_videos', 'df_sql_Top_videos',
    'df_sql_video_comment_count'))
button1 = st.sidebar.button("Click to proceed")
if button1:
    if option == 'df_sql_More_comments':
        st.write(df_sql_More_comments)
    elif option == 'df_sql_Channel_that_published_video_in_year2022s':
        st.write(df_sql_Channel_that_published_video_in_year2022s)
    elif option == 'df_sql_most_liked_videos':
        st.write(df_sql_most_liked_videos)
    elif option == 'df_sql_channel':
        st.write(df_sql_channel)
    elif option == 'df_sql_videos_basic_info':
        st.write(df_sql_videos_basic_info)
    elif option == 'df_sql_videos_basic_info':
        st.write(df_sql_videos_basic_info)
    elif option == 'df_sql_Least_Watched_videos':
        st.write(df_sql_Least_Watched_videos)
    elif option == 'df_sql_Top_videos':
        st.write(df_sql_Top_videos)
    elif option == 'df_sql_video_comment_count':
        st.write(df_sql_video_comment_count)
st.sidebar.text("channels and their total video count exist in Data base")
try:
    st.sidebar.write(df_sql_channel_id_info)
except BaseException as e:
    pass