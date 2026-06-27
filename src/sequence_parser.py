from src.sequence_record import SequenceRecord

class SequenceParser:
    def parse(self, file_content: str, filename: str) -> list:
        records = []
        lines = file_content.splitlines()
        if not lines:
            return records

        first_line = lines[0].strip()

        # Format FASTA
        if first_line.startswith('>'):
            current_header = None
            current_seq_lines = []
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('>'):
                    if current_header is not None:
                        records.append(SequenceRecord(current_header, "".join(current_seq_lines)))
                    current_header = line[1:].strip()
                    current_seq_lines = []
                else:
                    current_seq_lines.append(line)
            if current_header is not None:
                records.append(SequenceRecord(current_header, "".join(current_seq_lines)))

        # Format FASTQ
        elif first_line.startswith('@'):
            for i in range(0, len(lines), 4):
                if i + 1 < len(lines):
                    header = lines[i].strip()[1:]
                    sequence = lines[i+1].strip()
                    if header and sequence:
                        records.append(SequenceRecord(header, sequence))
        else:
            raise ValueError("Format file salah! Harus FASTA (>) atau FASTQ (@).")
        return records