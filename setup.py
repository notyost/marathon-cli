import os
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
INSTALL_REQS = parse_requirements(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.pip'),
    session=PipSession()
)

setup(
    name='marathon_cli',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    description='command line utility for marathon api requests',
    long_description='command line utility for marathon api requests',
    url='https://github.com/SPScommerce/marathon-cli',
    author='meganlkm',
    author_email='webapps@spscommerce.com',
    install_requires=[str(ir.req) for ir in INSTALL_REQS],
    entry_points={
        'console_scripts': [
            'marathon-cli=marathon_cli:main'
        ],
    }
)