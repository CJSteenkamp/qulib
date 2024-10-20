from setuptools import setup, find_packages

setup(
    name='qulib',
    version='0.2',
    packages=find_packages(),
    install_requires=['numpy'],
    tests_require=['pytest'],
    test_suite='tests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

# p setup.py sdist bdist_wheel
# twine upload dist/*