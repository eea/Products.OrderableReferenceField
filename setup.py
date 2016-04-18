""" Setup.py
"""
from setuptools import setup, find_packages
import os
from os.path import join


NAME = 'Products.OrderableReferenceField'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description=(
            "This product provides an Archetype field that's very similiar "
            "to the Archetypes Reference field, with the addition that it "
            "stores the order of referenced objects"),
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='European Environment Agency',
      author_email='webadmin@eea.europa.eu',
      url='ttps://github.com/eea/Products.OrderableReferenceField',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
