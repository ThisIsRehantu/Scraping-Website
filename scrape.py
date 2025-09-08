import os
import requests
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

# Target website
BASE_URL = "https://oprec24.my.id/"

# Output folders
os.makedirs("output/assets", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    print(f"[INFO] Opening {BASE_URL} ...")

    page.goto(BASE_URL)
    page.wait_for_timeout(5000)  # tunggu 5 detik biar semua konten muncul

    # === 1. Simpan HTML final ===
    html = page.content()
    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("[OK] HTML saved -> output/index.html")

    # === 2. Simpan screenshot ===
    page.screenshot(path="output/screenshot.png", full_page=True)
    print("[OK] Screenshot saved -> output/screenshot.png")

    # === 3. Download semua asset (img, css, js) ===
    elements = page.locator("link, script, img")
    count = elements.count()

    for i in range(count):
        el = elements.nth(i)
        src = el.get_attribute("href") or el.get_attribute("src")

        if src:
            full_url = urljoin(BASE_URL, src)
            parsed = urlparse(full_url)
            filename = os.path.basename(parsed.path)

            # Skip kalau ga ada nama file
            if not filename:
                continue

            try:
                r = requests.get(full_url, timeout=10)
                save_path = os.path.join("output/assets", filename)
                with open(save_path, "wb") as f:
                    f.write(r.content)
                print("[OK] Downloaded:", filename)
            except Exception as e:
                print("[ERR] Gagal download:", full_url, "-", e)

    browser.close()
    print("\n[Done] Semua konten sudah disimpan di folder output/")
