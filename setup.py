from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyphptree',
    version='1.0.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Alexey Torgashin',
    author_email='support@uvviewsoft.com',
    url='http://uvviewsoft.com/',
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: PHP",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ),
)