import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='extmath',
    version='0.9',
    author='Nattawut Phetmak',
    # author_email='',
    description='Collections of useful tools in mathematics.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/neizod/extmath',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
