## Shopify Image & Video Upload — Ops Notes

### What didn’t work
- Shopify rejects **HEIC** images and **MOV** videos
- Old Ubuntu tools failed due to:
  - Outdated `libheif`
  - Apple HEIC HDR / auxiliary metadata
- Raw phone images exceeded Shopify limits:
  - > **25 megapixels**
  - > **20 MB**
- ImageMagick crashed without memory limits

---

### What worked
- Upgraded `libheif` (via PPA)
- Standardised on **JPG** for images, **MP4** for videos
- Applied hard caps before upload:
  - Images: **≤ 4500×4500 px**, JPG **quality ~88**, metadata stripped
  - Videos: **1080p**, H.264
- Used fixed, repeatable commands → zero errors

---

### Final commands (copy–paste)

#### HEIC → Shopify-ready JPG (ONLY HEIC)
```bash
shopt -s nullglob && \
export MAGICK_MEMORY_LIMIT=1GiB MAGICK_MAP_LIMIT=2GiB MAGICK_DISK_LIMIT=4GiB && \
for f in *.HEIC *.heic; do \
  heif-convert "$f" temp.jpg && \
  convert temp.jpg \
    -auto-orient \
    -resize '4500x4500>' \
    -quality 88 \
    -strip \
    "${f%.*}-shopify.jpg" && \
  rm temp.jpg; \
done
```

#### MOV → Shopify-ready MP4
```bash
for f in *.MOV *.mov; do
  ffmpeg -i "$f" \
    -vf "scale=1920:-2" \
    -c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p \
    -crf 24 -preset slow \
    -movflags +faststart \
    -c:a aac -b:a 128k \
    "${f%.*}.mp4"
done
```

