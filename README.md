# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jelaskan latar belakang bisnis dari perushaan tersebut.

Jaya Jaya Institut merupakan institusi pendidikan tinggi (perguruan tinggi) yang memiliki komitmen untuk memberikan layanan pendidikan berkualitas kepada mahasiswanya. Namun, institusi menghadapi tantangan terkait retensi mahasiswa, di mana banyak mahasiswa yang berhenti sebelum menyelesaikan masa studinya. Upaya untuk meningkatkan angka kelulusan dan meminimalkan angka dropout menjadi prioritas strategis untuk menjaga kualitas dan keberlanjutan institusi.

### Permasalahan Bisnis
Tuliskan seluruh permasalahan bisnis yang akan diselesaikan.

Permasalahan utama yang ingin diselesaikan adalah tingginya tingkat dropout mahasiswa yang mencapai 32,1%. Hal ini berdampak pada efektivitas pendidikan dan reputasi institusi. Institusi membutuhkan cara untuk mendeteksi sedini mungkin mahasiswa yang memiliki risiko tinggi untuk berhenti kuliah agar bimbingan konseling dapat diberikan secara tepat sasaran.

### Cakupan Proyek
Tuliskan cakupan proyek yang akan dikerjakan.

Proyek ini mencakup pengembangan solusi analisis data end-to-end, yaitu:
* Melakukan Exploratory Data Analysis (EDA) untuk menemukan faktor-faktor utama (Red Flags) yang memicu mahasiswa dropout, seperti faktor ekonomi dan performa akademik semester awal.  
* Membangun Dashboard Performa Siswa yang memberikan ringkasan eksekutif dan profil risiko mahasiswa bagi pihak manajemen.  
* Mengembangkan Model Klasifikasi (Random Forest) untuk memprediksi status mahasiswa (Dropout, Enrolled, atau Graduate) dengan sistem skor risiko.

### Persiapan

* Sumber data: Dataset berasal dari file students_performance/data.csv yang berisi data demografi, latar belakang pendidikan, status ekonomi, dan performa akademik mahasiswa pada semester 1 dan 2.  

* Setup environment: Menggunakan bahasa pemrograman Python dengan pustaka utama: pandas untuk pengolahan data, scikit-learn untuk pemodelan, matplotlib/seaborn untuk visualisasi, serta Streamlit untuk antarmuka dashboard.  

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

Telah dibuat sebuah dashboard interaktif menggunakan Streamlit.  Executive Summary: 
* Menampilkan metrik utama seperti Total Mahasiswa (4.424), Dropout Rate (32,1%), dan Graduate Rate (49,9%).  
* Analisis Faktor: Visualisasi distribusi status mahasiswa dan korelasi antara penerimaan beasiswa terhadap status kelulusan.  
* Akses Dashboard: [a590proyekakhirana.streamlit.app].

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

Prototype sistem ini diintegrasikan ke dalam dashboard Streamlit pada menu "Student Risk Predictor".  

* Cara Menjalankan: Pengguna memasukkan data akademik seperti status pembayaran SPP, status beasiswa, rata-rata nilai semester 1, status hutang, mata kuliah lulus semester 2, dan usia saat mendaftar.  

* Hasil: Sistem akan mengeluarkan probabilitas risiko. Jika risiko > 70%, sistem akan memberikan label "RISIKO TINGGI" dengan peringatan berwarna merah.

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

Berdasarkan analisis, performa akademik di semester awal (khususnya jumlah mata kuliah yang lulus di semester 2) dan kelancaran finansial (status pembayaran SPP dan beasiswa) memiliki korelasi yang sangat kuat terhadap keputusan mahasiswa untuk bertahan atau dropout. Model Random Forest yang dibangun mampu memberikan skor risiko secara dinamis untuk membantu intervensi dini.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

Beberapa tindakan yang disarankan bagi Jaya Jaya Institut:
1. Sistem Peringatan Dini Akademik: Memberikan pendampingan bimbingan konseling khusus bagi mahasiswa yang memiliki nilai rata-rata rendah atau jumlah kelulusan mata kuliah di bawah standar pada semester 1.  
2. Dukungan Finansial Terfokus: Memperluas program beasiswa atau memberikan skema cicilan bagi mahasiswa yang terdeteksi seb
