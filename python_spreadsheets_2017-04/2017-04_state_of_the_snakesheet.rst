Python and Spreadsheets: State of the Union, Apr 2017
=====================================================
Kojo Idrissa
-------------
-  QA Specialist for Decisio Health
-  Former Educator & Accountant w/ an MBA
-  `@transition <https://twitter.com/transition>`_

Setup
=======
-  Not a lot of advanced code here
-  Very beginner-friendly
-  Interesting code provided by *your* specific use case

Context/Background
==================
-  My role as a Python contributor
    *  Grow the community
    *  Bring non-programmers into the fold
-  Solutions for people who aren't professional developers
    *  Solutions obvious to experienced developers often aren't available to non-developers

Two primary audiences
=====================
-  Spreadsheet users who want to "step their game up"

-  Python developers confronted with spreadsheets

Three Basic Approaches
=======================

-  Working with spreadsheet files (my focus)
-  Running Python code in a spreadsheet app: our Lightning Talk on `xlwings <https://www.xlwings.org/>`_
-  Scripting spreadsheet apps: theoretically possible with OpenOffice & LibreOffice, `just not easy <https://onesheep.org/scripting-libreoffice-python/>`_


Working with spreadsheet files
===============================
-  `Python-Excel.org <http://www.python-excel.org>`_ web site collects info for working with Excel files
-  Use case: You've been given a spreadsheet full of data to process, but not in a way that's convenient in your spreadsheet app.
    +  Perfect entry point for creating new Pythonistas. Spreadsheet hackers are ALMOST programmers *(kinda)*.
-  `OpenPyXL <http://pythonhosted.org//openpyxl/>`_
    +  get it from `PyPi <https://pypi.python.org/pypi/openpyxl>`_ 
    +  Python >=2.6
    +  works with .xlsx & .xlsm files
+  Let's look at some examples!

Simple
=======
-  reading well-structured data
-  reading & writing well-structured data

Intermediate
=============

Advanced/My Current Task
=========================
-  semi-structured data to JSON