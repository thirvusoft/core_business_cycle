from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in core_business_cycle/__init__.py
from core_business_cycle import __version__ as version

setup(
	name="core_business_cycle",
	version=version,
	description="BC",
	author="BC",
	author_email="bc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
