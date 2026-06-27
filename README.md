# 🧬 GC Content Analyzer

Aplikasi bioinformatika berbasis web yang dirancang untuk menganalisis distribusi konten GC (*Guanine-Cytosine*) di dalam sekuens nukleotida secara cepat, akurat, dan interaktif.

---

## Fitur Utama
* **Multi-Format Support:** Mendukung pembacaan file sekuens standar seperti **FASTA, FASTQ, dan TXT**.
* **Visualisasi Interaktif:** Menampilkan grafik persentase konten GC yang bersih dan mudah dipahami.
* **Ekspor Data:** Hasil analisis dapat diunduh langsung dalam format laporan data (CSV).
* **Antarmuka Modern:** Tampilan minimalis yang responsif dengan latar belakang bertema animasi DNA 3D.

---

## Struktur Project
Berikut adalah susunan direktori dan file di dalam project ini:

```text
gc-content-analyzer/
│
├── static/                
│   ├── css/
│   │   └── style.css        
│   └── images/
│       └── dna_bg.png       
│
├── templates/               
│   └── index.html           
│
├── app.py                   
├── requirements.txt         
└── README.md                