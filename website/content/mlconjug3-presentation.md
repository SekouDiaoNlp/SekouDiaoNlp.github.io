Title: mlconjug3-presentation
Category: Python
Date: 2021-04-19
Tags: Python, Machine Learning, Natural Language processing, AI, Conjugation
Slug: mlconjug3-presentation
Author: SekouDiaoNlp
Summary: Presentation of my NLP project mlconjug, a Python library for conjugating verbs in several languages.
lang: en
order: 001

I am making this post to present to the world my Python library which has the best AI (as far as I know)
capable of conjugating verbs in several languages.
You can find below a summary of what it can achieve.

# MLCONJUG3

[![Package Maintenance Status]][1]  [![Package Maintener]][2]  [![Build status on Windows, MacOs and Linux]][3]

[![Pypi Python Package Index Status]][4]  [![Anaconda Package Index Status]][5]  [![Compatible Python versions]][4]

[![Documentation Status]][6]  [![Dependencies status]][7]  [![Code Coverage Status]][8]  [![Code Vulnerability Status]][9]

[![Supported platforms]][5]


A Python library to conjugate verbs in French, English, Spanish,
Italian, Portuguese and Romanian (more soon) using Machine Learning
techniques.  
Any verb in one of the supported language can be conjugated, as the
module contains a Machine Learning model of how the verbs behave.  
Even completely new or made-up verbs can be successfully conjugated in
this manner.  
The supplied pre-trained models are composed of:

-   a binary feature extractor,
-   a feature selector using Linear Support Vector Classification,
-   a classifier using Stochastic Gradient Descent.

mlconjug3 uses scikit-learn to implement the Machine Learning
algorithms.  
Users of the library can use any compatible classifiers from
scikit-learn to modify and retrain the models.

  [Package Maintenance Status]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
  [1]: https://GitHub.com/SekouDiaoNlp/mlconjug3/graphs/commit-activity
  [Package Maintener]: https://img.shields.io/badge/maintainer-SekouDiaoNlp-blue
  [2]: https://GitHub.com/SekouDiaoNlp/mlconjug3
  [Build status on Windows, MacOs and Linux]: https://github.com/SekouDiaoNlp/mlconjug3/workflows/mlconjug3/badge.svg
  [3]: https://github.com/SekouDiaoNlp/mlconjug3/actions
  [Pypi Python Package Index Status]: https://img.shields.io/pypi/v/mlconjug3.svg
  [4]: https://pypi.python.org/pypi/mlconjug3
  [Anaconda Package Index Status]: https://anaconda.org/conda-forge/mlconjug3/badges/version.svg
  [5]: https://anaconda.org/conda-forge/mlconjug3
  [Compatible Python versions]: https://img.shields.io/pypi/pyversions/mlconjug3
  [Supported platforms]: https://img.shields.io/conda/pn/conda-forge/mlconjug3?color=dark%20green&label=Supported%20platforms
  [Documentation Status]: https://readthedocs.org/projects/mlconjug3/badge/?version=latest
  [6]: https://mlconjug3.readthedocs.io/en/latest
  [Dependencies status]: https://pyup.io/repos/github/SekouDiaoNlp/mlconjug3/shield.svg
  [7]: https://pyup.io/repos/github/SekouDiaoNlp/mlconjug3/
  [Code Coverage Status]: https://codecov.io/gh/SekouDiaoNlp/mlconjug3/branch/master/graph/badge.svg
  [8]: https://codecov.io/gh/SekouDiaoNlp/mlconjug3
  [Code Vulnerability Status]: https://snyk-widget.herokuapp.com/badge/pip/mlconjug3/badge.svg
  [9]: https://snyk.io/test/github/SekouDiaoNlp/mlconjug3?targetFile=requirements.txt