import streamlit as st
import joblib

model = joblib.load('flowerclassifier.pkl')

st.title('My app')
st.write('enter flower measurment to pridict the iris species')

sepal_length=st.number_input('Enter sepal length')
sepal_width=st.number_input('Enter sepal width')
petal_length=st.number_input('Enter petal length')
petal_width=st.number_input('Enter petal width')

if st.button('predict'):
    newdata = [[sepal_length,sepal_width,petal_length,petal_width]]
    pred = model.predict(newdata)
    st.write(pred)


    if pred == 0:
        st.success('the predicted class is setosa')
    elif pred == 1:
         st.success('the predicted class is versicolor')
    else:
        st.success('the predicted class is virginica')
    
