import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load Model dan Metadata
@st.cache_resource
def load_model():
    model_path = 'model/model_jaya_jaya_institut.joblib'
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"File model tidak ditemukan di {model_path}. Pastikan folder 'model' sudah diunggah ke GitHub.")
        st.stop()

saved_data = load_model()
model = saved_data['model']
features = saved_data['features']

# --- SIDEBAR: Filter & Navigasi ---
st.sidebar.title("Jaya Jaya Institut")
menu = st.sidebar.selectbox("Pilih Menu", ["Executive Summary", "Student Risk Predictor"])

# --- MENU 1: EXECUTIVE SUMMARY ---
if menu == "Executive Summary":
    st.title("📊 Dashboard Performa Siswa")
    
    if os.path.exists('students_performance/data.csv'):
        df_raw = pd.read_csv('students_performance/data.csv', sep=';')
        df_raw['Status'] = df_raw['Status'].str.strip()
        
        # PERBAIKAN TOTAL: Meniadakan status 'Enrolled' sesuai saran reviewer
        # Kita hanya menggunakan df_model untuk seluruh ringkasan dan grafik
        df_model = df_raw[df_raw['Status'] != 'Enrolled'].copy()
        
        total_final = len(df_model)
        dropout_rate = (df_model['Status'] == 'Dropout').mean()
        graduate_rate = (df_model['Status'] == 'Graduate').mean()

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Mahasiswa (Lulus & Dropout)", f"{total_final:,}")
        with col2:
            st.metric("Dropout Rate", f"{dropout_rate:.1%}")
        with col3:
            st.metric("Graduate Rate", f"{graduate_rate:.1%}")

        st.divider()
        st.subheader("Analisis Faktor Utama (Data Latih Model)")
        gra1, gra2 = st.columns(2)

        with gra1:
            # PERBAIKAN: Grafik pie hanya menunjukkan Dropout vs Graduate
            st.write("**Proporsi Status Akhir Mahasiswa**")
            fig_pie, ax_pie = plt.subplots()
            status_counts = df_model['Status'].value_counts()
            ax_pie.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
            st.pyplot(fig_pie)

        with gra2:
            # PERBAIKAN: Grafik bar hanya membandingkan Dropout vs Graduate terhadap Beasiswa
            st.write("**Status Akhir vs Beasiswa**")
            df_plot = df_model.copy()
            df_plot['Scholarship_holder'] = df_plot['Scholarship_holder'].map({0: 'Bukan Penerima', 1: 'Penerima Beasiswa'})
            
            fig_bar, ax_bar = plt.subplots(figsize=(8, 6))
            sns.countplot(data=df_plot, x='Scholarship_holder', hue='Status', ax=ax_bar)
            
            for p in ax_bar.patches:
                if p.get_height() > 0:
                    ax_bar.annotate(f'{int(p.get_height())}', 
                                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                                    ha = 'center', va = 'center', 
                                    xytext = (0, 9), 
                                    textcoords = 'offset points')
            
            ax_bar.set_ylim(0, df_plot['Status'].value_counts().max() + 500)
            st.pyplot(fig_bar)
    else:
        st.info("File data.csv tidak ditemukan di folder students_performance/.")

# --- MENU 2: STUDENT RISK PREDICTOR ---
elif menu == "Student Risk Predictor":
    st.header("🔍 Sistem Deteksi Dini Risiko Dropout")
    st.write("Sistem ini melakukan inferensi untuk memprediksi kemungkinan status akhir siswa di masa depan.")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            tuition = st.selectbox("Pembayaran SPP Lancar?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
            scholarship = st.selectbox("Penerima Beasiswa?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
            sem1_grade = st.number_input("Rata-rata Nilai Sem 1", 0.0, 20.0, 12.0)
        with col2:
            debtor = st.selectbox("Memiliki Hutang?", [1, 0], format_func=lambda x: "Ya" if x==1 else "Tidak")
            sem2_approved = st.number_input("Mata Kuliah Lulus Sem 2", 0, 20, 5)
            age = st.number_input("Usia saat Daftar", 17, 60, 20)

        submit = st.form_submit_button("Analisis Risiko")

    if submit:
        input_data = pd.DataFrame([[0]*len(features)], columns=features)
        input_data['Tuition_fees_up_to_date'] = tuition
        input_data['Scholarship_holder'] = scholarship
        input_data['Curricular_units_1st_sem_grade'] = sem1_grade
        input_data['Debtor'] = debtor
        input_data['Curricular_units_2nd_sem_approved'] = sem2_approved
        input_data['Age_at_enrollment'] = age

        classes_list = list(model.classes_)
        try:
            dropout_idx = classes_list.index(0) 
            probability = model.predict_proba(input_data)[0][dropout_idx]

            st.divider()
            if probability > 0.7:
                st.error(f"⚠️ RISIKO TINGGI: Mahasiswa ini berpeluang {probability:.2%} untuk Dropout.")
                st.info("Rekomendasi: Berikan intervensi akademik atau finansial segera.")
            else:
                # Menampilkan potensi kelulusan (Graduate) sebagai hasil inferensi positif
                st.success(f"✅ RISIKO RENDAH: Mahasiswa berpeluang {1-probability:.2%} untuk lulus (Graduate).")
        except ValueError:
            st.error("Terjadi kesalahan pada mapping label model. Pastikan model menggunakan label biner (0: Dropout, 1: Graduate).")