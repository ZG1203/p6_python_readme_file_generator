from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator

license_list=[
    "Academic Free License v3.0 (AFL-3.0)",
    "Apache license 2.0 (Apache-2.0)",
    "Artistic license 2.0 (Artistic-2.0)",
    "Boost Software License 1.0 (BSL-1.0)",
    "BSD 2-clause 'Simplified' license (BSD-2-Clause)",
    "BSD 3-clause 'New' or 'Revised' license (BSD-3-Clause)",
    "BSD 3-clause Clear license (BSD-3-Clause-Clear)",
    "BSD 4-clause 'Original' or 'Old' license (BSD-4-Clause)",
    "BSD Zero-Clause license (0BSD)",
    "Creative Commons license family (CC)",
    "Creative Commons Zero v1.0 Universal (CC0-1.0)",
    "Creative Commons Attribution 4.0 (CC-BY-4.0)",
    "Creative Commons Attribution ShareAlike 4.0 (CC-BY-SA-4.0)",
    "Do What The F*ck You Want To Public License (WTFPL)",
    "Educational Community License v2.0 (ECL-2.0)",
    "Eclipse Public License 1.0 (EPL-1.0)",
    "Eclipse Public License 2.0 (EPL-2.0)",
    "European Union Public License 1.1 (EUPL-1.1)",
    "GNU Affero General Public License v3.0 (AGPL-3.0)",
    "GNU General Public License family (GPL)",
    "GNU General Public License v2.0 (GPL-2.0)",
    "GNU General Public License v3.0 (GPL-3.0)",
    "GNU Lesser General Public License family (LGPL)",
    "GNU Lesser General Public License v2.1 (LGPL-2.1)",
    "GNU Lesser General Public License v3.0 (LGPL-3.0)",
    "ISC (ISC)",
    "LaTeX Project Public License v1.3c (LPPL-1.3c)",
    "Microsoft Public License (MS-PL)",
    "MIT (MIT)",
    "Mozilla Public License 2.0 (MPL-2.0)",
    "Open Software License 3.0 (OSL-3.0)",
    "PostgreSQL License (PostgreSQL)",
    "SIL Open Font License 1.1 (OFL-1.1)",
    "University of Illinois/NCSA Open Source License (NCSA)",
    "The Unlicense (Unlicense)",
    "zLib License (Zlib)"
]


def readme_generator ():
    print("Please answer questions below to generate a readme file")
    questions = [
        {"type": "input", "name":"title","message":"What is your project title?","validate": EmptyInputValidator("Project title cannot be empty")},
        {"type": "input", "name":"description","message":"What is the project description?","validate": EmptyInputValidator("Project description cannot be empty")},
        {"type": "input", "name":"installation","message":"What are installation instructions?","validate": EmptyInputValidator("Installation instructions cannot be empty")},
        {"type": "input", "name":"usage","message":"What is usage information?","validate": EmptyInputValidator("Usage information cannot be empty")},
        {"type": "list", "name":"license","message":"choose a license","choices":license_list},
        {"type": "input", "name":"author","message":"What is the author's name?","validate": EmptyInputValidator("Author's name cannot be empty")},
        {"type": "input", "name":"contact","message":"What is the author's contact information?","validate": EmptyInputValidator("Author's contact cannot be empty")}
    ]
    answers = prompt(questions)
    with open("readme.md","w") as md_file:
        md_file.write(f"# {answers['title'].title()}\n\n")
        for key,value in answers.items():
            if key != "title":
                formated_key=key.title()
                md_file.write(f"## {formated_key}\n")
                formated_value=value.capitalize()
                md_file.write(f"{formated_value}\n\n")
    print ("Readme file has been created")
    print ("Generated readme file content:")
    with open("readme.md","r") as md_file:
        for line in md_file:
            print(line)
    

readme_generator()