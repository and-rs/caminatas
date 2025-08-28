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

3. Generate requirements.txt for deployment
   ```sh
   uv export --no-emit-workspace --no-dev --no-annotate --no-header --no-hashes --output-file requirements.txt
   ```

### TODO

1. Dev Ex
   - [ ] rustywind, black, djlint and basedpyright pre-commit pipeline
   - [ ] script for updating static dependencies (htmx)
   - [ ] responsive design for main sections and components
   - [ ] image optimization pipeline
   - [ ] lazyloading pipeline
   - [ ] lighthouse testing
   - [ ] first deployment (railway)
   - [ ] gzip middleware pipeline

   - [x] autoreload tailwind stylesheet
   - [x] mobile modal for header
   - [x] first mockup

2. Sections
   - [ ] Home
     - [ ] hero (find better image)
     - [ ] carousel
     - [ ] benefits
     - [ ] step-by-step for users
     - [ ] upcoming events
     - [ ] call to action (contact)
   - [ ] About Us
   - [ ] Walks
   - [ ] Blog

### Page Examples

- https://www.volcanoadventures.com.co/
- https://www.tufuerzanatural.com/eventos
- https://www.roadtrip.travel/blog
- https://montanascolombianas.com/
- https://htmlrev.com/free-tailwind-templates.html#services
