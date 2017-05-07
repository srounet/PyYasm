import os
import re
import setuptools


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()



setuptools.setup(
    name='pyyasm',
    version='0.0.1',
    description='A python Yasm Wrapper for x86 and x64.',
    long_description=long_description,
    author='Fabien Reboia',
    author_email='srounet@gmail.com',
    license = "BSD",
    url = "https://github.com/srounet/pyyasm",
    download_url = 'https://github.com/srounet/pyyasm/archive/0.0.1.tar.gz',
    packages = setuptools.find_packages(),
    package_data = {
        '': ['*.exe'],
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Assembly',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
    ],
)