# Orama Zetta docs website — built with MkDocs Material, served static on Railway.
# Graphviz diagrams are PRE-RENDERED to SVG by the zetta-sync skill and committed
# under docs/diagrams/, so the container needs no graphviz system dependency.
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# Build the static site into ./site
RUN mkdocs build --site-dir site

ENV PORT=8080
EXPOSE 8080

# Serve the built static site bound to Railway's $PORT.
CMD ["sh", "-c", "python3 -m http.server ${PORT} --bind 0.0.0.0 --directory site"]
