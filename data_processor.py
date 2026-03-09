import csv
import json
from datetime import datetime

class DataProcessor:
    """
    Simple data automation tool.
    Reads CSV → processes rows → outputs clean data
    """
    
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.processed_data = []
    
    def read_csv(self):
        """Read data from CSV file"""
        print(f"Reading {self.input_file}...")
        with open(self.input_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.processed_data.append(row)
        print(f"Read {len(self.processed_data)} rows")
    
    def process_rows(self):
        """
        Process each row of data.
        Example: clean email, validate, add timestamp
        """
        print("Processing rows...")
        for row in self.processed_data:
            # Example processing: clean email, add status
            if 'email' in row:
                row['email'] = row['email'].lower().strip()
                row['email_valid'] = '@' in row['email']
            
            # Add processing timestamp
            row['processed_at'] = datetime.now().isoformat()
        
        print(f"Processed {len(self.processed_data)} rows")
    
    def save_output(self, format='json'):
        """Save processed data to file"""
        print(f"Saving to {self.output_file}...")
        
        if format == 'json':
            with open(self.output_file, 'w') as f:
                json.dump(self.processed_data, f, indent=2)
        elif format == 'csv':
            if self.processed_data:
                keys = self.processed_data[0].keys()
                with open(self.output_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(self.processed_data)
        
        print(f"Done! Output saved to {self.output_file}")
    
    def run(self, output_format='json'):
        """Execute the full pipeline"""
        self.read_csv()
        self.process_rows()
        self.save_output(format=output_format)

# Usage
if __name__ == '__main__':
    processor = DataProcessor('input.csv', 'output.json')
    processor.run()