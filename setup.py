#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='design-automation-benchmark',
      version='0.1.0',
      description='Design Automation Benchmark',
      author='The Design Research Collective',
      author_email='ask-drc@andrew.cmu.edu',
      url='https://github.com/cmudrc/design-automation-benchmark/',    
      install_requires=["numpy", "scipy"],
      packages=['dab'],
      package_dir={'dab': 'src'},
      package_data={'dab': ['data/*']},
      )
