import os
import subprocess
import sys
from pathlib import Path
from tqdm import tqdm

def process_pdf_folder(input_folder, output_base_dir):
    """Process all PDFs in a given folder using magic-pdf."""
    input_path = Path(input_folder)
    output_dir = Path(output_base_dir) / input_path.name
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nProcessing folder: {input_folder}")
    print(f"Output directory: {output_dir}")
    
    # Get list of PDF files in the folder
    pdf_files = list(input_path.glob('*.pdf'))
    
    # Process each PDF in the folder with progress bar
    for pdf_file in tqdm(pdf_files, desc=f"Processing {input_path.name}"):
        try:
            # Create individual output directory for each PDF
            pdf_output_dir = output_dir / pdf_file.stem
            pdf_output_dir.mkdir(parents=True, exist_ok=True)
            
            # Construct and execute magic-pdf command
            cmd = [
                'magic-pdf',
                '-p', str(pdf_file),
                '-o', str(pdf_output_dir),
                '-m', 'auto'
            ]
            
            # Run the command and capture output
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                print(f"\nError processing {pdf_file.name}:")
                print(f"Error output: {result.stderr}")
                
        except Exception as e:
            print(f"\nError processing {pdf_file.name}: {str(e)}")

def main():
    """Main function to orchestrate the PDF processing workflow."""
    try:
        # Create base output directory
        output_base_dir = Path('processed_pdfs')
        output_base_dir.mkdir(exist_ok=True)
        
        # Get all pdf folders sorted numerically
        pdf_folders = sorted(
            [d for d in Path('.').glob('pdfs_*') if d.is_dir()],
            key=lambda x: int(str(x).split('_')[1])
        )
        
        # Process each folder
        for folder in pdf_folders:
            process_pdf_folder(folder, output_base_dir)
                
        print("\nProcessing complete!")
        print(f"Results saved in: {output_base_dir.absolute()}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
