import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(
    name = "django-buzz",
    version = "0.1.1",
    packages = find_packages(),
    author = "Agiliq and friends",
    author_email ="shabda@agiliq.com", 
    description = "Django app to find What is hot and buzzing in a topic.",
    url = "http://github.com/agiliq/django-buzz",
    include_package_data = True
)
