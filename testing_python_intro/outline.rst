Intro to Testing Python
========================

What is "testing"?
-------------------
-  Defined
-  Functional vs Integration testing

    +  Functional: from the user perspective
    +  Integration: does this code work as expected?
        +  I'll focus on Integration Testing
   

Why would I do this?
--------------------
-  REQUIRES a deeper understanding and analysis of
    -  what your code does
    -  how it does it 
-  Code works now, don't break it if you add to it
-  ``Software Engineering`` > ``Typin' and Hopin'`` 
   
How would I do this?
--------------------
-  Python's built-in tools
    -  Doctest
    -  Unittest
-  Other tools (brief mention)
    -  `Nose <https://nose.readthedocs.org/en/latest/>`_ ("in maintenance mode for the past several years") vs `Nose2 <https://nose2.readthedocs.org/en/latest/>`_ (the successor)
    -  `Pytest <http://pytest.org/latest/>`_: The new hotness
    -  `Unittest2 <https://pypi.python.org/pypi/unittest2>`_
    -  I'll focus on Python3 tools cuz that's the future.

        +  But my example code will be in Python 2.7 cuz Twillio is NOT in the future. :-(

*  Methods

    -  How do you write tests?

        +  TDD Testing Cycle

            *  Write test, run test
            *  Test Fails
            *  Write enough code to pass test
    -  What are you testing for, specifically?
    -  What AREN'T/SHOULDN'T you test?
    -  On to EXAMPLES!!!

EXAMPLE CODE!!
-------------------
-  `My Die-rolling app <https://github.com/kojoidrissa/helloflask>`_

Doctest: your first step into testing AND documentation
-------------------------------------------------------
-  You should be documenting your functions anyway
-  Simplest way to start testing


Unittest: Testing SMALLTALK style! (like Gangnam Style...but with testing)
---------------------------------------------------------------------------

-  An "`xUnit <https://en.wikipedia.org/wiki/XUnit>`_" style of testing. Based on SUnit from Smalltalk
-  test isolation: why unittest creates a NEW object for EACH test method
-  mocking: because you can't test The Internet


Other Tools of Note
-------------------------------
-  I'll evaluate them to see how useful I think they'll be to new developers. I haven't used ANY of these yet

    +  `Coverage <https://coverage.readthedocs.org/en/coverage-4.0.3/>`_: is all the code being tested?
    +  `Mcabe <https://pypi.python.org/pypi/mccabe>`_: How complex is your code?
    +  `PyFlakes <https://pypi.python.org/pypi/pyflakes>`_, `Pep 8 <https://www.python.org/dev/peps/pep-0008/>`_ & `Flake8 <https://pypi.python.org/pypi/flake8>`_: Because style matters


References
***********
-  `Python 3.4 Doctest docs <https://docs.python.org/3.4/library/doctest.html>`_
-  `Doctest Introduction <http://pythontesting.net/framework/doctest/doctest-introduction/>`_
-  `Testing through documentation <https://pymotw.com/2/doctest/>`_
-  `Python 3.4 Unittest docs <https://docs.python.org/3.4/library/unittest.html#>`_

    +  `TestCase class docs <https://docs.python.org/3.4/library/unittest.html#unittest.TestCase>`_

-  `Ned Batchelder: Getting Started Testing - PyCon 2014 <https://www.youtube.com/watch?v=FxSsnHeWQBY>`_

    +  Ned's `notes <http://nedbatchelder.com/text/test0.html>`_ from that talk.

Give credit where it's due
---------------------------
-  `Python Testing <http://pythontesting.net/>`_
-  `Obey The Testing Goat! <http://www.obeythetestinggoat.com/>`_

    +  `TDD Resources <http://www.obeythetestinggoat.com/pages/tdd-resources.html>`
