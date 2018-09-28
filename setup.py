from distutils.core import setup

install_requires = []

setup(
    name='ppj',
    version='0.0.1',
    description='Pretty print loosely JSON formatted logs stored in the clipboard',
    author='Alan So',
    author_email='alansoandso@gmail.com',
    packages=['ppjson'],
    scripts=['scripts/ppj'],
    install_requires=install_requires
)
