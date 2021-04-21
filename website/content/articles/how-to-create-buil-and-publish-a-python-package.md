Title: How to create, build and publish a Python package
Category: Python
Date: 2021-04-20
Tags: Python, Pypi, Anaconda, conda-forge
Slug: How-to-create-build-and-publish-a-Python-package
Author: SekouDiaoNlp
Summary: A nifty tutorial about how to create build and publish a Python package.
lang: en
order: 002

# An easy step-by-step guide to build and publish Python packages.  
<br />

So you have a great idea to create a Python package that could be useful to many people, and you want to  make it available to the public.

<br />
That's a great idea and will allow you to share your work with the world and maybe achieve great success and create a community of users and contributors around your product.

<br />
However, the process of creating, building and publishing a python process might be tedious and time-consuming.

<br />
You can find the information about how to achieve this on the interwebz, but it requires a lot of google-fu, and the relevant information is scattered over many websites.

<br />
In this tutorial I will explain how to do that in a detailed and easy to follow step-by-step procedure.

<br />
<br />

## INSTALL GIT AND CREATE A GITHUB ACCOUNT:  
<br />

[Git](https://git-scm.com/downloads) is a Source Control System and [GitHub](https://github.com/) is a collaborative platform which allows multiple developers to work
on the same projects as well as sharing your code with the world.

<br />
You can download and install [git](https://git-scm.com/downloads) by clicking on the link and follow the installation instructions.

<br />
Create an account on [GitHub](https://github.com/) by clicking on the link.

<br />
<br />

## INSTALL A PYTHON DISTRIBUTION:  
<br />

I recommend using the Python distribution created by Anaconda as this is a great Python distribution and provides
pre-compiled packages for many python packages, especially scientific packages bundled with libraries written in C,
C++, Fortran, Go, etc...

<br />
It is really easy to use and by using Anaconda you don't need to have compilers installed on your computer,
which can be a big hassle especially on Windows systems, or more exotic architectures with ARM, PowerPC or AArch64 processors.

<br />
The Anaconda distributions comes in 2 flavors:

<br />

- The main distribution is [Anaconda ](https://www.anaconda.com/products/individual#Downloads) [Miniconda]. It comes pre-bundled with over 1500 scientific packages automatically installed at once.  
 It takes time to download and install and takes a large amount of disk space (a few minutes and 3 GB),  
 But you won't need to install each of the packages you want to use individually.
- The other distribution is [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html). It comes pre-bundled with just the core Python and a few packages.

<br />
You can install your chosen distribution by clicking on their link and following the installation instructions provided on
their website.

<br />

Once Anaconda/Miniconda is installed, you need to add the [conda-forge](https://conda-forge.org/) channel to your list of package repositories:

    :::python
    conda config --add channels conda-forge
    conda config --set channel_priority strict

<br />

For faster installation of conda packages use [mamba](https://github.com/mamba-org/mamba) instead of conda:

    :::python
    conda install mamba -n base -c conda-forge

<br />
<br />

## CREATE THE BASE FOLDER STRUCTURE OF YOUR PROJECT:  
<br />

Install a tool called [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html).
This is a command-line utility that creates projects from a Python package project template.

    :::python
    mamba install cookiecutter -y

<br />

Then create your package structure by cloning a Cookiecutter project template:

    :::console
    git clone git@github.com:audreyr/cookiecutter-pypackage.git

<br />

Modify the variables defined in cookiecutter.json and have a look at the project structure if you want to make some changes.

<br />

[Create a new repository](https://github.com/new) on GitHub named as the name of your package then push your newly created
project folder to this new repository.

<br />

Then generate your project from the project template:

    :::python
    cookiecutter <path/to/my/project template>/

<br />

You will be prompted to enter some project config values. (These are defined in the project’s cookiecutter.json.)

<br />

Then, Cookiecutter will generate a project from the template, using the values that you entered.
It will be placed in your current directory. Find detailed information [here](https://cookiecutter.readthedocs.io/en/1.7.2/first_steps.html).

<br />
<br />

## IT IS FINALLY TIME TO CODE 😎:  
<br />

You are now almost ready to code your awesome package. You just need to set up your development environment.

<br />
<br />

### CREATE A NEW VIRTUAL ENVIRONMENT:  
<br />

You need to first create a python virtual environment that will contain your project and all
its dependencies. This will prevent your needed dependencies to interfere with the main Python environment.

<br />

To create a new virtual environment:

    :::python
    conda create --name myenv python=3.x <optional packages that you want pre-installed in this virtual environment>

<br />

Where 'myenv' is the name of your virtual environment and replace 'python=3.x' by the python version you desire.

<br />

You can also specify a list of packages that you want pre-installed in this virtual environment and conda will install them automatically.

<br />

Once the virtual environment has been created, navigate to the root folder of your project and activate the new virtual environment:

    :::python
    conda activate myenv

<br />

Where 'myenv' is still the name of your virtual environment.

<br />

Modify the files 'setup.cfg' and 'setup.py' according to your needs.
You can find a helpful guide on how to do that [here](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html).

<br />
<br />

### ACTIVATE DEVELOPER MODE:  
<br />

In order to develop your package you need to make it editable so that any changes you made to the code are immediately
applied, and you can test and debug your code.

<br />

To enable this feature, while still in the root folder of your project (and making sure that your virtual environment is active)
type the following command:

    :::python
    pip install -e .

<br />
<br />

### START DEVELOPING YOUR CODE:  
<br />

You can now create and edit your code, add dependencies and run unit tests on your code to squash any bug that might be crawling around.

<br />

You can specify the dependencies that your package needs to run in a file called requirements.txt.

<br />

The dependencies on the tools you use while developing your package can be specified in a file called requirements_dev.txt.

<br />

You can find more information on the use of requirements files [here](https://pip.pypa.io/en/stable/user_guide/#requirements-files).

<br />

I **STRONGLY** advise you to write tests and run them regularly. I recommend using [pytest](https://pytest.org/) to run your tests.
The dependency on pytest is specified in requirements_dev.txt as it is only used during development.

<br />

You should put your tests in the 'test/' folder created by cookiecutter.

<br />
<br />

### MANAGE DEPENDENCIES:  
<br />

In order to manage your dependencies I recommend to use [pip-upgrader](https://github.com/simion/pip-upgrader):
It is a tool which allows you to automatically keep your dependencies up to date.

<br />

First install the dependencies you specified by typing these commands:

    :::python
    pip install -r requirements.txt
    pip install -r requirements_dev.txt

<br />

During the course of your development you can make sure that your dependencies are up to date by running this command from time to time:

    :::python
    pip-upgrade requirements.txt requirements_dev.txt

<br />

This will check on PyPi if there are newer versions of your dependencies and update the requirements files with the latest versions.
If it finds new version, you just need to reinstall your dependencies.

    :::python
    pip install -r requirements.txt
    pip install -r requirements_dev.txt

<br />

After a while you will be ready to build and publish your package. That's great news!

<br />
<br />

## GENERATE DOCUMENTATION FROM THE DOCUMENTATION FOLDER:  
<br />

I also **STRONGLY** advise you to write a good documentation for your project as it makes a great difference in the potential success of your project.

<br />

I recommend using [Sphinx](https://www.sphinx-doc.org/en/master/index.html) to autogenerate the documentation.
You can install it by typing:

    :::python
    pip install Sphinx

<br />

Once Sphinx is installed you can easily autogenerate the documentation for your project by navigating to the docs/ folder
of your project and running:

    :::console
    make html

<br />

This will auto-generate an html version of your documentation.
That's great but wouldn't it be better if your documentation was automatically uploaded to [readthedocs](https://readthedocs.org/) so that it is always available online?

<br />

Create an account [readthedocs](https://readthedocs.org/) and [follow their instructions](https://docs.readthedocs.io/en/stable/intro/import-guide.html)
on how to automatically upload your documentation to their site every time you release a new version of your package.

<br />

The documentation will be automatically available and always up to date at https://<your-package-name>.readthedocs.io/en/latest/index.html

<br />

You are now ready to build your package.

<br />
<br />

## BUILD THE PYTHON PACKAGE:  
<br />

I recommend using the tool [bump2version](https://pypi.org/project/bump2version/) to easily update the version number of your package.
You can install it by typing:

    :::python
    pip install bump2version

<br />

When you are ready to release a new version of your package, type:

    :::python
    bump2version <option>

<br />

Where <option> can be either major, minor or patch depending on how you want to update the version number.

<br />

Once you bumped the version number, it is time to build your package.
Run the following command to build your package. This will create both a source distribution and a binary distribution.

    :::python
    python setup.py sdist bdist_wheel

<br />

The built packages will be placed in the dist/ folder of your project.

<br />

Now It is time to distribute your package.

<br />
<br />

## UPLOAD YOUR PYTHON PACKAGE:  
<br />

You are ready to upload your package to [PyPi](https://pypi.org/) which is the official repository of Python packages.

<br />

You must first [create an account on PyPi](https://pypi.org/account/register/) to be able to upload your package.

<br />

The tool to upload your package is called [twine](https://twine.readthedocs.io/en/latest/). It is very easy to use.

<br />

To install twine, type the following command:

    :::python
    pip install twine

<br />

Once twine is installed, upload your package to PyPi by typing this command:

    :::python
    twine upload dist/*

<br />

This command will ask you for the username and password of your Pypi account.

<br />

You can alternatively create a file called [.pypirc](https://packaging.python.org/specifications/pypirc/) which contains
your configuration and credentials and use this command to upload your package:

    :::python
    twine upload --config-file <path/to/your/.pypirc> dist/*

<br />

Once uploaded to PyPi, your package will be able to be installed by people by simply typing:

    :::python
    pip install <your-package-name>

<br />

You have now successfully uploaded your package to Pypi.
This is great and now users can start to use your package!

<br />

But if you want your package to be even more widely available and be able to be installed on all platforms even exotic ones,
I advise you to also upload your package to [conda-forge](https://conda-forge.org/). This way your package will be also available on Anaconda.

<br />
<br />

## CONDA-FORGE CONTRIBUTION:  
<br />

In order to upload your package to [conda-forge](https://conda-forge.org/) see <https://conda-forge.org/docs/maintainer/adding_pkgs.html> for more
details.

<br />

I will give a quick rundown of how to achieve this:

<br />

Fork <https://github.com/conda-forge/staged-recipes/tree/master/recipes>

<br />

Create a new branch from the staged-recipes master branch.

<br />

Generate a new folder with &lt;your\_package\_name&gt; in the recipes subdirectory.

<br />

Generate the recipe for your package with the following command:

    :::python
    mamba install grayskull
    grayskull pypi <your_package_name>

<br />

This will grab the latest version of your package from PyPi and auto-generate the recipe to create a conda package.

<br />

Edit the file meta.yaml with the relevant information.

<br />

Create a Pull Request to upload the recipe.

<br />

After the Pull Request is merged, a new repository with your package is created at [https://github.com/conda-forge/\\]

<br />

You are now the maintainer of this repository.

<br />

You can now update this repository, and the changes you make will be automatically updated to conda-forge.

<br />
<br />

## CONDA-FORGE FEEDSTOCK MANAGEMENT:  
<br />

In order to efficiently manage your new package repository follow these instructions.

<br />

Optionally add a new remote:

    :::console
    git checkout master
    git remote add upstream https://github.com/conda-forge/<feedstock>
    git fetch upstream
    git checkout -b <branch-name>

<br />

Where <feedstock> is your package name <branch-name> is a new git branch where you will make your changes.

<br />

Make changes locally to the recipe and commit the changes:

    :::python
    conda smithy rerender -c auto

    :::console
    git push origin <branch-name>

<br />

Create a Pull Request on [https://github.com/<feedstock>/\\].

<br />

Merge the Pull Request after all tests are successful.

<br />

Your package is now available at [https://anaconda.org/conda-forge/your-package-name\\].
