from setuptools import setup, find_packages
import sys, os

if __name__ == '__main__':
    version = '0.0'
    setup(
        name = 'rfooConsoleUtil',
        version = version,
        description = "Helper tools for rfoo.utils.rconsole",
        classifiers = [],
        author = "SellerEngine Software",
        url = "https://github.com/sellerengine/rfooConsoleUtil",
        license = "MIT",
        packages = find_packages(exclude = ['*.test', '*.test.*']),
    )
