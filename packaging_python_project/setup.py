import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="animal-pkg-lyt", # Replace with your own username
    version="0.0.1",
    author="lytang",
    author_email="luyang.tang@lmh.ox.ac.uk",
    description="Animal pkg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luyangtang/python_bootcamp/packaging_python_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)