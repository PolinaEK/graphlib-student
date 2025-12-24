from setuptools import setup, find_packages

setup(
    name="graphlib-student",
    version="0.1.8",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "networkx"
    ],
    author="Polina",
    description="Учебная библиотека для работы с графами",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    url="https://github.com/PolinaEK/graphlib-student.git",
    project_urls={
        "Source": "https://github.com/PolinaEK/graphlib-student.git",
        "Bug Tracker": "https://github.com/PolinaEK/graphlib-student/issues",
    },
)
