#!/usr/bin/env python3
import sys
from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop

if sys.version_info < (3, 7):
    errstr = 'devi only supports python version 3.7+. Please Upgrade.\n'
    sys.exit(1)

requirements = []

if sys.version_info < (3, 11):
    requirements.append('tomli')

test_requirements = []

extra_requirements = {}

class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        print("hola me estoy instalando (develop)")
        print("hola, he fallado! (develop)")

class PostInstallCommand(install):
    def run(self):
        print("hola me estoy instalando")
        print("hola, he fallado!")

setup(
    name='devi',
    description='devi is a tool for managing your project templates',
    long_description=open('README.md').read(),
    author='Paolo Flores',
    license='MIT',
    packages=[],
    entry_points={
        'console_scripts': [
            'khal = khal.cli:main_khal',
            'ikhal = khal.cli:main_ikhal',
        ]
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    tests_require=test_requirements,
    cmdclass={
        'install': PostInstallCommand,
        'develop': PostDevelopCommand
    },
)
