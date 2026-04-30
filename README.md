# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi (perguruan tinggi) yang memiliki komitmen untuk memberikan layanan pendidikan berkualitas kepada mahasiswanya. Namun, institusi menghadapi tantangan terkait retensi mahasiswa, di mana banyak mahasiswa yang berhenti sebelum menyelesaikan masa studinya. Upaya untuk meningkatkan angka kelulusan dan meminimalkan angka dropout menjadi prioritas strategis untuk menjaga kualitas dan keberlanjutan institusi.

### Permasalahan Bisnis

Jaya Jaya Institut menghadapi tantangan besar terkait tingginya tingkat mahasiswa yang tidak menyelesaikan pendidikannya (dropout). Hal ini berdampak sangat signifikan pada efektivitas pendidikan dan reputasi institusi. Oleh seban itu, saya membuat analisis terhadap institusi yang sedang membutuhkan sebuah sistem deteksi dini untuk mengidentifikasi mahasiswa yang berisiko tinggi berhenti kuliah agar pihak bimbingan konseling dapat memberikan penanganan secara tepat sasaran.

### Cakupan Proyek

Proyek ini mencakup pengembangan solusi analisis data end-to-end, yaitu:
* Melakukan Exploratory Data Analysis (EDA) untuk menemukan faktor-faktor utama (Red Flags) yang memicu mahasiswa dropout.  
* Membangun Dashboard Performa Siswa yang memberikan ringkasan eksekutif dan profil risiko mahasiswa bagi pihak manajemen.  
* Mengembangkan Model Klasifikasi (Random Forest) untuk memprediksi potensi status akhir mahasiswa (Dropout atau Graduate) dengan sistem skor risiko.

### Persiapan

* Sumber data: Dataset diunduh secara manual atau diambil langsung dari [database](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance), kemudian disimpan dalam file students_performance/data.csv. Berkas ini berisi data lengkap mengenai demografi, latar belakang pendidikan, status ekonomi, serta performa akademik mahasiswa.  

* Setup environment: Dikembangkan menggunakan Python di dalam virtual environment.  
    - Pustaka Utama: pandas, numpy, scikit-learn, matplotlib, seaborn, dan Streamlit.  
    - Langkah Pembuatan Environment (via Conda):
      1. Membuat environment baru: conda create --name student-performance python=3.9.  
      2. Mengaktifkan environment: conda activate student-performance.
      3. Menginstal library yang dibutuhkan: pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn==1.2.2 joblib==1.3.1 streamlit.  
    - IDE: Eksperimen data dilakukan melalui Jupyter Notebook

## Business Dashboard

Telah dibuat sebuah dashboard interaktif menggunakan Streamlit yang hanya memproses data final mahasiswa (Dropout dan Graduate) untuk memberikan analisis yang lebih tajam dan valid secara konsep.:  
* Tautan Prototype (Streamlit Cloud): [a590proyekakhirana.streamlit.app].

Executive Summary:
* Menampilkan metrik utama yang mencerminkan data final institusi.

* Analisis Faktor: Visualisasi distribusi status mahasiswa dan korelasi variabel kunci terhadap status kelulusan dengan label yang deskriptif.

Menjalankan Dashboard Metabase (Docker)
Silakan ikuti langkah-langkah di bawah ini untuk menjalankan environment Metabase menggunakan Docker.

1. Spesifikasi Environment
Versi Metabase: v0.49.13

File Database: metabase.db.mv.db (Sudah disertakan dalam root folder proyek).

2. Langkah-Langkah Menjalankan
   docker pull metabase/metabase:v0.49.13

   docker run -d -p 3000:3000 --name metabase_check metabase/metabase:v0.49.13

   docker cp metabase.db.mv.db metabase_check:/metabase.db/metabase.db.mv.db

   docker restart metabase_check

3. Akses Dashboard & Kredensial
   http://localhost:3000 (User: ana.rosyidah24@gmail.com / Pass: Rosyidah89).

## Menjalankan Sistem Machine Learning

Prototype sistem ini telah dideploy dan diintegrasikan ke dalam dashboard Streamlit untuk menyediakan layanan deteksi dini bagi mahasiswa.

* Link Prototype: https://a590proyekakhirana.streamlit.app/

Deployment Process
Prototype ini telah berhasil di-deploy melalui Streamlit Cloud Community dengan tahapan sebagai berikut:

1. Mengunggah seluruh source code proyek (termasuk folder model/ dan requirements.txt) ke repositori GitHub.

2. Melakukan login ke Streamlit Cloud dan mengintegrasikan repositori GitHub tersebut.


3. Melakukan deployment aplikasi agar dapat diakses secara publik oleh pengguna. lakukan langkah seperti pada vidio berikut https://www.youtube.com/watch?v=JL9xOs-G1hI

Cara Penggunaan
* Input: Pengguna memasukkan data akademik seperti status pembayaran SPP, status beasiswa, rata-rata nilai semester 1, status hutang, mata kuliah lulus semester 2, dan usia saat mendaftar pada menu "Student Risk Predictor".

* Output: Sistem akan mengeluarkan probabilitas risiko. Jika risiko > 70%, sistem akan memberikan label "RISIKO TINGGI" dengan peringatan berwarna merah.

Performa Model
*Berdasarkan revisi model terbaru yang fokus pada klasifikasi biner (Dropout vs Graduate), model berhasil mencapai performa sebagai berikut:

* Akurasi Model: 91% pada data pengujian.

* Metrik Kualitas: Model sangat tajam mengenali potensi dropout dengan skor precision dan recall yang seimbang di atas 80%, sehingga efektif sebagai sistem deteksi dini.

* Fitur Utama: Faktor paling berpengaruh terhadap prediksi adalah jumlah mata kuliah yang lulus di semester 2, rata-rata nilai semester 2, dan kelancaran pembayaran uang kuliah.

## Conclusion

Berdasarkan analisis, performa akademik di semester awal (khususnya jumlah mata kuliah yang lulus di semester 2) dan kelancaran finansial (status pembayaran SPP dan beasiswa) memiliki korelasi yang sangat kuat terhadap keputusan mahasiswa untuk bertahan atau dropout. Model Random Forest yang dibangun mampu memberikan skor risiko secara dinamis untuk membantu intervensi dini.

1. Analisis Data & Dashboard

   Dari hasil ulasan mendalam melalui EDA dan tampilan dashboard, kita bisa melihat pola yang jelas mengenai karakteristik mahasiswa yang cenderung mengalami dropout di Jaya Jaya Institut:

   * Kendala Finansial adalah "Red Flag" Utama: Data menunjukkan bahwa mahasiswa dengan status pembayaran SPP yang tidak lancar (Tuition_fees_up_to_date = 0) serta mereka yang memiliki hutang (Debtor = 1) memiliki angka dropout yang jauh lebih tinggi dibandingkan mahasiswa tanpa masalah administrasi.  

   * Performa Akademik di Semester Kedua: Keberhasilan melewati tahun pertama sangat krusial. Mahasiswa yang gagal meluluskan mata kuliah di semester 2 (Curricular_units_2nd_sem_approved) atau memiliki rata-rata nilai (Grade) rendah menunjukkan sinyal kuat akan segera berhenti kuliah.  

   * Profil Demografi: Usia saat mendaftar ternyata berpengaruh; mahasiswa yang masuk di usia yang lebih tua cenderung lebih rentan dropout dibanding mahasiswa usia reguler. Selain itu, secara statistik dalam dataset ini, mahasiswa laki-laki memiliki kecenderungan dropout yang lebih besar.

2. Performa Model Machine Learning

   Untuk membantu institusi melakukan pencegahan, model Machine Learning telah dikembangkan dengan hasil sebagai berikut:Performa Sangat Baik: 
   * Dengan menggunakan algoritma Random Forest Classifier, model kita berhasil mencapai tingkat Akurasi 91% pada data pengujian. Tidak hanya sekadar akurat secara total, model ini juga sangat tajam dalam mengenali mahasiswa yang akan dropout (skor precision dan recall di atas 80%), sehingga meminimalisir kesalahan prediksi.  
   * Faktor Penentu Prediksi: Saat model bekerja, tiga fitur utama yang paling dijadikan acuan dalam mengambil keputusan adalah:
   1. Jumlah mata kuliah yang berhasil lulus di semester 
   2. Rata-rata nilai akademik di semester 
   3. Status kelancaran pembayaran uang kuliah (SPP).

### Rekomendasi Action Items

1. Sistem Peringatan Dini Akademik:
Data menunjukkan bahwa kegagalan melewati tahun pertama adalah prediktor terkuat (Curricular_units_1st_sem_approved). Institusi harus menerapkan kebijakan "3-Strike Warning":

* Jika mahasiswa gagal meluluskan < 10 mata kuliah di semester 1, mereka secara otomatis didaftarkan dalam sistem pendampingan akademik wajib.

* Jika Grade semester 1 berada di bawah 11 (skala 0-20), mahasiswa diberikan akses ke kelas remedial/tutoring agar performa di semester 2 dapat diperbaiki.

2. Dukungan Finansial Terfokus:
Berdasarkan data, status Debtor dan ketidaklancaran pembayaran SPP berkorelasi signifikan dengan dropout.

* Proaktif: Institusi tidak menunggu mahasiswa drop, melainkan mengirimkan email pemberitahuan mengenai "Opsi Keringanan Biaya" bagi mahasiswa yang terdeteksi memiliki status Debtor = 1 di pertengahan semester.

* Skema: Menyediakan skema installment (cicilan) yang fleksibel bagi kelompok ini agar mereka tetap dapat fokus pada studi tanpa beban administratif yang menumpuk.

3. Pendampingan Mahasiswa Berisiko Tinggi (Predictor-based):
Menggunakan Student Risk Predictor yang telah dibangun, pihak BK (Bimbingan Konseling) akan mendapatkan laporan mingguan mengenai mahasiswa dengan skor risiko > 70%. Pihak BK akan melakukan deep interview untuk memahami apakah masalah utama mahasiswa adalah faktor internal (motivasi/akademik) atau eksternal (ekonomi/keluarga) untuk diberikan solusi yang presisi.
