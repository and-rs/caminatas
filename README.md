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

### TODO

- [ ] fix hot-reload types (arel)
- [ ] script for updating static dependencies
- [ ] black, djlint and basedpyright pre-commit pipeline
- [ ] autoreload tailwind stylesheet
- [ ] integrate rustywind?
- [x] jinja fragments (not necessary)
