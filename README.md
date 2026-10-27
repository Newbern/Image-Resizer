# Image Resizer

A Python utility for batch-resizing images in a selected folder. It uses a graphical folder picker, preserves image proportions, and saves processed images in a timestamped output directory.

## Features

- Select an image folder using a graphical folder picker.
- Resize images wider than **800 pixels** while preserving their aspect ratio.
- Copy images that are already 800 pixels wide or smaller without resizing.
- Support PNG, JPG, JPEG, BMP, WebP, GIF, and TIFF file extensions.
- Save each processing run in its own timestamped folder.
- Display processing results and errors in the terminal.
- Preserve original files by saving results to a separate output directory.

## Requirements

- Python 3.9 or newer
- Pillow
- Tkinter, included with most standard Python installations

## Installation

1. Download or clone the repository.
2. Open a terminal in the project directory.
3. Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python image_resizer.py
```

1. Select the folder containing your images.
2. Allow the program to process the supported image files.
3. Find the results in the `resized_output` directory next to the script.

Each run creates a separate folder named with the current date and time.

## Output Structure

```text
image-resizer/
├── image_resizer.py
├── README.md
├── requirements.txt
├── .gitignore
└── resized_output/
    └── YYYY-MM-DD_HH-MM-SS/
        ├── photo1.jpg
        └── photo2.png
```

## Supported Formats

- PNG
- JPG / JPEG
- BMP
- WebP
- GIF
- TIFF

## Important Notes

- The program processes images in the selected folder only; it does not scan subdirectories.
- Original filenames are retained.
- Original image files are not modified.
- Animated GIFs and multi-page TIFFs may lose animation frames or additional pages during processing. Special handling is needed to preserve them.

## License

No open-source license is specified. Add a license file if you intend to distribute this project publicly.
