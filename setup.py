from setuptools import setup,find_packages

setup(name="census-income",
      version="0.01",
      author="fezphantom",
      author_email="fezphantom@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","flask","numpy"])