import sys
import os
from setuptools import setup
from setuptools.command.install import install


class my_install(install):
    def run(self):
        self.run_command("test")
        self.run_command("install_scripts")

s = setup(
    name="octocmd", 
    version='0.1',
    author='Giles Hall', 
    author_email="giles@polymerase.org",
    url='https://github.com/vishnubob/octocmd',
    description='Command line interface for OctoPrint',
    keywords=['OctoPrint', 'command'],
    scripts=["scripts/octocmd"],
    install_requires=[
        "requests",
    ],
    packages=None,
    cmdclass={'install': my_install}
)
