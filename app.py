import os
from pathlib import Path
from flask import Flask, render_template, request, send_file
from src.csv_exporter import CSVExporter
from src.gc_analyzer import GCAnalyzer
from src.sequence_parser import SequenceParser

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
LATEST_CSV = OUTPUT_DIR / "hasil_gc_content.csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = Flask(__name__)
parser = SequenceParser()
exporter = CSVExporter()

@app.get("/")
def index():
    return render_template("index.html", results=None)

@app.post("/analyze")
def analyze():
    uploaded_file = request.files.get("sequence_file")
    if not uploaded_file or uploaded_file.filename == "":
        return render_template("index.html", error="Please select a FASTA/FASTQ file first.", results=None)

    try:
        file_content = uploaded_file.read().decode("utf-8")
        records = parser.parse(file_content, uploaded_file.filename)
        if not records:
            return render_template("index.html", error="Invalid sequence file format.", results=None)
            
        analyzer = GCAnalyzer(records)
        results = analyzer.analyze()
        summary = analyzer.summary(results)
        
        STATIC_DIR = Path(__file__).resolve().parent / "static"
        chart_url = analyzer.generate_chart(results, STATIC_DIR)
        
        exporter.export(results, LATEST_CSV)
        
        return render_template(
            "index.html", 
            results=results, 
            summary=summary, 
            top_three=results[:3],
            chart_url=chart_url
        )
    except Exception as e:
        return render_template("index.html", error=str(e), results=None)

@app.get("/download-csv")
def download_csv():
    if not LATEST_CSV.exists():
        return "No file available for download.", 404
    return send_file(LATEST_CSV, mimetype="text/csv", as_attachment=True, download_name="gc_analytics_results.csv")

if __name__ == "__main__":
    app.run(debug=True)