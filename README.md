# README FOR SCRAPING PRACTICE EXAMS
##### By: Andrew Hariri
###### Purpose: I noticed that there were a bunch of pdf practice exams available for CSCI 201, but I didn't want to manually download all of them
###### Disclaimer: This guide is heavily geared towards Mac users.

### PRE-INSTALLATION

##### Before you start make sure you have already installed the following:
1.  Homebrew Package Manager
    *   if you are on mac, make sure you have `homebrew` installed
        *   to install homebrew, please refer to the guide here: <https://brew.sh/>
2.  `python3`
    *   if you don't have it installed you can run `$ brew install python`
    *   it is possible to have several versions of python on your computer (ie. mac's often come with python 2.6 and up) so on your command line run `$ python --version` to check which version of python you have
        *   if it comes back with `python 2.x.x` (this happened to me) you will need to establish aliases for `python` and `pip`
            *   enter permanent aliases by typing `$ nano source ~/.bash_profile`
                *   make sure the header at the top says `File: /Users/yourUserName/.bash_profile`
                    *   if it doesn't, try doing `ctrl X`
            *   then create an area for aliases and add the following:
                *   Comments start with `#` so you can section off an area like `#--- Aliases ---#`
                *   `alias python="python3"`
                *   `alias pip="pip3"`
            *   `ctrl O` to save your aliases, then click `enter`
            *   `ctrl X` to exit
            *   you should now be good to go
        *   otherwise, your running python3 and you're good to go!
3.  The python `requests` module
    *   if you have pip (python's package manager), you can simply do `$ pip install requests`
    *   to double check you have the most recent version, do `$ pip install requests --upgrade`

### INSTALLATION
1.  git clone the file into the directory where you want to save all of your practice midterms/finals
    - ie. run `git clone git@github.com:hariria/Scrape-Exams-CSCI-201.git`
        - if permission is denied, try running `git clone https://github.com/hariria/Scrape-Exams-CSCI-201.git`
2.  then `cd` into that directory and run `python scrapeExams.py` on your terminal
3.  Hopefully it should work!
