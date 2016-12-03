#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

try:
  from setuptools import setup, find_packages
  setup
except ImportError:
  from distutils.core import setup
  setup

from splat import __version__

from setuptools import setup, find_packages
setup(
  name = "splat",
  version = __version__,
  packages = find_packages(exclude=['docs','tests*']),

  # Project uses reStructuredText, so ensure that the docutils get
  # installed or upgraded on the target machine
  install_requires = ['astropy','astroquery','bokeh','flask','matplotlib','numpy','pandas','requests','scipy'],

  package_data = {
      '': ['db/*.bib', 'db/*.txt','reference/EvolutionaryModels/Baraffe/*',\
            'reference/EvolutionaryModels/Burrows/*','reference/EvolutionaryModels/Saumon/*',\
            'reference/EvolutionaryModels/Baraffe/*','reference/Filters/*.txt','reference/Spectra/*.fits', \
            'reference/SpectralModels/BTSettl2008/*.txt','reference/SpectralModels/BTSettl2015/*.txt',\
            'reference/SpectralModels/burrows06/*.txt','reference/SpectralModels/drift/*.txt', \
            'reference/SpectralModels/morley12/*.txt','reference/SpectralModels/morley14/*.txt', \
            'reference/SpectralModels/saumon12/*.txt']
  },
#    include_package_data == True,

  zip_safe = True,
  use_2to3 = False,
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Astronomy',
      'Topic :: Scientific/Engineering :: Physics'
  ],

  # metadata for upload to PyPI
  author = "Adam Burgasser",
  author_email = "aburgasser@ucsd.edu",
  description = "SpeX Prism Library Analysis Toolkit",
  license = "MIT",
#    download_url='%s/astropy-%s.tar.gz' % (DOWNLOAD_BASE_URL, VERSION),
  keywords = ['splat','spectroscopy', 'spectral analysis', 'astronomy','astrophysics',\
              'ultracool dwarfs','low mass stars', 'brown dwarfs', 'spex','prism', 'classification'],
  url = "http://www.browndwarfs.org/splat/",   # project home page, if any


)
