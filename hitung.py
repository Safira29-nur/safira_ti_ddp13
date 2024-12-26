import streamlit as st

st.title("halaman menghitung")

#form menabung
with st.form("menghitung"):
    nama = st.text_input("nama anda")
    Jumlah = st.number_input("jumlah (km)")
    tanggal = st.date_input("tanggal")
    waktu = st.time_input("waktu")
    button = st.form_submit_button(label ="menghitung")
    if button and Jumlah >= 1000:
        st.session_state['total_semua'].append({
            "Tipe" : "menghitung",
            "Jumlah" : Jumlah
        })
        st.success(f"anda berhasil menempuh jarak sebesar {Jumlah}")
    else:
        st.error("jarak tempuh kurang")