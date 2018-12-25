import setuptools
from os.path import dirname, join

setuptools.setup(
    name="optimus",
    version="0.0.1",
    author="Akhil Harihar",
    author_email="akhil01@live.com",
    description="Python port of jenssegers/optimus Id obfuscation php package",
    long_description=open(join(dirname(__file__), 'README.md'), encoding='utf-8').read(),
    url="https://github.com/akhilharihar/optimus",
    license="MIT License",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        
    ],
)