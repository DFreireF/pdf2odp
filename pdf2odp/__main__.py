import ezodf
import os
import argparse

def create_presentation(file_path, output_name = 'default-name', figures_per_slide = 1, rows=2, cols=2):
    # Create a new presentation
    doc = ezodf.newdoc(doctype='odp')

    # Loop through all the input figures
    figures = [f for f in os.listdir(file_path) if f.endswith('.pdf')]
    num_figures = len(figures)
    num_slides = num_figures // figures_per_slide + (num_figures % figures_per_slide > 0)
    slide_idx = 1
    fig_idx = 0
    while slide_idx <= num_slides:
        # Create a new slide
        slide = doc.body.add_presentation_slide()

        # Add figures to the slide
        for row in range(rows):
            for col in range(cols):
                if fig_idx >= num_figures:
                    break

                figure = figures[fig_idx]
                image = slide.add_image(file_path + '/' + figure)
                image.width = f'{100//cols}%'
                image.height = f'{100//rows}%'
                image.vertical_align = 'middle'
                image.horizontal_align = 'center'
                image.vertical_pos = f'{100//rows*row + 50//(2*rows)}%'
                image.horizontal_pos = f'{100//cols*col + 50//(2*cols)}%'
                fig_idx += 1

        slide_idx += 1

    # Save the presentation
    doc.save(f'{output_name}.odp')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create LibreOffice Impress presentation with figures')
    parser.add_argument('path', type=str, help='path to directory containing figures')
    parser.add_argument('-o','--out', type=str, default = 'pdf2odp', help='Output name')
    parser.add_argument('-s', '--fps', type=int, default=1, help='number of figures per slide')
    parser.add_argument('-r', '--rows', type=int, default=2, help='number of rows in figure grid')
    parser.add_argument('-c', '--cols', type=int, default=2, help='number of columns in figure grid')
    args = parser.parse_args()

    create_presentation(args.path, args.out, args.fps, args.rows, args.cols)
