import streamlit as st

st.title("💫 cats are the best")
st.write(
    "Yall i love cats lets start stanning cats guys and learn informatika hashtag slay -bi'sawesome"
)
st.image("IMG_4860.jpeg")



st.title("Aplikasi Rawr")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
