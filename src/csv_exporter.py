import csv
from pathlib import Path

class CSVExporter:
    def to_string(self, results: list) -> str:
        if not results: return ""
        headers = results[0].keys()
        rows = [",".join(headers)]
        for item in results:
            rows.append(",".join(str(item[k]) for k in headers))
        return "\n".join(rows)

    def export(self, results: list, output_path: Path):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if not results: return
        headers = results[0].keys()
        with open(output_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(results)