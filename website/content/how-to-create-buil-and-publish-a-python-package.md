Title: How to create build and publish a Python package
Category: Python
Date: 2021-04-20
Tags: Python, Pypi, Anaconda, conda-forge
Slug: mlconjug3-presentation
Author: SekouDiaoNlp
Summary: A nifty tutorial about how to create build and publish a Python package.
lang: en
order: 002

# An easy step-by-step guide to build and publish Python packages.

## ANACONDA:

To create a new virtual environment:

    :::python
    $ conda create -n myenv python=3.x

For faster installation of conda packages use mamba instead of conda:

    :::python
    $ conda install mamba -n base -c conda-forge
    $ mamba install <packages>

## MANAGE DEPENDENCIES:

    :::python
    $ pip-upgrade requirements.txt requirements_dev.txt
    $ pipenv install --site-packages -r requirements.txt
    $ pipenv install --site-packages -r requirements_dev.txt --dev -e .
    $ pipenv update -r requirements.txt
    $ pipenv update -r requirements_dev.txt --dev -e .

## BUILD PYTHON PACKAGE:

    :::python
    $ bump2version patch --allow-dirty
    $ python setup.py sdist bdist_wheel
    $ twine check dist/*

## UPLOAD PYTHON PACKAGE:

    :::python
    $ twine upload dist/*

## GENERATE DOCUMENTATION AND GITHUB PAGE FROM THE DOCUMENTATION FOLDER:

    :::console
    $ make html

## CONDA-FORGE CONTRIBUTION:

(see <https://conda-forge.org/docs/maintainer/adding_pkgs.html> for more
details)

Fork <https://github.com/conda-forge/staged-recipes/tree/master/recipes>
Create a new branch from the staged-recipes master branch Generate a new
folder with &lt;your\_package\_name&gt; in the recipes subdirectory
Generate the recipe with the following command:

    :::python
    $ mamba install grayskull
    $ grayskull pypi <your_package_name>

Edit the file meta.yaml with the relevant information Create a Pull
Request to upload the recipe After the Pull Request is merged, a new
repository is created at [https://github.com/conda-forge/\\]

## CONDA-FORGE FEEDSTOCK MANAGEMENT:

Optionally add new remote:

    :::console
    $ git checkout master
    $ git remote add upstream https://github.com/conda-forge/<feedstock>
    $ git fetch upstream
    $ git checkout -b <branch-name>

make changes locally to the recipe and commit the changes:

    :::python
    $ conda smithy rerender -c auto
    $ git push origin <branch-name>

Create a Pull Request on [https://github.com/SekouDiaoNlp/\\] Merge the
Pull Request after all tests are successful

  [https://github.com/conda-forge/\\]: https://github.com/conda-forge/\
  [https://github.com/SekouDiaoNlp/\\]: https://github.com/SekouDiaoNlp/\