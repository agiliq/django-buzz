from setuptools import find_packages
from distutils.core import setup

setup(
    name = "django-buzz",
    version = "0.4a",
    packages = find_packages(),
    author = "Agiliq",
    author_email ="hello@agiliq.com",
    description = "Django app to find What is hot and buzzing in a topic.",
    url = "http://github.com/agiliq/django-buzz",
    include_package_data = True
)
