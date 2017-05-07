import re
import setuptools


setuptools.setup(
    name='pyyasm',
    version='0.0.1',
    description='Wrapper around yasm',
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