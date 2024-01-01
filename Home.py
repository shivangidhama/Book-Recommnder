# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 22:18:33 2023

@author: aviyansh
"""

import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(
    page_title="Book-recommender",page_icon="📖",)

def recommend_book(book):
    index = np.where(pt.index==book)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data = []
    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    return data


books=pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

st.title("Book Recommender System")

book_list = pt.index.values
option=st.selectbox("Select or type a book to recommend",book_list
    )
if st.button("Recommend Me"):
    movie = recommend_book(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(movie[0][2])
        st.text(movie[0][0])
        st.text(movie[0][1])  
    with col2:
        st.image(movie[1][2])
        st.text(movie[1][0])
        st.text(movie[1][1])
    with col3:
        st.image(movie[2][2])
        st.text(movie[2][0])
        st.text(movie[2][1])
    with col4:
        st.image(movie[3][2])
        st.text(movie[3][0])
        st.text(movie[3][1])
    with col5:
        st.image(movie[4][2])
        st.text(movie[4][0])
        st.text(movie[4][1])





