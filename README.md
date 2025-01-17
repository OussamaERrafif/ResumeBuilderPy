# Resume Generator using LaTeX

## Description

This Python project generates a professional resume using LaTeX. The project allows users to customize their resume details directly in the Python script, which then compiles into a polished PDF document. This tool is perfect for anyone looking to create a clean and customizable resume with minimal effort.

## Features

- Easy customization of resume content within the Python script.
- Generates a professional-looking PDF resume.
- Utilizes the power of LaTeX for precise formatting and styling.
- Simple setup and execution process.

## Requirements

- Python 3.x
- LaTeX distribution installed on your computer (e.g., TeX Live, MiKTeX)

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/resume-generator-latex.git
cd resume-generator-latex
```

### Step 2: Set Up Python Environment

It is recommended to use a virtual environment to manage dependencies. 

#### Using `venv`

```bash
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
```

### Step 3: Install LaTeX

Ensure you have a LaTeX distribution installed on your computer. You can download and install one of the following:

- [TeX Live](https://www.tug.org/texlive/)
- [MiKTeX](https://miktex.org/)

Make sure the LaTeX binaries are added to your system's PATH.

## Usage

1. Customize the `app.py` script with your personal information, work experience, education, skills, and other relevant details.
2. Run the Python script to generate the resume:

```bash
python app.py
```

3. The generated PDF resume will be saved in the `output` directory.
