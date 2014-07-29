
from setuptools import setup, find_packages
import os

# Variable
version = '0.1'

def read(*rnames):
        return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '
' +
    'Contributors
'
    '============
'
    + '
' +
    read('docs', 'CONTRIBUTORS.txt')
    + '
' +
    read('docs', 'CHANGES.txt')
    + '
')

setup(
      name='bb.extjs.session',
      version=version,
      description='Server session for bb.extjs framework',
      long_description=long_description,
      keywords='',
      author='Biel/Bienne',
      author_email='Samuel.Riolo@biel-bienne.ch',
      url='',
      license='LGPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data = True,
      namespace_packages=['bb.extjs'],
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      """,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      )
