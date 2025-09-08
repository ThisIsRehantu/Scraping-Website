# 🌐 Web Scraper with Playwright

Script Python untuk melakukan scraping **website dinamis (Next.js/React/SPA)** menggunakan [Playwright](https://playwright.dev/).  
Script ini bisa menyimpan hasil render halaman, screenshot, dan semua asset (CSS, JS, gambar) ke dalam folder `output/`.

Cocok buat arsip website atau clone untuk deploy ulang di hosting static seperti **Vercel**.

---

## 🚀 Features
- ✅ Render halaman penuh dengan Chromium (headless browser).
- ✅ Simpan HTML hasil render (`output/index.html`).
- ✅ Simpan screenshot halaman penuh (`output/screenshot.png`).
- ✅ Download semua asset (`CSS`, `JS`, `images`) ke `output/assets/`.
- ✅ Bisa dijalankan di **GitHub Codespaces**, **PC Lokal (Linux/Mac/Windows)**, atau **Termux (Android)**.

---

## 📂 Struktur Output
Hasil scraping akan tersimpan dalam struktur berikut:

## 📂 Struktur Output ( Hasil Scraper ) 

output/ ├── index.html
        ├── screenshot.png
        └── assets/



---

## 🛠️ Setup di GitHub Codespaces


### A. GitHub Codespaces 
- Buka Codespaces
- Fork atau clone repo ini.  
- Buka di GitHub Codespaces.

### 1. Install system dependencies (WAJIB)
Jalankan perintah berikut di terminal Codespaces:

```bash
sudo apt-get update && sudo apt-get install -y \
libatk1.0-0 \
libatk-bridge2.0-0 \
libcups2 \
libdrm2 \
libxkbcommon0 \
libxcomposite1 \
libxdamage1 \
libxfixes3 \
libxrandr2 \
libgbm1 \
libasound2t64 \
libnss3 \
libxshmfence1 \
libx11-xcb1 \
libx11-6 \
libxcb1 \
libglib2.0-0 
```

### 2. Instal Dependencies

```bash
pip install playwright requests
playwright install chromium
```

### 3. Jalankan Script

```bash
python scrape.py
```


---

### B. PC Lokal (Linux/Mac/Windows)

### 1. Clone repo
```bash
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME
```


### 2. Install Python dependencies
```bash
pip install playwright requests
playwright install chromium
```
⚠️ Catatan untuk Linux: Jika Playwright error karena dependency sistem, install paket berikut:
```bash
sudo apt-get install -y libnss3 libx11-xcb1 libxcomposite1 libxdamage1 \
libxrandr2 libasound2 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
libgbm1 libxkbcommon0 libxshmfence1 libglib2.0-0
```


### 3. Jalankan Script
```bash
python scrape.py
```

---


### C. Termux (Android)

### 1. Update & Install Python
```bash
pkg update && pkg upgrade -y
pkg install python -y
pkg install python-pip -y
```

### 2. Install dependencies
```bash
pip install playwright requests
playwright install chromium
```

### 3. Install library Playwright di Termux
```bash
playwright install-deps
```

### 4. Clone repo
```bash
git clone https://github.com/USERNAME/REPO-NAME.git
cd REPO-NAME
```

### 5. Jalankan Script
```bash
python scrape.py
```


⚠️ Catatan: Playwright di Termux kadang butuh tambahan setup (misalnya Termux X11 atau proot-distro dengan Ubuntu). Kalau error, lebih disarankan pakai Codespaces atau PC.
