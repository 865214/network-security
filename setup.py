from setuptools import find_packages, setup

def get_requirements()->list[str]:
    """
    This function will return list of requirements
    """
    requirement_lst: list[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            #Read Lines from the file 
            lines = file.readlines()
            # Process each Lines
            for line in lines:
                requirement = line.strip()
                #Ignore emply line and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_lst

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Zoheb Kazi",
    author_email = "kazizoheb59@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)
                       