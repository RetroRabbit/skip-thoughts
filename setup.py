#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file for long description
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='Skip Thoughts',
      version='1.0',
      description='Sent2Vec encoder and training code from the paper Skip-Thought Vectors.',
      author='Ryan Kiros',
      url='https://github.com/ryankiros/skip-thoughts',
      long_description=read('README.md'),
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['theano','keras','nltk','scikit-learn','gensim','scipy']
     )