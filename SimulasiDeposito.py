import streamlit as st

def calculate_deposit(NominalPenempatan, Tenor, SukuBunga, TarifPajak):
    # Hitung bunga
    bunga = NominalPenempatan * (SukuBunga / 100) * (Tenor / 12)
    # Hitung pajak
    pajak = bunga * (TarifPajak / 100)
    # Total yang diterima setelah dipotong pajak
    total_setelah_pajak = NominalPenempatan + bunga - pajak
    return bunga, pajak, total_setelah_pajak

def run():
    st.title('Simulasi Deposito')
    # Membuat form
    with st.form(key='form_parameters'):
        
        NominalPenempatan= st.number_input('Nominal Penemoatan', min_value=0, value=10000000, step =1000000, help= 'Nominal Penemoatan.')
        Tenor= st.number_input('Tenor', min_value=0, max_value=12, value=3, step =1, help= 'Tenor.')
        SukuBunga= st.number_input('Suku Bunga', min_value=0, max_value=100, value=2, step =1, help= 'Suku Bunga dalam %.')
        TarifPajak = st.number_input('Tarif Pajak (%)', min_value=0, max_value=100, value=10, step=1, help='Tarif pajak atas bunga deposito dalam persen.')
        
        submitted = st.form_submit_button('Hitung')

        if submitted:
            bunga, pajak, total_setelah_pajak = calculate_deposit(NominalPenempatan, Tenor, SukuBunga, TarifPajak)
            st.write(f"Total bunga yang akan Anda dapatkan adalah:") 
            st.write(int(bunga)) 
            st.write(f"Total pajak yang akan dipotong dari bunga adalah:")
            st.write(int(pajak))
            st.write(f"Total uang yang akan Anda terima setelah deposito berakhir adalah:")
            st.write(int(total_setelah_pajak))

if __name__ == "__main__":
    run()
