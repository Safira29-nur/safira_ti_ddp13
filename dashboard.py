import streamlit as st

st.title("halaman kalkulator")

def total():
    total_hitung = sum(t['Jumlah']
                       for t in st.session_state['total_semua']
                       if t ['Tipe'] == 'menghitung')
    return total_hitung

total_semua = st.session_state['total_semua']
total_hitung = total()

st.metric("total perhitungan jarak adalah", f"km. {total_hitung}")