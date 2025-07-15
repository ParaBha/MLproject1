#setup.py is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package.

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'#-e . is map to setup.py
def get_requirements(file_path:str)->List[str]:
    '''
    thsi function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #to remove the \n from the requirements.txt
        requirements = [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(

name = 'mlproject',
version = '0.0.1',
author = 'Param',
author_email = 'parambhatt95@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)
    
