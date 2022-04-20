======================================
piepy - Preprocessing Intracranial EEG
======================================

|ProjectStatus|_ |Version|_ |BuildStatus|_ |Coverage|_ |License|_ |PythonVersions|_

.. |ProjectStatus| image:: https://www.repostatus.org/badges/latest/active.svg
.. _ProjectStatus: https://www.repostatus.org/#active

.. |Version| image:: https://img.shields.io/pypi/v/piepy.svg
.. _Version: https://pypi.python.org/pypi/piepy/

.. |BuildStatus| image:: https://github.com/piepy-tools/piepy/actions/workflows/build.yml/badge.svg
.. _BuildStatus: https://github.com/piepy-tools/piepy/actions/workflows/build.yml

.. |Coverage| image:: https://codecov.io/gh/piepy-tools/piepy/branch/main/graph/badge.svg
.. _Coverage: https://codecov.io/gh/piepy-tools/piepy

.. |License| image:: https://img.shields.io/pypi/l/piepy.svg
.. _License: https://opensource.org/licenses/Apache-2.0

.. |PythonVersions| image:: https://img.shields.io/pypi/pyversions/piepy.svg
.. _PythonVersions: https://pypi.python.org/pypi/piepy/


piepy is a module for preprocessing iEEG data.

Overview
--------

``piepy`` is a pipeline for preprocessing iEEG data.

Documentation
-------------

Documentation for ``piepy`` is available on the
`documentation site <https://piepy-tools.github.io/piepy/index.html>`_.

This documentation includes:

- `Tutorials <https://piepy-tools.github.io/piepy/auto_tutorials/index.html>`_:
  with a step-by-step guide through the approach and how to apply it
- `Examples <https://piepy-tools.github.io/piepy/auto_examples/index.html>`_:
  demonstrating an example analysis and use case
- `API list <https://piepy-tools.github.io/piepy/api.html>`_:
  which lists and describes all the code and functionality available in the module
- `Glossary <https://piepy-tools.github.io/piepy/glossary.html>`_:
  which defines key terms used in the module

Dependencies
------------

``piepy`` is written in Python, and requires >= Python 3.6 to run.

It has the following dependencies:

- `neurodsp <https://github.com/neurodsp-tools/neurodsp>`_ >= 2.1.0
- `numpy <https://github.com/numpy/numpy>`_ >= 1.18.5
- `scipy <https://github.com/scipy/scipy>`_ >=  1.4.1
- `pandas <https://github.com/pandas-dev/pandas>`_ >= 0.25.3
- `matplotlib <https://github.com/matplotlib/matplotlib>`_ >= 3.0.3
- `pytest <https://github.com/pytest-dev/pytest>`_ (optional)

Install
-------

**Stable Version**

To install the latest stable release, you can use pip:

.. code-block:: shell

    $ pip install piepy

**Development Version**

To get the latest, development version, you can get the code using git:

.. code-block:: shell

    $ git clone https://github.com/piepy-tools/piepy

To install this cloned copy, move into the directory you just cloned, and run:

.. code-block:: shell

    $ pip install .

**Editable Version**

To install an editable, development version, move into the directory you cloned and install with:

.. code-block:: shell

    $ pip install -e .


Contribute
----------

This project welcomes and encourages contributions from the community!

To file bug reports and/or ask questions about this project, please use the
`Github issue tracker <https://github.com/piepy-tools/piepy/issues>`_.

To see and get involved in discussions about the module, check out:

- the `issues board <https://github.com/piepy-tools/piepy/issues>`_ for topics relating to code updates, bugs, and fixes

When interacting with this project, please use the
`contribution guidelines <https://github.com/piepy-tools/piepy/blob/main/CONTRIBUTING.md>`_
and follow the
`code of conduct <https://github.com/piepy-tools/piepy/blob/main/CODE_OF_CONDUCT.md>`_.

Quickstart
----------


.. code-block:: python

    import piepy

    # Load data

    # Run preprocessing


Funding
-------

Supported by NIH award R01 GM134363 from the
`NIGMS <https://www.nigms.nih.gov/>`_.

.. image:: https://www.nih.gov/sites/all/themes/nih/images/nih-logo-color.png
  :width: 400

|
