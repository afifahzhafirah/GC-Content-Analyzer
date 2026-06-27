# GC Content Analyzer

Aplikasi bioinformatika berbasis web yang dirancang menggunakan Python dan Flask untuk menganalisis distribusi konten GC (*Guanine-Cytosine*) di dalam sekuens nukleotida dengan format FASTA maupun FASTQ.

---

## Fitur Utama
* **Multi-Format Support:** Mendukung pembacaan file sekuens standar seperti **FASTA, FASTQ, dan TXT**.
* **Visualisasi Interaktif:** Menampilkan grafik persentase konten GC yang bersih dan mudah dipahami.
* **Ekspor Data:** Hasil analisis dapat diunduh langsung dalam format laporan data (CSV).
* **Antarmuka Modern:** Tampilan minimalis yang responsif dengan latar belakang bertema animasi DNA 3D.

---
# Teknologi yang Digunakan

- Python
- Flask
- HTML
- CSS
- Matplotlib

---

## Struktur Project
Berikut adalah susunan direktori dan file di dalam project ini:

```text
GC-Content-Analyzer/
│
├── data/                
│   ├── sample.fasta
│   
├── outputs/                
│   ├── hasil_gc_content.csv
│
├── src/                
│   ├── __init__.py
│   ├── csv_exporter.py
│   ├── gc_analyzer.py
│   ├── sequence_parser.py       
│   └── sequence_record.py
│    
├── static/                
│   ├── dna_bg.png
│   ├── style.css        
│
├── templates/               
│   └── index.html           
│
├── README.md                  
├── app.py          
└── requirements.txt
```
---
       
# Cara Menjalankan Program
1. Clone repository

```bash
git clone https://github.com/afifahzhafirah/GC-Content-Analyzer.git
```

2. Masuk ke folder project

```bash
cd GC-Content-Analyzer
```

3. Install library

```bash
pip install -r requirements.txt
```

4. Jalankan server aplikasi

```bash
python app.py
```

5. Buka browser

```
http://127.0.0.1:5000
```
---

# Hasil Program

Aplikasi ini akan menghasilkan output berupa:
1. **Ringkasan Hasil Analisis (Summary)** dari sekuens yang dimasukkan.
2. **Daftar sekuens dengan persentase tertinggi** (Top 3 GC Content).
3. **Tabel Seluruh Sekuens** yang berisi rincian lengkap tiap baris data.
4. **Grafik GC Content** untuk mempermudah perbandingan visual.
5. **File Hasil Analisis (.csv)** yang siap diunduh.

---
