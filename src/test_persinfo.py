import unittest
from persinfo import PersInfo

class TestPersInfo(unittest.TestCase):
    def setUp(self):
        self.person = PersInfo("John", "Doe", "johndoe@example.com", "1234567890", "123 Main St")

    def test_add_education(self):
        self.person.add_Education("University of XYZ", "Bachelor's Degree", "2022")
        self.assertEqual(len(self.person.Education), 1)
        self.assertEqual(self.person.Education[0]['School'], "University of XYZ")
        self.assertEqual(self.person.Education[0]['Degree'], "Bachelor's Degree")
        self.assertEqual(self.person.Education[0]['Graduation Date'], "2022")

    def test_add_experience(self):
        self.person.add_Experience("ABC Company", "Software Engineer", "2018", "2021")
        self.assertEqual(len(self.person.Experience), 1)
        self.assertEqual(self.person.Experience[0]['Company'], "ABC Company")
        self.assertEqual(self.person.Experience[0]['Position'], "Software Engineer")
        self.assertEqual(self.person.Experience[0]['Start Date'], "2018")
        self.assertEqual(self.person.Experience[0]['End Date'], "2021")

    def test_add_programming_languages(self):
        self.person.add_programming_languages("Python")
        self.assertEqual(len(self.person.Skills['Programming Languages']), 1)
        self.assertEqual(self.person.Skills['Programming Languages'][0], "Python")

    def test_add_frameworks(self):
        self.person.add_frameworks("Django")
        self.assertEqual(len(self.person.Skills['Frameworks']), 1)
        self.assertEqual(self.person.Skills['Frameworks'][0], "Django")

    def test_add_databases(self):
        self.person.add_databases("MySQL")
        self.assertEqual(len(self.person.Skills['Databases']), 1)
        self.assertEqual(self.person.Skills['Databases'][0], "MySQL")

    def test_add_tools(self):
        self.person.add_tools("Git")
        self.assertEqual(len(self.person.Skills['Tools']), 1)
        self.assertEqual(self.person.Skills['Tools'][0], "Git")

    def test_add_projects(self):
        self.person.add_projects("Project 1", "Description 1", "Tech Stack 1", "https://example.com/project1")
        self.assertEqual(len(self.person.Projects), 1)
        self.assertEqual(self.person.Projects[0]['project_name'], "Project 1")
        self.assertEqual(self.person.Projects[0]['description'], "Description 1")
        self.assertEqual(self.person.Projects[0]['tech_stack'], "Tech Stack 1")
        self.assertEqual(self.person.Projects[0]['link'], "https://example.com/project1")

    def test_add_certifications(self):
        self.person.add_certifications("Certificate 1", "Organization 1", "2021")
        self.assertEqual(len(self.person.certifications), 1)
        self.assertEqual(self.person.certifications[0]['certificate_name'], "Certificate 1")
        self.assertEqual(self.person.certifications[0]['issuing_organization'], "Organization 1")
        self.assertEqual(self.person.certifications[0]['date'], "2021")

    def test_str_representation(self):
        expected_output = "Name: John Doe\nEmail: johndoe@example.com\nPhone: 1234567890\nAddress: 123 Main St\nEducation: []\nExperience: []\nSkills: {'Programming Languages': [], 'Frameworks': [], 'Databases': [], 'Tools': []}\nProjects: []\nCertifications: []"
        self.assertEqual(str(self.person), expected_output)

if __name__ == '__main__':
    unittest.main()