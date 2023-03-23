from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as f:
        requirements= f.readlines()
        requirements=[r.replace("\n"," ") for r in requirements]



setup(
name='ML_Project',
version='0.0.1',
author='deftydev',
author_email='devanshgupta79212346@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)