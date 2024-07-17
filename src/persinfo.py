class PersInfo:
    def __init__(self, first_name, last_name, email, phone, address, Education=None, Experience=None, Skills=None, Projects=None, certifications=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.Education = Education if Education is not None else []
        self.Experience = Experience if Experience is not None else []
        self.Skills = Skills if Skills is not None else {
            'Programming Languages': [],
            'Frameworks': [],
            'Databases': [],
            'Tools': []
        }
        self.Projects = Projects if Projects is not None else []
        self.certifications = certifications if certifications is not None else []

        self.full_name = f'{self.first_name} {self.last_name}'

    def add_Education(self, School, Degree, Graduation_Date):
        self.Education.append({
            'School': School,
            'Degree': Degree,
            'Graduation Date': Graduation_Date
        })

    def add_Experience(self, Company, Position, Start_Date, End_Date= ''):
        if End_Date == '':
            End_Date = 'present'
        self.Experience.append({
            'Company': Company,
            'Position': Position,
            'Start Date': Start_Date,
            'End Date': End_Date
        })

    def add_programming_languages(self, language):
        self.Skills['Programming Languages'].append(language)

    def add_frameworks(self, framework):
        self.Skills['Frameworks'].append(framework)

    def add_databases(self, database):
        self.Skills['Databases'].append(database)

    def add_tools(self, tool):
        self.Skills['Tools'].append(tool)

    def add_projects(self, project_name, description, tech_stack, link):
        self.Projects.append({
            'project_name': project_name,
            'description': description,
            'tech_stack': tech_stack,
            'link': link
        })

    def add_certifications(self, certificate_name, issuing_organization, date):
        self.certifications.append({
            'certificate_name': certificate_name,
            'issuing_organization': issuing_organization,
            'date': date
        })

    def __str__(self):
        return f'Name: {self.full_name}\nEmail: {self.email}\nPhone: {self.phone}\nAddress: {self.address}\nEducation: {self.Education}\nExperience: {self.Experience}\nSkills: {self.Skills}\nProjects: {self.Projects}\nCertifications: {self.certifications}'

