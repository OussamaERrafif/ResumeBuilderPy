from persinfo import PersInfo
from generateresume import ResumeBuilder


def main():
    # Example usage
    person = PersInfo(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
        phone='+1234567890',
        address='123 Main St, Anytown, USA'
    )

    # Add education
    person.add_Education(School='University of Example', Degree='B.Sc. Computer Science', Graduation_Date='June 2024')
    person.add_Education(School='Example College', Degree='High School Diploma', Graduation_Date='June 2020')

    # Add experience
    person.add_Experience(Company='Example Corp', Position='Software Engineer', Start_Date='January 2021', End_Date='Present')
    person.add_Experience(Company='Example LLC', Position='Intern', Start_Date='June 2020', End_Date='December 2020')

    # Add skills
    person.add_programming_languages('Python')
    person.add_programming_languages('JavaScript')
    person.add_frameworks('Django')
    person.add_frameworks('React')
    person.add_databases('PostgreSQL')
    person.add_tools('Git')

    # Add projects
    person.add_projects(project_name='Project Alpha', description='A web application for managing tasks.', tech_stack='Python, Django', link='https://github.com/johndoe/project-alpha')
    person.add_projects(project_name='Project Beta', description='A web application for managing inventory.', tech_stack='JavaScript, React', link='https://github.com/johndoe/project-alpha')

    # Add certifications
    person.add_certifications(certificate_name='Certified Python Developer', issuing_organization='Python Institute', date='December 2020')
    person.add_certifications(certificate_name='Certified React Developer', issuing_organization='React Foundation', date='January 2021')

    # Generate the resume
    resume_builder = ResumeBuilder(person)
    resume_builder.generate_latex('john_doe_resume.tex')



if __name__ == '__main__':
    main()
