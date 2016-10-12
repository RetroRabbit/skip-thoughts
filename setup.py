#!/usr/bin/env python

from distutils.core import setup

setup(name='Skip Thoughts',
      version='1.0',
      description='Sent2Vec encoder and training code from the paper Skip-Thought Vectors.',
      author='Ryan Kiros',
      url='https://github.com/ryankiros/skip-thoughts',
      packages=['skipthoughts', 'skipthoughts.training','skipthoughts.decoding'],
      install_requires=['theano','keras','nltk','scikit-learn','gensim','scipy']
     )