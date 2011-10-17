from setuptools import find_packages
from distutils.core import setup

setup(
    name = "django-buzz",
    version = "0.1.2",
    packages = find_packages(),
    author = "Agiliq and friends",
    author_email ="shabda@agiliq.com", 
    description = "Django app to find What is hot and buzzing in a topic.",
    url = "http://github.com/agiliq/django-buzz",
    include_package_data = True
)
