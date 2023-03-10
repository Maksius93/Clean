from setuptools import setup, find_namespace_packages

setup(name="clean_folder",
      version=1.0,
      description="App for clean folder in given path",
      author="Go IT_Student Max Fursa",
      author_email="m.g.fursa.gmail.com",
      license="MIT",
      packages=find_namespace_packages(),
      entry_points={"console_scripts": ["clean-folder=clean_folder.sort:main"]})
