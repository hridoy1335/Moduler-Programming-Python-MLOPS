from typing import List
from setuptools import setup, find_packages



PROJECT_NAME = "MLOPS"
DESCRIPTION = "It's a test project for MLOPS"
AURTHOR = "Hridoy Khan"
EMAIL = "rkhridoyinfo@gmail.com"
VERSION = "0.0.1"
url = "https://github.com/hridoy1335"
HYPEN_E_DOT = "-e ."



def get_requires_list()->List[str]:
    with open("requirements.txt", "r") as f:
        requires_list = [line.strip() for line in f.readlines()]
        if HYPEN_E_DOT in requires_list:
            requires_list.remove(HYPEN_E_DOT)
            return requires_list



setup(
    name=PROJECT_NAME,
    author=AURTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    version=VERSION,
    url=url,
    packages=find_packages(),
    install_requires=get_requires_list()
)