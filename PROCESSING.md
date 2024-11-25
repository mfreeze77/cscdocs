# PDF Processing Instructions

This guide explains how to use the PDF processing script in your runpod environment.

## Setup

1. Copy the repository contents to your runpod environment
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure magic-pdf is installed and accessible in your environment

## Usage

Simply run the script in the directory containing the PDF folders:

```bash
python process_pdfs.py
```

The script will:
- Process all PDFs in each `pdfs_XX` folder
- Create a `processed_pdfs` directory
- Generate output for each PDF including:
  - Markdown file
  - Layout diagrams
  - Extracted images
  - JSON files with content and structure information

## Output Structure

For each PDF, the following output will be generated in the `processed_pdfs` directory:

```
processed_pdfs/
├── pdfs_01/
│   ├── document1/
│   │   ├── document1.md
│   │   ├── images/
│   │   ├── document1_layout.pdf
│   │   ├── document1_middle.json
│   │   ├── document1_model.json
│   │   ├── document1_origin.pdf
│   │   ├── document1_spans.pdf
│   │   └── document1_content_list.json
│   └── document2/
│       └── ...
├── pdfs_02/
│   └── ...
└── ...
```

## Error Handling

The script includes error handling and progress tracking:
- Progress bars show processing status for each folder
- Errors are logged but won't stop the entire process
- Each PDF is processed independently

## GPU Resources

The script will automatically utilize available GPU resources through magic-pdf's implementation. No additional configuration is needed for GPU acceleration.

## Monitoring

You can monitor the progress through:
- Progress bars for each folder
- Console output for any errors or issues
- The growing `processed_pdfs` directory structure
