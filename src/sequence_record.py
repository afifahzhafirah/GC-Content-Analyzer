class SequenceRecord:
    def __init__(self, header: str, sequence: str):
        """
        Inisialisasi objek sekuens tunggal.
        """
        self.header = header
        self.sequence = sequence.upper() 

    def get_alignment_data(self) -> dict:
        """
        Menghitung frekuensi kemunculan setiap basa nitrogen menggunakan Dictionary.
        """
        counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        
        # Looping membaca sekuens
        for base in self.sequence:
            if base in counts:
                counts[base] += 1
        return counts

    def get_gc_content(self) -> float:
        """
        Menghitung persentase GC Content dari sekuens.
        Rumus: ((G + C) / Total Basa) * 100
        """
        counts = self.get_alignment_data()
        gc_count = counts['G'] + counts['C']
        total_bases = len(self.sequence)
        
        if total_bases == 0:
            return 0.0
            
        # Hitung persentase
        gc_percentage = (gc_count / total_bases) * 100
        return round(gc_percentage, 2)  