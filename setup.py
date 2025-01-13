from setuptools import setup, find_packages

setup(
    name='neetcode',
    version='0.1.0',
    author='Alberto Bonifacio',
    packages=find_packages(include=['src','src.*']),
    install_requires=[
        'pandas',
        'numpy',
        'jupyter',
        'ipykernel',
        'black'
    ],
    python_requires='>=3.11.9',
)