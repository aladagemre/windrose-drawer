WINDROSE DRAWING SCRIPTS
==========================

Plots windroses for given wind data. Inputs csv files. Sample csv file is given in test folder. You may have several csv files in one folder for bulk-processing.

Screenshots
=============

+![Figure 1](https://github.com/aladagemre/windrose-drawer/blob/master/test/plots/Nowhere_Wind-fig1.png)
+![Figure 2](https://github.com/aladagemre/windrose-drawer/blob/master/test/plots/Nowhere_Wind-fig2.png)
+![Figure 3](https://github.com/aladagemre/windrose-drawer/blob/master/test/plots/Nowhere_Wind-fig3.png)
+![Figure 4](https://github.com/aladagemre/windrose-drawer/blob/master/test/plots/Nowhere_Wind-fig4.png)
+![Figure 5](https://github.com/aladagemre/windrose-drawer/blob/master/test/plots/Nowhere_Wind-fig5.png)

REQUIREMENTS
==============
python matplotlib and numpy libraries are required.

If using linux,
    sudo pip install matplotlib numpy
will install the requirements.

If using Windows,
Install this IDE and run the code in it:

http://orange.biolab.si/download/orange-win-w-python-snapshot-hg-2014-05-13-py2.7.exe


INSTRUCTIONS
    
=============================================================

    python process.py test
    
will produce plots for csv files in test/ folder. Resulting plots will be put in test/plots/ folder.    

Use this command for any folder you'd like to process.


============================================================

If you have two seperate datasets: data and dust, you will use the following commands.
    
    python process.py data

will produce plots for csv files in data/ folder. Resulting plots will be put in data/plots/ folder.

    python process.py dust

will produce plots for csv files in dust/ folder. Resulting plots will be put in dust/plots/ folder.


* Make sure Dust files have filename in the form of Dust_City_Wind.csv and study filenames are City_Wind.csv

