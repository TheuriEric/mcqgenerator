from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Eric Theuri",
    author_email="tericmail001@gmail.com",
    install_requires=["openai","langchain","streamlit","python-deotenv","pyPDF2"],
    packages=find_packages()
)