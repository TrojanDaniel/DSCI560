# DSCI560
Data Informatics Professional Practicum

HW4

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TrojanDaniel/DSCI560/master?filepath=hw2.ipynb)

Steps: 

1- Create a blank virtual environment and name it dsci560H4

  clone the repository from homework 2 to local
  
  pip install virtualenv 
 
  then execute virtualenv dsci540H4 in bash to create the virtual environment  
  
![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/1-1.png)




2- Activate the environment and install the dependencies 

  the activate.sh is in bin under dsci560H4
  
  execute source ./dsci560H4/bin/activate, then the virtual environment is activated
  
![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/1-2.png)

  for visualization, execute pip install matplotlib to download the required package

![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/matplotlib.png)




3- A screenshot of the terminal with the activated environment after running the script for the
number generator

execute python3 gen_dataset_a.py to run the script

![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/gen_dataset_a.png)




4- Extract the dependencies of your virtual environment
  
  a  These are dependencies installed in virtual environment
    
![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/requirements.png)
  
  Compared with manually installed matplotlib, there are many dependencies not related to our project are installed. 
  
  
  b  Create .gitignore to filter docs
  
  
  c  extract the dependencies' file by running pip freeze>requirements.txt
 
Remember to run deactivate to close virtual environment




5- Update/reuse the Jupyter notebook for Homework 2 and make sure it is executable in Binder (10p).
The notebook has to be executable, run end-to-end and include visualizations of the initial (2p), intermediate (4p) and final results (4p) used in Homework 2
   
   use mybinder to create the image for my github repository and link to hw2.ipynb
   
![image](https://raw.githubusercontent.com/TrojanDaniel/DSCI560/master/venv_screenshots/mybinder.png)   

execute  %run gen_dataset_a.py in Jupyter

execute  %run gen_dataset_b.py in Jupyter

execute  %run visualize.py in Jupyter


Visualizations are showed in the Jupyter Notebook after executing these commands. 





