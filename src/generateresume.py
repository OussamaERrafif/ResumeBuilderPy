class ResumeBuilder:
    def __init__(self, person):
        self.person = person

    def generate_latex(self, filename='resume.tex'):
        with open(filename, 'w') as f:
            f.write(r'''\documentclass{resume} % Use the custom resume.cls style

\usepackage[left=0.75in,top=0.6in,right=0.75in,bottom=0.6in]{geometry} % Document margins
\newcommand{\tab}[1]{\hspace{.2667\textwidth}\rlap{#1}}
\usepackage{hyperref}
\newcommand{\itab}[1]{\hspace{0em}\rlap{#1}}
\name{''' + f'{self.person.full_name}' + r'''} % Your name
\address{''' + f'{self.person.address}' + r'''} % Your address
\address{''' + f'{self.person.phone}\\ {self.person.email}' + r'''} % Your phone number and email

\begin{document}

%----------------------------------------------------------------------------------------
%	EDUCATION SECTION
%----------------------------------------------------------------------------------------

\begin{rSection}{Education}
''' + self._format_education() + r'''
\end{rSection}

%----------------------------------------------------------------------------------------
%	EXPERIENCE SECTION
%----------------------------------------------------------------------------------------
\begin{rSection}{Experience}
''' + self._format_experience() + r'''
\end{rSection}

%----------------------------------------------------------------------------------------
%	PROJECTS SECTION
%----------------------------------------------------------------------------------------
\begin{rSection}{Projects}
''' + self._format_projects() + r'''
\end{rSection}

%----------------------------------------------------------------------------------------
%	SKILLS SECTION
%----------------------------------------------------------------------------------------
\begin{rSection}{Skills}
''' + self._format_skills() + r'''
\end{rSection}

%----------------------------------------------------------------------------------------
%	AWARDS AND SCHOLARSHIPS SECTION
%----------------------------------------------------------------------------------------
\begin{rSection}{Awards and Scholarships}
''' + self._format_awards() + r'''
\end{rSection}

\end{document}
''')

    def _format_education(self):
        edu_str = ''
        for edu in self.person.Education:
            edu_str += r'{\bf ' + edu["School"] + r'} \hfill {\em ' + edu["Degree"] + r'} \\ ' + '\n'
            edu_str += 'Graduation Date: ' + edu["Graduation Date"] + r' \\ ' + '\n' + r'\\ ' + '\n'
        return edu_str

    def _format_experience(self):
        exp_str = ''
        for exp in self.person.Experience:
            exp_str += r'{\bf ' + exp["Position"] + r'}, ' + exp["Company"] + r' \hfill {\em ' + exp["Start Date"] + ' - ' + exp["End Date"] + r'} \\ ' + '\n'
            exp_str += r'\\ ' + '\n'
        return exp_str

    def _format_projects(self):
        proj_str = ''
        for proj in self.person.Projects:
            proj_str += r'{\bf ' + proj["project_name"] + r'} \hfill {\em ' + proj["tech_stack"] + r'} \\ ' + '\n'
            proj_str += proj["description"] + r' \\ ' + '\n'
            proj_str += r'\href{' + proj["link"] + r'}{Link} \\ ' + '\n' + r'\\ ' + '\n'
        return proj_str

    

    def _format_skills(self):
        skills_str = '{Programming Languages :}\\' + '\n'
        skills_str += ', '.join(self.person.Skills['Programming Languages']) + r' \\ ' + '\n'
        skills_str += '{Frameworks : }\\' + '\n'
        skills_str += ', '.join(self.person.Skills['Frameworks']) + r' \\ ' + '\n'
        skills_str += '{Databases : }\\' + '\n'
        skills_str += ', '.join(self.person.Skills['Databases']) + r' \\ ' + '\n'
        skills_str += '{Tools : }\\' + '\n'
        skills_str += ', '.join(self.person.Skills['Tools']) + r' \\'
        return skills_str

    def _format_awards(self):
        awards_str = ''
        for cert in self.person.certifications:
            awards_str += r'{\bf ' + cert["certificate_name"] + r'} \hfill ' + cert["issuing_organization"] + r' \hfill {\em ' + cert["date"] + r'} \\ ' + '\n'
        return awards_str
