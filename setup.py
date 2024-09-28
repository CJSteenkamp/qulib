from setuptools import setup, find_packages

setup(
    name='Qulib',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    tests_require=['pytest'],
    test_suite='tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    url="https://github.com/CJSteenkamp/qulib",
    maintainer='CJ Steenkamp',
    maintainer_email='joshsteenkamp2407@gmail.com'
)

# p setup.py sdist bdist_wheel
# twine upload dist/*