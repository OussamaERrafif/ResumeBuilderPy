import subprocess

def convert_latex_to_pdf(latex_file_path, output_pdf_path):
    try:
        subprocess.run(['pdflatex', '-output-directory', output_pdf_path, latex_file_path])
        print("Conversion successful!")
    except Exception as e:
        print(f"Conversion failed: {e}")

# Example usage
latex_file_path = 'C:/Users/ROG Zephyrus/Desktop/Programing/projects/pythonpy/ResumeBuilder/john_doe_resume.tex'
output_pdf_path = 'C:/Users/ROG Zephyrus/Desktop/Programing/projects/pythonpy/ResumeBuilder/output'
convert_latex_to_pdf(latex_file_path, output_pdf_path)