# Multiple figures in .PDF to LibreOffice Impress (.odp)

This script takes an arbitrary number of PDF figures and creates a LibreOffice Impress presentation (.odp) file. It then inserts the figures into the slides in a grid format, with no overlapping.

## Requirements
- Python 3.x
- ezodf package
- LibreOffice Impress

## Usage
`pdf2odp.py [-h] [-o OUT] [-s FPS] [-r ROWS] [-c COLS] path`

#### Arguments
- `path` (required): path to directory containing the .pdf files of the figures
- `-o/--out`: output file name. Default is 'pdf2odp'
- `-s/--fps`: number of figures per slide. Default is 1
- `-r/--rows`: number of rows in figure grid. Default is 2
- `-c/--cols`: number of columns in figure grid. Default is 2

## Example Usage
To create a LibreOffice Impress file with 2 figures per slide, 3 rows, and 2 columns, run the following command:

python pdf2odp.py -s 2 -r 3 -c 2 /path/to/figures/

This will create an Impress file named `pdf2odp.odp` in the current working directory.
