from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts] #replaces the new line "\n" while reading newline from requirements.txt file.

        if HYPHEN_E_DOT in requiremnts:
            requiremnts.remove(HYPHEN_E_DOT)
    return requiremnts
    

setup(
    name='MLProject',
    version='0.0.1',
    author='Neel Adalja',
    author_email='neel.adalja25@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)