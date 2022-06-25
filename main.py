import pickle
import streamlit as st 
import numpy as np

populer_df = pickle.load(open('populer.pkl','rb'))
simalarity_score = pickle.load(open('similarity.pkl','rb'))
books = pickle.load(open('booksr.pkl','rb'))
table = pickle.load(open('table.pkl','rb'))

def recommend(book_name):
    
    index = np.where(table.index==book_name)[0][0]
    
    distances = simalarity_score[index]
    similar_items = sorted(list(enumerate(simalarity_score[index])),key=lambda x:x[1],reverse=True)[1:7]
    
    item = []
    item2 = []
    item3=[]
    for i in similar_items:
        temp_df = books[books['Book-Title']== table.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        
    for j in similar_items:
        temp_df1 = books[books['Book-Title']== table.index[j[0]]]
        item2.extend(list(temp_df1.drop_duplicates('Book-Title')['Book-Author'].values))

    for k in similar_items:
        temp_df2 = books[books['Book-Title']== table.index[k[0]]]
        item3.extend(list(temp_df2.drop_duplicates('Book-Title')['Image-URL-M'].values))
    

    return item,item2,item3
    

st.title('Book Recommend System','That Recommend books based on your selection ')

if st.button('Suggest Me Some Trending Books'):



    col1,col2,col3,col4,col5= st.columns(5)
    
    with col1:
        for i in range(5,len(populer_df),10):
            st.text(list(populer_df['Book-Title'])[i-5])
            st.image(list(populer_df['Image-URL-M'])[i-5],caption='by - '+list(populer_df['Book-Author'])[i-5])
            st.text(list(populer_df['Book-Title'])[i])
            st.image(list(populer_df['Image-URL-M'])[i],caption='by - '+list(populer_df['Book-Author'])[i])
    with col2:
        for i in range(6,len(populer_df),10):
            st.text(list(populer_df['Book-Title'])[i-5])
            st.image(list(populer_df['Image-URL-M'])[i-5],caption='by - '+list(populer_df['Book-Author'])[i-5])
            st.text(list(populer_df['Book-Title'])[i])
            st.image(list(populer_df['Image-URL-M'])[i],caption='by - '+list(populer_df['Book-Author'])[i])
    with col3:
        for i in range(7,len(populer_df),10):
            st.text(list(populer_df['Book-Title'])[i-5])
            st.image(list(populer_df['Image-URL-M'])[i-5],caption='by - '+list(populer_df['Book-Author'])[i-5])
            st.text(list(populer_df['Book-Title'])[i])
            st.image(list(populer_df['Image-URL-M'])[i],caption='by - '+list(populer_df['Book-Author'])[i])
    with col4:
        for i in range(8,len(populer_df),10):
            st.text(list(populer_df['Book-Title'])[i-5])
            st.image(list(populer_df['Image-URL-M'])[i-5],caption='by - '+list(populer_df['Book-Author'])[i-5])
            st.text(list(populer_df['Book-Title'])[i])
            st.image(list(populer_df['Image-URL-M'])[i],caption='by - '+list(populer_df['Book-Author'])[i])
    with col5:
        for i in range(9,len(populer_df),10):
            st.text(list(populer_df['Book-Title'])[i-5])
            st.image(list(populer_df['Image-URL-M'])[i-5],caption='by - '+list(populer_df['Book-Author'])[i-5])
            st.text(list(populer_df['Book-Title'])[i])
            st.image(list(populer_df['Image-URL-M'])[i],caption='by - '+list(populer_df['Book-Author'])[i])   

st.text('( or )') 
a = st.selectbox('Select a book',options=table.index)



if st.button("Recommend Me Book Based On My Selected Book"):
    names,Author,link = recommend(a)
    
    col11, col21, col31  = st.columns(3)
    
    with col11:
        st.text(names[0])
        st.image(link[0],caption ='by - '+Author[0])
        st.text(names[3])
        st.image(link[3],caption ='by - '+Author[3])
    with col21:
        st.text(names[1])
        st.image(link[1],caption ='by - '+Author[1])
        st.text(names[4])
        st.image(link[4],caption ='by - '+Author[4])
    with col31:
        st.text(names[2])
        st.image(link[2],caption ='by - '+Author[2])
        st.text(names[5])
        st.image(link[5],caption ='by - '+Author[5])

