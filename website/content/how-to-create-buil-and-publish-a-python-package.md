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

So you have a great idea to create a Python package that could be useful to many people, and you want to  make it available to the public.

That's a great idea and will allow you to share your work with the world and maybe achieve great success and create a community of users and contributors around your product.

However, the process of creating, building and publishing a python process might be tedious and time-consuming.

You can find the information about how to achieve this on the interwebz, but it requires a lot of google-fu, and the relevant information is scattered over many websites.

In this tutorial I will explain how to do that in a detailed and easy to follow step-by-step procedure.


## INSTALL GIT AND CREATE A GITHUB ACCOUNT:

[Git](https://git-scm.com/downloads) is a Source Control System and [GitHub](https://github.com/) is a collaborative platform which allows multiple developers to work
on the same projects as well as sharing your code with the world.

You can download and install [git](https://git-scm.com/downloads) by clicking on the link and follow the installation instructions.

Create an account on [GitHub](https://github.com/) by clicking on the link.

## INSTALL A PYTHON DISTRIBUTION:

I recommend using the Python distribution created by Anaconda as this is a great Python distribution and provides
pre-compiled packages for many python packages, especially scientific packages bundled with libraries written in C,
C++, Fortran, Go, etc...

It is really easy to use and by using Anaconda you don't need to have compilers installed on your computer,
which can be a big hassle especially on Windows systems.

The Anaconda distributions comes in 2 flavors:

- The main distribution is [Anaconda ](https://www.anaconda.com/products/individual#Downloads) [Miniconda]. It comes pre-bundled with over 1500 scientific packages automatically installed at once.  
 It takes time to download and install and takes a large amount of disk space (a few minutes and 3 GB),  
 But you won't need to install each of the packages you want to use individually.
- The other distribution is [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html). It comes pre-bundled with just the core Python and a few packages.

You can install your chosen distribution by clicking on their link and following the installation instructions provided on
their website.

Once Anaconda/Miniconda is installed, you need to add the [conda-forge](https://conda-forge.org/) channel to your list of package repositories:

    :::python
    $ conda config --add channels conda-forge
    $ conda config --set channel_priority strict

For faster installation of conda packages use [mamba](https://github.com/mamba-org/mamba) instead of conda:

    :::python
    $ conda install mamba -n base -c conda-forge

Next you will need to create the base folder structure of your project.

Install a tool called [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html).
This is a command-line utility that creates projects from a Python package project template.

    :::python
    $ mamba install cookiecutter -y

Then create your package structure by cloning a Cookiecutter project template:

    :::console
    $ git clone git@github.com:audreyr/cookiecutter-pypackage.git

Modify the variables defined in cookiecutter.json and have a look at the project structure if you want to make some changes.

[Create a new repository](https://github.com/new) on GitHub named as the name of your package then push your newly created
project folder to this new repository.

Then generate your project from the project template:

    :::python
    $ cookiecutter <path/to/my/project>/

To create a new virtual environment:

    :::python
    $ conda create -n myenv python=3.x

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