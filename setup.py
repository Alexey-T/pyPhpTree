from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='pyphptree',
    version='1.0.2',
    packages=find_packages(),
    long_description=long_description,
    author='Alexey Torgashin',
    author_email='support@uvviewsoft.com',
    url='https://github.com/Alexey-T/pyPhpTree',
    #license='Mozilla Public License 2.0 (MPL 2.0)',
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
)