import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.set_page_config(page_title="Book Recommendation", page_icon="📚", layout="wide")

popular_df = pickle.load(open('popular_books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
book_titles = list(pt.index.values)

book_name=list(popular_df['Book-Title'].values),
author=list(popular_df['Book-Author'].values),
image=list(popular_df['Image-URL-M'].values),
votes=list(popular_df['num_of_rating'].values),
rating=list((round(popular_df['avg_rating'], 2).values))


def recommend(user_input):
    # user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    return data


st.title('Book Recommendation System')
user_input = st.selectbox('Please type or select a book from the dropdown to get recommendations', book_titles)
if st.button('Show Recommendation'):
    st.header('Recommendations for the book:  {}'.format(user_input))
    data = recommend(user_input)
    cols = st.columns(4)
    for c in range(len(cols)):
        with cols[c]:
            st.image(data[c][2])
            st.write(data[c][0])
            st.write(data[c][1])

st.markdown('___')
st.markdown('___')
st.title('Top rated books')
d=0
for i in range(12):
    cols = st.columns(4)
    for c in range(4):
        with cols[c]:
                        st.image(image[0][d])
                        st.write(book_name[0][d])
                        st.write(author[0][d])
                        st.write('avg rating', rating[d])
                        st.write('total votes', votes[0][d])
        d=d+1
    #d = d+4



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
st.markdown(hide_st_style, unsafe_allow_html=True)
