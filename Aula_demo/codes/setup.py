from setuptools import find_packages, setup

setup(
   name='data-path',
   version='1.0',
   packages=find_packages(exclude=['tests*']),
   include_package_data=True,
)