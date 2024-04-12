import streamlit as st
import Home
import SimulasiDeposito
import SimulasiDPLK

navigation = st.sidebar.selectbox('Pilihan Halaman :', ('Simulasi Deposito', 'Simulasi DPLK'))

if navigation == 'Home':
    Home.run()
elif navigation == 'Simulasi DPLK':
    SimulasiDPLK.run()
else:
    SimulasiDeposito.run()
