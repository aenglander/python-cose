from setuptools import find_packages
from setuptools import setup

setup(
    name="python-cose",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["cryptography>=2.0"],
    url="https://github.com/aenglander/python-cose",
    license="MIT",
    author="Adam L. Englander",
    author_email="adamenglander@yahoo.com",
    description="CBOR Object Signing and Encryption Library for Python "
    "utilizing PyCA cryptography",
)
