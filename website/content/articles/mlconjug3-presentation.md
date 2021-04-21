Title: Presentation of the python package mlconjug3
Category: Python
Date: 2021-04-19
Tags: Python, Machine Learning, Natural Language processing, AI, Conjugation, Linguistics
Slug: mlconjug3-presentation
Author: SekouDiaoNlp
Summary: Presentation of my NLP project mlconjug, a Python library for conjugating verbs in several languages.
lang: en
order: 001

[TOC]

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



<br />

## Academic publications citing mlconjug3




-   Ali Malik and Mike Wu and Vrinda Vasavada and Jinpeng Song and John
    Mitchell and Noah D. Goodman and Chris Piech.  
    "[Generative Grading Neural Approximate Parsing for Automated Student Feedback](https://arxiv.org/abs/1905.09916)".   
    Proceedings of the 34th AAAI conference on Artificial Intelligence, 2019.


<br />

## Software projects using mlconjug3



-   [Gender Bias Visualization](https://github.com/GesaJo/Gender-Bias-Visualization)
    This project offers tools to visualize the gender bias in
    pre-trained language models to better understand the prejudices in
    the data.  
    
-   [Text Adaptation To Context](https://github.com/lzontar/Text_Adaptation_To_Context) 
    This project uses language models to generate text that is well
    suited to the type of publication.  
    
-   [Facemask Detection](https://github.com/samuel-karanja/facemask-derection) 
    This project offers a model which recognizes covid-19 masks.  
    
-   [Bad Excuses for Zoom Abuses](https://github.com/tyxchen/bad-excuses-for-zoom-abuses) 
    Need an excuse for why you can't show up in your Zoom lectures? Just
    generate one here!  
    
-   [NLP](https://github.com/pskshyam/NLP) Repository to store
    Natural Language Processing models.  
    
-   [Virtual Assistant](https://github.com/JeanExtreme002/Virtual-Assistant) 
    This is a simple virtual assistant. With it, you can search the
    Internet, access websites, open programs, and more using just your
    voice. This virtual assistant supports the English and Portuguese
    languages and has many settings that you can adjust to your liking.  
    
-   [Bad Advice](https://github.com/matthew-cheney/bad-advice) This
    python module responds to yes or no questions. It dishes out its
    advice at random. Disclaimer: Do not actually act on this advice
    ;)  
    
-   [Spanish Conjugations Quiz](https://github.com/williammortimer/Spanish-Conjugations-Quiz)
    Python+Flask web app that uses mlconjug to dynamically generate
    foreign language conjugation questions.  
    
-   [Silver Rogue DF](https://github.com/FranchuFranchu/silver-rogue-df)  
    A dwarf-fortress adventure mode-inspired rogue-like Pygame Python3
    game


<br />

## BibTeX citation




If you want to cite mlconjug3 in an academic publication use this
citation format:



    :::bibtex
    @article{mlconjug3,  
          title={mlconjug3},  
          author={Sekou Diao},  
          journal={GitHub. Note: https://github.com/SekouDiaoNlp/mlconjug3 Cited by},  
          year={2021}  
        }



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