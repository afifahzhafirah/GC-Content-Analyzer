import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from pathlib import Path

class GCAnalyzer:
    def __init__(self, records: list):
        self.records = records

    def analyze(self) -> list:
        results = []
        for record in self.records:
            counts = record.get_alignment_data()
            gc_content = record.get_gc_content()
            results.append({
                'Variant': record.header,
                'Length (bp)': len(record.sequence),
                'A': counts['A'],
                'T': counts['T'],
                'G': counts['G'],
                'C': counts['C'],
                'GC Content (%)': gc_content
            })
        return sorted(results, key=lambda x: x['GC Content (%)'], reverse=True)

    def summary(self, results: list) -> str:
        if not results:
            return "No sequence data processed."
        return f"Successfully analyzed {len(results)} sequences. The highest GC content is found in '{results[0]['Variant']}' ({results[0]['GC Content (%)']}%)."

    def generate_chart(self, results: list, output_dir: Path) -> str:
        """Membuat grafik batang"""
        if not results:
            return ""
        
        variants = [item['Variant'] for item in results]
        gc_values = [item['GC Content (%)'] for item in results]
        
        plt.figure(figsize=(7.5, 4.2))
        plt.gcf().patch.set_facecolor('#1e293b')  
        
        ax = plt.axes()
        ax.set_facecolor('#0f172a')  
        
        bars = plt.bar(variants, gc_values, color='#f43f5e', edgecolor='#38bdf8', width=0.4)
        
        plt.title('GC Content Distribution per Sequence', color='#38bdf8', fontsize=12, pad=15, fontweight='bold')
        plt.ylabel('GC Content (%)', color='#94a3b8', labelpad=8, fontsize=10)
        plt.xlabel('Sequence Identifier', color='#94a3b8', labelpad=12, fontsize=10)
        
        ax.set_xticklabels(
            variants, 
            color='#94a3b8', 
            fontsize=8.5, 
            rotation=45, 
            ha='right', 
            rotation_mode='anchor'
        )
        
        ax.tick_params(axis='y', colors='#94a3b8', labelsize=8.5)
        ax.spines['bottom'].color = '#334155'
        ax.spines['left'].color = '#334155'
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.grid(axis='y', linestyle='--', alpha=0.1, color='#cbd5e1')
        
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom', color='#f8fafc', fontsize=8, fontweight='bold')
        
        output_dir.mkdir(parents=True, exist_ok=True)
        chart_path = output_dir / "gc_chart.png"
        plt.savefig(chart_path, dpi=150, bbox_inches='tight', facecolor=plt.gcf().get_facecolor())
        plt.close()
        
        return "/static/gc_chart.png"