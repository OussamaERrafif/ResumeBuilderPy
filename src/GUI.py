import tkinter as tk
from tkinter import ttk, messagebox

class ResumeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True)

        # Create frames for each tab
        self.create_personal_info_tab()
        self.create_education_tab()
        self.create_experience_tab()
        self.create_skills_tab()
        self.create_projects_tab()
        self.create_certifications_tab()

        # Generate button
        self.generate_button = ttk.Button(root, text="Generate Resume", command=self.generate_resume)
        self.generate_button.pack(pady=10)

    def create_personal_info_tab(self):
        self.personal_info_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.personal_info_frame, text="Personal Info")

        self.personal_info_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.personal_info_frame, text="First Name:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.first_name_entry = ttk.Entry(self.personal_info_frame)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.personal_info_frame, text="Last Name:").grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.last_name_entry = ttk.Entry(self.personal_info_frame)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.personal_info_frame, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.email_entry = ttk.Entry(self.personal_info_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.personal_info_frame, text="Phone:").grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.phone_entry = ttk.Entry(self.personal_info_frame)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.personal_info_frame, text="Address:").grid(row=4, column=0, padx=10, pady=5, sticky='W')
        self.address_entry = ttk.Entry(self.personal_info_frame)
        self.address_entry.grid(row=4, column=1, padx=10, pady=5, sticky='EW')

    def create_education_tab(self):
        self.education_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.education_frame, text="Education")

        self.education_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.education_frame, text="School:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.school_entry = ttk.Entry(self.education_frame)
        self.school_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.education_frame, text="Degree:").grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.degree_entry = ttk.Entry(self.education_frame)
        self.degree_entry.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.education_frame, text="Graduation Date:").grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.graduation_date_entry = ttk.Entry(self.education_frame)
        self.graduation_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

        self.add_education_button = ttk.Button(self.education_frame, text="Add Education", command=self.add_education)
        self.add_education_button.grid(row=3, column=1, padx=10, pady=5, sticky='E')

        self.education_listbox = tk.Listbox(self.education_frame)
        self.education_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

    def create_experience_tab(self):
        self.experience_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.experience_frame, text="Experience")

        self.experience_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.experience_frame, text="Company:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.company_entry = ttk.Entry(self.experience_frame)
        self.company_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.experience_frame, text="Position:").grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.position_entry = ttk.Entry(self.experience_frame)
        self.position_entry.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.experience_frame, text="Start Date:").grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.start_date_entry = ttk.Entry(self.experience_frame)
        self.start_date_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.experience_frame, text="End Date:").grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.end_date_entry = ttk.Entry(self.experience_frame)
        self.end_date_entry.grid(row=3, column=1, padx=10, pady=5, sticky='EW')

        self.add_experience_button = ttk.Button(self.experience_frame, text="Add Experience", command=self.add_experience)
        self.add_experience_button.grid(row=4, column=1, padx=10, pady=5, sticky='E')

        self.experience_listbox = tk.Listbox(self.experience_frame)
        self.experience_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

    def create_skills_tab(self):
        self.skills_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.skills_frame, text="Skills")

        self.skills_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.skills_frame, text="Programming Languages:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.languages_entry = ttk.Entry(self.skills_frame)
        self.languages_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        self.add_languages_button = ttk.Button(self.skills_frame, text="Add Language", command=self.add_language)
        self.add_languages_button.grid(row=1, column=1, padx=10, pady=5, sticky='E')

        self.languages_listbox = tk.Listbox(self.skills_frame)
        self.languages_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

        ttk.Label(self.skills_frame, text="Frameworks:").grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.frameworks_entry = ttk.Entry(self.skills_frame)
        self.frameworks_entry.grid(row=3, column=1, padx=10, pady=5, sticky='EW')

        self.add_frameworks_button = ttk.Button(self.skills_frame, text="Add Framework", command=self.add_framework)
        self.add_frameworks_button.grid(row=4, column=1, padx=10, pady=5, sticky='E')

        self.frameworks_listbox = tk.Listbox(self.skills_frame)
        self.frameworks_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

        ttk.Label(self.skills_frame, text="Databases:").grid(row=6, column=0, padx=10, pady=5, sticky='W')
        self.databases_entry = ttk.Entry(self.skills_frame)
        self.databases_entry.grid(row=6, column=1, padx=10, pady=5, sticky='EW')

        self.add_databases_button = ttk.Button(self.skills_frame, text="Add Database", command=self.add_database)
        self.add_databases_button.grid(row=7, column=1, padx=10, pady=5, sticky='E')

        self.databases_listbox = tk.Listbox(self.skills_frame)
        self.databases_listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

        ttk.Label(self.skills_frame, text="Tools:").grid(row=9, column=0, padx=10, pady=5, sticky='W')
        self.tools_entry = ttk.Entry(self.skills_frame)
        self.tools_entry.grid(row=9, column=1, padx=10, pady=5, sticky='EW')

        self.add_tools_button = ttk.Button(self.skills_frame, text="Add Tool", command=self.add_tool)
        self.add_tools_button.grid(row=10, column=1, padx=10, pady=5, sticky='E')

        self.tools_listbox = tk.Listbox(self.skills_frame)
        self.tools_listbox.grid(row=11, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

    def create_projects_tab(self):
        self.projects_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.projects_frame, text="Projects")

        self.projects_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.projects_frame, text="Project Name:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.project_name_entry = ttk.Entry(self.projects_frame)
        self.project_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.projects_frame, text="Description:").grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.description_entry = ttk.Entry(self.projects_frame)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.projects_frame, text="Tech Stack:").grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.tech_stack_entry = ttk.Entry(self.projects_frame)
        self.tech_stack_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.projects_frame, text="Link:").grid(row=3, column=0, padx=10, pady=5, sticky='W')
        self.link_entry = ttk.Entry(self.projects_frame)
        self.link_entry.grid(row=3, column=1, padx=10, pady=5, sticky='EW')

        self.add_projects_button = ttk.Button(self.projects_frame, text="Add Project", command=self.add_project)
        self.add_projects_button.grid(row=4, column=1, padx=10, pady=5, sticky='E')

        self.projects_listbox = tk.Listbox(self.projects_frame)
        self.projects_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

    def create_certifications_tab(self):
        self.certifications_frame = ttk.Frame(self.notebook, width=400, height=280)
        self.notebook.add(self.certifications_frame, text="Certifications")

        self.certifications_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(self.certifications_frame, text="Certificate Name:").grid(row=0, column=0, padx=10, pady=5, sticky='W')
        self.certificate_name_entry = ttk.Entry(self.certifications_frame)
        self.certificate_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.certifications_frame, text="Issuing Organization:").grid(row=1, column=0, padx=10, pady=5, sticky='W')
        self.issuing_organization_entry = ttk.Entry(self.certifications_frame)
        self.issuing_organization_entry.grid(row=1, column=1, padx=10, pady=5, sticky='EW')

        ttk.Label(self.certifications_frame, text="Date:").grid(row=2, column=0, padx=10, pady=5, sticky='W')
        self.date_entry = ttk.Entry(self.certifications_frame)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5, sticky='EW')

        self.add_certifications_button = ttk.Button(self.certifications_frame, text="Add Certification", command=self.add_certification)
        self.add_certifications_button.grid(row=3, column=1, padx=10, pady=5, sticky='E')

        self.certifications_listbox = tk.Listbox(self.certifications_frame)
        self.certifications_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='EW')

    def add_education(self):
        school = self.school_entry.get()
        degree = self.degree_entry.get()
        graduation_date = self.graduation_date_entry.get()
        self.education_listbox.insert(tk.END, f"{school}, {degree}, {graduation_date}")

    def add_experience(self):
        company = self.company_entry.get()
        position = self.position_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.experience_listbox.insert(tk.END, f"{company}, {position}, {start_date} - {end_date}")

    def add_language(self):
        language = self.languages_entry.get()
        self.languages_listbox.insert(tk.END, language)

    def add_framework(self):
        framework = self.frameworks_entry.get()
        self.frameworks_listbox.insert(tk.END, framework)

    def add_database(self):
        database = self.databases_entry.get()
        self.databases_listbox.insert(tk.END, database)

    def add_tool(self):
        tool = self.tools_entry.get()
        self.tools_listbox.insert(tk.END, tool)

    def add_project(self):
        project_name = self.project_name_entry.get()
        description = self.description_entry.get()
        tech_stack = self.tech_stack_entry.get()
        link = self.link_entry.get()
        self.projects_listbox.insert(tk.END, f"{project_name}, {description}, {tech_stack}, {link}")

    def add_certification(self):
        certificate_name = self.certificate_name_entry.get()
        issuing_organization = self.issuing_organization_entry.get()
        date = self.date_entry.get()
        self.certifications_listbox.insert(tk.END, f"{certificate_name}, {issuing_organization}, {date}")

    def generate_resume(self):
        messagebox.showinfo("Generate Resume", "Resume generation is not yet implemented.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()