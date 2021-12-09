import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loading",
    version="1.0.0",
    author="Silas Hayes-Williams",
    author_email="silas.hayes.williams@gmail.com",
    description="Displays cool loading animations to the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/silas-hw/loading-pkg",
    project_urls={
        "Bug Tracker": "https://github.com/silas-hw/loading-pkg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)