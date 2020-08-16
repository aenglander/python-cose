from distutils.core import setup

from setuptools import find_packages

setup(
    name="cose-python",
    version="0.1.0",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=["cryptography>=2.0"],
    url="https://github.com/aenglander/cose-python",
    license="MIT",
    author="Adam L. Englander",
    author_email="adamenglander@yahoo.com",
    description="CBOR Object Signing and Encryption Library",
)
