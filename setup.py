from setuptools import find_packages, setup

setup(
    name='cetys-chatbot',
    packages=find_packages(where=".") +
    find_packages(where="./Chatbot") +
    find_packages(where="./Model") +
    find_packages(where="./Solutions")

)