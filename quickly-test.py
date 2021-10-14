import os
from pdf2docx import Converter

def main():
    script_path = os.path.abspath(__file__) 
    test_dir = os.path.dirname( script_path )  + '/test'
    sample_dir = os.path.join( test_dir, 'samples')
    output_dir =  os.path.join(test_dir, 'outputs')

    filename = 'x5'
    pdf_file = os.path.join(sample_dir, f'{filename}.pdf')
    docx_file = os.path.join(output_dir, f'{filename}.docx')
    
    cv = Converter( pdf_file )
    settings = {
        'min_section_height': 0
    }
    cv.convert(docx_file, start=0, end=None, **settings) # Hay que corregir el quitar '.pdf' ya que queda en el nombre del archivo
    cv.close()


if __name__ == '__main__':
    main()
   