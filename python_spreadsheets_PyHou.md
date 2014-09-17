#Python and Spreadsheets: State of the Union, Sept 2014 (*BETA*)
-  By Kojo Idrissa
    -  Rouge Pythonista
    -  Educator/Accountant

#Setup
-  Not a lot of code here
    +  Interesting code provided by the specific use case
-  Looking for feedback
    +  What else should be included?

#Three approaches + "Other"
-  Working with spreadsheet files
-  Using Python code IN a spreadsheet app
-  Scripting spreadsheet apps
-  Other: options I'm still investigating

#Working with spreadsheet files
-  OpenPyXL
    +  works with .xlsx files
    +  I've demoed a larger example program
-  [Python-Excel](http://www.python-excel.org) packages
    +  xlrd; xlwt; xlutils
    +  I believe these only work with *.xls files; need to double check as of Fall 2014

#Running Python code IN a spreadsheet app
-  The largest growth area: replacing VB with Python
-  [Python for Excel with PyXLL video (Enthought's Canopy plugin)](http://vimeo.com/89024595?utm_source=Python+Weekly+Newsletter&utm_campaign=42441d6a58-Python_Weekly_Issue_133_April_3_2014&utm_medium=email&utm_term=0_9e26887fc5-42441d6a58-312680573) pronounced "Pixel"
    +  Enthought's [PyXLL](https://www.enthought.com/products/pyxll/) page
    +  Webinar: [Webinar: Python for Excel with PyXLL](https://www.youtube.com/watch?v=0RzTsvBIhaE)
        *  Centralized management of functions used in your spreadsheets. This is difficult to do with Excel, where each person uses their own formulas or VBA code
        *  Centralized version control
    +  Enthought PyXLL webinar: [Supercharging Excel Analytics with Python](http://www.youtube.com/watch?v=lGjFCTrd-AQ&utm_source=Python+Weekly+Newsletter&utm_campaign=4d7e0202aa-Python_Weekly_Issue_156_September_11_2014&utm_medium=email&utm_term=0_9e26887fc5-4d7e0202aa-312680573)
-  xlwings and ExcelPython
    +  First five mintues of these [EuroPython 2014 Lightning Talks](http://www.youtube.com/watch?v=qDzeSGv28kU&feature=youtu.be&t=35s) focuses on these two packages. The authors are planning to merge them.
    -  xlwings: [Replace your VBA code with Python](http://xlwings.org/?utm_source=Python+Weekly+Newsletter&utm_campaign=42441d6a58-Python_Weekly_Issue_133_April_3_2014&utm_medium=email&utm_term=0_9e26887fc5-42441d6a58-312680573)
    -  [ExcelPython: call Python scripts from Excel/VBA](https://github.com/ericremoreynolds/excelpython)
+  [PyInEx](https://www.pytexas.org/2014/talks/35/); Python interpreter embedded IN Excel!!
    *  I won't talk about this, because there's already an entire presentation on it [scheduled for Sunday at 1pm](https://www.pytexas.org/2014/talks/35/). You should go see that. :-)
    *  Google Code page is [here](https://code.google.com/p/pyinex/)

#Scripting spreadsheet apps (still researching)
+  Open/LibreOffice (via PyUno) 
    *  https://wiki.openoffice.org/wiki/PyUNO_bridge#Tutorial
    *  https://wiki.openoffice.org/wiki/Python
    *  https://www.google.com/search?client=safari&rls=en&q=libreoffice+python+uno&ie=UTF-8&oe=UTF-8&gfe_rd=cr&ei=UpvtU-WtLefU8gfDmIGoBg
    *  http://en.wikipedia.org/wiki/Universal_Network_Objects
    *  https://pypi.python.org/pypi/unotools/0.3.2
    *  http://api.libreoffice.org/examples/examples.html#python_examples
    *  [UNOTools](https://bitbucket.org/t2y/unotools)

#Other (still researching)
*  Google Docs spreadsheets with Python?
-  PeeWee to explore CSV files?
    +  http://charlesleifer.com/blog/using-peewee-to-explore-csv-files/
    +  http://peewee.readthedocs.org/en/latest/peewee/playhouse.html#csv-loader
-  Other CSV file options
    +  Not my preferred approach
