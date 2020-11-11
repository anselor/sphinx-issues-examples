#
# coding=utf-8

import os
import setuptools

#
# get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='issue-typevar-ns',
    version='0.0.1',

    description='Hello World',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='hello world',

    author='Eric Lin',
    author_email='anselor@gmail.com',
    url='',
    license='MIT',

    packages=['issue'],

    python_requires='>=3.4',
    install_requires=[],
    setup_requires=['setuptools_scm'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    # dependencies for development and testing
    # $ pip install -e .[dev]
    extras_require={
        'dev': ['sphinx']
    },
)
