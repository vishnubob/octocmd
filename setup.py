import sys
import os
from setuptools import setup
from pip.req import parse_requirements
from setuptools.command.install import install

install_requires = parse_requirements(os.path.join(os.path.split(__file__)[0], "requirements.txt"))
install_requires = [str(ir.req) for ir in install_requires]

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
    install_requires=install_requires,
    packages=None,
    cmdclass={'install': my_install}
)
