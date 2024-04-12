import streamlit as st

def calculate_pension(usia_saat_ini, usia_pensiun, setoran_awal, iuran_rutin, frekuensi_iuran):
    tahun_pensiun = usia_pensiun - usia_saat_ini
    if frekuensi_iuran == 'bulanan':
        periode_iuran = tahun_pensiun * 12
    elif frekuensi_iuran == '3 bulan':
        periode_iuran = tahun_pensiun * 4
    elif frekuensi_iuran == '6 bulan':
        periode_iuran = tahun_pensiun * 2
    elif frekuensi_iuran == 'tahunan':
        periode_iuran = tahun_pensiun
    else:
        return 0
    
    TotalDana = setoran_awal
    for i in range(periode_iuran):
        TotalDana += iuran_rutin
        if TotalDana > 50000000:
            TotalDana += (TotalDana - 50000000) * 0.05

    return TotalDana

def run():
    st.title('Simulasi Dana Pensiun Lembaga Keuangan')

    with st.form(key='form_parameters'):
        
        usia_saat_ini = st.number_input('Usia Saat Ini (tahun)', min_value=0, value=30, step=1, format="%d", help='Usia Anda saat ini.')
        usia_pensiun = st.number_input('Usia Pensiun (tahun)', min_value=0, value=60, step=1, format="%d", help='Usia Anda saat pensiun.')
        setoran_awal = st.number_input('Setoran Awal (Rp)', min_value=0, value=1000000, step=100000, format="%d", help='Setoran awal Anda.')
        iuran_rutin = st.number_input('Iuran Rutin (Rp)', min_value=0, value=50000, step=10000, format="%d", help='Iuran rutin Anda setiap periode.')
        frekuensi_iuran = st.selectbox('Frekuensi Iuran', ['bulanan', '3 bulan', '6 bulan', 'tahunan'], help='Pilih frekuensi iuran Anda.')

        submitted = st.form_submit_button('Hitung')

        if submitted:
            total_iuran = calculate_pension(usia_saat_ini, usia_pensiun, setoran_awal, iuran_rutin, frekuensi_iuran)
            st.write(f"Total iuran yang diperlukan hingga pensiun adalah: Rp {int(total_iuran):,}")

if __name__ == "__main__":
    run()
