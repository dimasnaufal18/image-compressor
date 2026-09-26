# 🖼️ Image Compressor

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-PIL-FFD43B?logo=python&logoColor=black)](https://python-pillow.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)](#)

**Image Compressor** adalah tool sederhana berbasis **Python CLI** untuk mengkompres gambar dengan cepat dan ringan. Tool ini mendukung berbagai format gambar umum, menyediakan pengaturan kualitas dari **1–100**, serta dapat mengonversi gambar secara otomatis ke format **JPEG**.

> 💡 **Tujuan project:** mengurangi ukuran file gambar agar lebih hemat ruang penyimpanan dan lebih mudah digunakan untuk kebutuhan web, dokumentasi, maupun berbagi file, dengan tetap mempertahankan kualitas visual yang baik.

![Image Compressor](https://dummyimage.com/1200x400/1f2937/ffffff&text=Image+Compressor+-+Python+CLI)

---

## 📚 Daftar Isi

- [✨ Fitur](#-fitur)
- [🛠️ Teknologi](#️-teknologi)
- [📦 Instalasi](#-instalasi)
- [🚀 Cara Pakai](#-cara-pakai)
- [📊 Contoh Hasil](#-contoh-hasil)
- [📁 Struktur Project](#-struktur-project)
- [⚙️ Konfigurasi](#️-konfigurasi)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Kontribusi](#-kontribusi)
- [👤 Author](#-author)
- [📄 Lisensi](#-lisensi)

---

## ✨ Fitur

- 🗜️ Mengkompres gambar **JPG, JPEG, PNG**, dan format umum yang didukung Pillow.
- 🎚️ Mengatur tingkat kualitas gambar dari **1 hingga 100**.
- 🔄 Mengonversi gambar secara otomatis ke **JPEG** untuk output.
- 📉 Menampilkan **persentase penghematan ukuran file** setelah proses kompresi.
- ⚡ Ringan dan cepat untuk penggunaan sehari-hari.
- 💻 Dapat digunakan melalui **Command Line Interface (CLI)**.
- 📦 Mendukung **batch processing** untuk memproses beberapa gambar.
- 🧩 Menggunakan library **Pillow (PIL)** yang populer dan mudah dipasang.
- 🖼️ Cocok untuk kebutuhan sederhana seperti optimasi gambar sebelum diunggah atau dibagikan.

---

## 🛠️ Teknologi

| Teknologi | Versi | Kegunaan |
|---|---|---|
| **Python** | 3.8+ | Bahasa pemrograman utama |
| **Pillow** | Terbaru yang kompatibel | Membaca, memproses, mengonversi, dan menyimpan gambar |
| **CLI** | Built-in | Antarmuka untuk menjalankan tool melalui terminal |
| **MIT License** | — | Lisensi open-source project |

---

## 📦 Instalasi

Ikuti langkah berikut untuk menjalankan project secara lokal.

### 1. Clone repository

```bash
git clone https://github.com/dimasnaufal18/image-compressor.git
cd image-compressor
```

### 2. Pastikan Python sudah terpasang

Gunakan **Python 3.8 atau versi yang lebih baru**.

```bash
python --version
```

Jika perintah `python` tidak tersedia, pada beberapa sistem Anda dapat menggunakan:

```bash
python3 --version
```

### 3. Buat virtual environment

Disarankan menggunakan virtual environment agar dependency project terisolasi dari instalasi Python lainnya.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependency

```bash
pip install -r requirements.txt
```

Atau instal Pillow secara langsung:

```bash
pip install Pillow
```

### 5. Verifikasi instalasi

```bash
python -c "from PIL import Image; print('Pillow berhasil diinstal')"
```

Jika muncul pesan **`Pillow berhasil diinstal`**, project siap digunakan. 🎉

---

## 🚀 Cara Pakai

Jalankan program melalui terminal dengan format:

```bash
python main.py [input] [output] [quality]
```

### Kompres dengan kualitas default

Jika output dan kualitas tidak ditentukan, implementasi project dapat menggunakan nilai default yang tersedia pada `main.py`. Untuk penggunaan sesuai konfigurasi project ini, kualitas default adalah **85**.

```bash
python main.py foto.jpg
```

Contoh:

```text
Input  : foto.jpg
Output : foto_compressed.jpg
Quality: 85
```

### Menentukan nama file output

```bash
python main.py foto.jpg hasil.jpg
```

Perintah tersebut akan membaca `foto.jpg` dan menyimpan hasil kompresi sebagai `hasil.jpg`.

### Menentukan tingkat kualitas

```bash
python main.py foto.jpg hasil.jpg 70
```

Nilai `70` berarti kualitas JPEG yang digunakan adalah **70**.

> ℹ️ Semakin tinggi nilai kualitas, umumnya semakin besar ukuran file dan semakin tinggi kualitas visual. Sebaliknya, nilai yang lebih rendah dapat menghasilkan file yang lebih kecil dengan kemungkinan penurunan kualitas yang lebih terlihat.

### Contoh penggunaan beberapa kualitas

```bash
# Kualitas tinggi
python main.py foto.jpg hasil_high.jpg 90

# Kualitas seimbang
python main.py foto.jpg hasil_medium.jpg 75

# Kompresi lebih agresif
python main.py foto.jpg hasil_small.jpg 50
```

### Batch Processing 📦

Untuk memproses banyak gambar, siapkan file-file sumber di:

```text
examples/input/
```

dan gunakan:

```text
examples/output/
```

sebagai direktori hasil.

> Catatan: implementasi batch processing perlu mengikuti antarmuka yang tersedia pada `main.py`. Jika versi program saat ini hanya menerima satu file per perintah, setiap file dapat diproses dengan menjalankan perintah CLI secara berulang.

Contoh pada Windows PowerShell:

```powershell
Get-ChildItem examples/input/*.jpg | ForEach-Object {
    python main.py $_.FullName "examples/output/$($_.BaseName).jpg" 85
}
```

Contoh pada Linux/macOS:

```bash
for file in examples/input/*.jpg; do
    filename=$(basename "$file")
    python main.py "$file" "examples/output/$filename" 85
done
```

---

## 📊 Contoh Hasil

Hasil aktual bergantung pada resolusi, jenis gambar, kompleksitas visual, format input, metadata, dan tingkat kualitas yang digunakan.

| File | Kualitas | Ukuran Awal | Ukuran Setelah Kompresi | Penghematan |
|---|---:|---:|---:|---:|
| `foto.jpg` | 85 | 4.00 MB | 2.40 MB | 40% |
| `foto.jpg` | 75 | 4.00 MB | 1.90 MB | 52.5% |
| `foto.jpg` | 60 | 4.00 MB | 1.45 MB | 63.75% |

> 📌 **Catatan:** angka pada tabel merupakan **contoh ilustrasi**, bukan hasil benchmark tetap. Persentase penghematan sebenarnya dihitung berdasarkan file yang diproses.

Secara umum:

```text
Ukuran Awal
     │
     ▼
┌───────────────┐
│ Image         │
│ Compressor    │
└───────┬───────┘
        │ Quality 1–100
        ▼
┌───────────────┐
│ Compressed    │
│ JPEG          │
└───────┬───────┘
        │
        ▼
Ukuran Lebih Kecil
```

---

## 📁 Struktur Project

```text
image-compressor/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── examples/
    ├── input/
    └── output/
```

### Penjelasan direktori

| File/Folder | Fungsi |
|---|---|
| `main.py` | Program utama untuk proses kompresi gambar |
| `requirements.txt` | Daftar dependency Python yang diperlukan |
| `README.md` | Dokumentasi project |
| `LICENSE` | Lisensi MIT project |
| `examples/input/` | Tempat menyimpan gambar input untuk contoh/batch processing |
| `examples/output/` | Tempat menyimpan hasil kompresi |

---

## ⚙️ Konfigurasi

Tool menggunakan tiga parameter utama:

| Parameter | Wajib | Nilai | Keterangan |
|---|---|---|---|
| `input` | Ya | Path file | Lokasi gambar yang akan dikompres |
| `output` | Tidak | Path file | Nama/lokasi file hasil |
| `quality` | Tidak | `1–100` | Tingkat kualitas output JPEG |

### Rekomendasi kualitas

| Quality | Tingkat Kompresi | Kualitas Visual | Penggunaan |
|---:|---|---|---|
| **90–100** | Rendah | Sangat tinggi | Arsip, foto penting, kebutuhan kualitas tinggi |
| **80–89** | Sedang | Tinggi | Penggunaan umum |
| **70–79** | Sedang–tinggi | Baik | Web, dokumentasi, berbagi file |
| **50–69** | Tinggi | Cukup baik | Menghemat ruang penyimpanan |
| **1–49** | Sangat tinggi | Dapat terlihat menurun | File dengan prioritas ukuran sangat kecil |

**Rekomendasi awal:** gunakan **quality 85** sebagai titik keseimbangan antara ukuran file dan kualitas visual.

> ⚠️ Nilai quality bukan persentase ukuran file. `quality=70` tidak berarti file akan menjadi tepat 70% dari ukuran awal.

---

## 🔧 Troubleshooting

### 1. `ModuleNotFoundError: No module named 'PIL'`

**Penyebab:** Pillow belum terinstal pada environment Python yang digunakan.

**Solusi:**

```bash
pip install Pillow
```

Jika menggunakan `python3`:

```bash
python3 -m pip install Pillow
```

Kemudian coba kembali:

```bash
python main.py foto.jpg
```

---

### 2. `python is not recognized` atau `command not found: python`

**Penyebab:** Python belum terinstal atau belum masuk ke `PATH`.

**Solusi:**

Periksa instalasi:

```bash
python --version
```

atau:

```bash
python3 --version
```

Jika Python sudah terinstal tetapi perintah `python` tidak tersedia, gunakan `python3` pada Linux/macOS atau pastikan Python ditambahkan ke `PATH` pada Windows.

---

### 3. `FileNotFoundError`

**Penyebab:** File input tidak ditemukan atau path yang diberikan salah.

**Solusi:**

Pastikan nama file dan lokasinya benar:

```bash
python main.py examples/input/foto.jpg
```

Periksa juga ekstensi file, misalnya `.jpg`, `.jpeg`, atau `.png`.

---

### 4. `UnidentifiedImageError`

**Penyebab:** Pillow tidak dapat mengenali file sebagai gambar yang valid. File mungkin rusak, kosong, atau formatnya tidak didukung.

**Solusi:**

- Pastikan file dapat dibuka dengan aplikasi gambar.
- Pastikan file benar-benar merupakan gambar.
- Coba gunakan file JPG atau PNG yang valid.
- Periksa kembali ekstensi dan isi file.

---

### 5. `PermissionError`

**Penyebab:** Program tidak memiliki izin untuk membaca input atau menulis output pada direktori tertentu.

**Solusi:**

Gunakan folder yang dapat ditulis oleh user dan pastikan file output tidak sedang dikunci aplikasi lain.

Contoh:

```bash
python main.py foto.jpg examples/output/hasil.jpg 85
```

---

### 6. Hasil JPEG memiliki latar belakang hitam/aneh

**Penyebab:** Gambar seperti PNG dapat menggunakan **alpha channel/transparansi**, sedangkan JPEG tidak mendukung transparansi.

**Solusi:** Pastikan gambar dikonversi ke mode warna yang sesuai sebelum disimpan sebagai JPEG, misalnya `RGB`. Implementasi `main.py` sebaiknya menangani konversi mode tersebut sebelum output JPEG dibuat.

---

## 🤝 Kontribusi

Kontribusi sangat terbuka untuk pengembangan project ini. Jika Anda ingin membantu, ikuti langkah berikut.

### Langkah kontribusi

1. **Fork** repository.
2. Buat branch baru:

```bash
git checkout -b feature/nama-fitur
```

3. Lakukan perubahan pada project.
4. Uji perubahan secara lokal.
5. Commit perubahan:

```bash
git add .
git commit -m "Add: nama fitur"
```

6. Push branch:

```bash
git push origin feature/nama-fitur
```

7. Buat **Pull Request** dan jelaskan perubahan yang dibuat.

### 💡 Ide fitur pengembangan

- [ ] Dukungan drag-and-drop.
- [ ] Progress bar untuk batch processing.
- [ ] Opsi mempertahankan metadata EXIF.
- [ ] Opsi menentukan folder output.
- [ ] Mode kompresi berdasarkan target ukuran file.
- [ ] Dukungan WebP dan AVIF.
- [ ] Opsi mempertahankan format input.
- [ ] Konfigurasi melalui file `.json` atau `.yaml`.
- [ ] Menampilkan statistik sebelum dan sesudah kompresi.
- [ ] Pengujian otomatis dengan `pytest`.
- [ ] CLI yang lebih lengkap menggunakan `argparse` atau `typer`.

---

## 👤 Author

Project ini dibuat oleh **Mhd Dimas Naufal**.

[![GitHub](https://img.shields.io/badge/GitHub-dimasnaufal18-181717?logo=github&logoColor=white)](https://github.com/dimasnaufal18)
[![Email](https://img.shields.io/badge/Email-emailkamu%40example.com-D14836?logo=gmail&logoColor=white)](sparx1233@gmail.com)

- **Nama:** Mhd Dimas Naufal
- **GitHub:** [@dimasnaufal18](https://github.com/dimasnaufal18)
- **Email:** [sparx1233@gmail.com](sparx1233@gmail.com)
- **Tahun:** 2026

---

## 📄 Lisensi

Project ini menggunakan **MIT License**.

Copyright (c) 2026 **Mhd Dimas Naufal**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the **"Software"**), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

Untuk informasi lebih lanjut mengenai lisensi MIT, kunjungi [Open Source Initiative](https://opensource.org/license/mit/).

---

<div align="center">

⭐ **Jika project ini bermanfaat, jangan lupa berikan bintang di GitHub!** ⭐

Dibuat dengan Python oleh **Mhd Dimas Naufal**

© 2026 **Mhd Dimas Naufal** — Image Compressor

</div>
