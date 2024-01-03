import streamlit as st
import pandas as pd
import numpy as np
from st_files_connection import FilesConnection
from google.cloud import storage
import os
from recommendation import get_recommendations
import io


# Set the environment variable for Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"


data = pd.read_csv('data.csv')
client = storage.Client()
bucket = client.get_bucket("streamlitmovies-bucket")
blob = bucket.get_blob("embd-18-20k.npy")
# Download the content of the blob as bytes
blob_content = blob.download_as_bytes()
# # Convert the content to a NumPy array
np_array = np.load(io.BytesIO(blob_content))

def main():
    st.title('Movie Recommender System')

    movie_list = data['title'][18000:20000].values
    movie_index =  data.index.tolist()

    selected_index = st.selectbox("Type and select your favorite movie", range(len(movie_list)), format_func=lambda i: movie_index[i])

    if st.button("Show Recommendation"):
        st.write(selected_index)
        st.write(np_array[selected_index])

        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.write("Film 1")
            
            with st.container(border=True):
                st.write("Film 2")

        with col2:
            with st.container(border=True):
                st.write("Film 1")

            with st.container(border=True):
                st.write("Film 2")

        st.snow()
    

# Run the Streamlit app
if __name__ == '__main__':
    main()
