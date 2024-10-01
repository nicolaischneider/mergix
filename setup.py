from setuptools import setup, find_packages

setup(
    name="mergix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mergix=mergix.main:main',
        ],
    },
    author="Nicolai Schneider",
    description="A tool to analyze Git merge conflicts",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nicolaischneider/mergix",
)