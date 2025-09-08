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
- ✅ Bisa dijalankan di **GitHub Codespaces**, **Termux**, atau **Linux server**.

---

## 📂 Struktur Output ( Hasil Scraper ) 

output/ ├── index.html        # HTML hasil render 
        ├── screenshot.png    # Screenshot halaman penuh 
        └── assets/           # File CSS, JS, dan gambar



---

## 🛠️ Setup di GitHub Codespaces

### 1. Buka Codespaces
- Fork atau clone repo ini.  
- Buka di GitHub Codespaces.

### 2. Install system dependencies (WAJIB)
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
libglib2.0-0 ```

### 3. Instal Dependencies

```bash
pip install playwright requests
playwright install chromium

## 4. Jalankan Script

python scrape.py
