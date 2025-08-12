### Caminatas

1. Install uv (please install globally)
   ```
   pip install uv
   ```

2. install dependencies
   ```
   uv sync
   ```

3. Start the app locally
   ```
   uv run fastapi dev
   ```

4. Start the TailwindCSS CLI to update css in realtime
   ```
   uv run tailwind.py
   ```

### MISC

1. Format `.jinja` files with djlint, on the `./templates` directory
   ```
   uv run djlint.py
   ```

2. OPTIMIZE IMAGES (needs size optimization too)
   ```sh
   cwebp -q 78 -mt -af -sharp_yuv input.jpg -o output_q78.webp
   avifenc -q 55 -s 6 --yuv 420 --sharpyuv -a tune=ssim input.jpg output_q55.avif
   cjpeg -quality 80 -optimize -progressive -sample 2x2 -quant-table 3 -outfile output_q80.jpg input.jpg
   ```

