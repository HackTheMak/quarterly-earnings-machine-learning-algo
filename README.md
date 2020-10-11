# Updated corrections
This program does work, but requires some corrections in order to operate due to versionings.

The code in this fork has the fixes.

Also, be sure to create the following sub-folders, as the code does not create them as given in the postings:
- filings
- cleaned_filings
- whole_file_diffs

# For Python3 Environment
This was tested using Linux Mint v19, which would work with Linux Ubuntu v20.

Python3 is been installed into the base O/Ss and therefore just need the following applications. Run the following commands:

- sudo apt-get install python3-pip
- sudo apt-get install python3-pandas
- sudo pip3 install yfinance
- sudo pip3 install fuzzywuzzy
- sudo pip3 install numpy
- sudo pip3 install python-edgar
- sudo pip3 install nltk
- python3 -c 'import nltk; nltk.download("punkt")'
- pip3 install python-Levenshtein

Follow the instructions from the links below, but use "python3" pr "pip3" when the command line instructions have "python" or "pip".

# quarterly-earnings-machine-learning-algo

Original Usage guide here: https://www.platorsolutions.com/post/full-guide-build-a-commission-free-algo-trading-bot-by-machine-learning-quarterly-earnings-reports

or

Updated Usage guide here: https://towardsdatascience.com/build-a-commission-free-algo-trading-bot-by-machine-learning-quarterly-earnings-reports-full-b414e5d759e8


Ticker.txt downloaded from https://www.sec.gov/include/ticker.txt

# Comparisions (GoogleML Natural Language Sentiment)
Results of 2 Years of Data
- Overall Precision/Recall: 26.71%
- Sentiment Score 0 Precision: 31.5%
- Sentiment Score 0  Recall: 51.03%

Results of 10 Years of Data (from article)
- Overall Precision/Recall: 29.38%
- Sentiment Score 0 Precision: 35.63%
- Sentiment Score 0  Recall: 60.78%

Results of 20 Years of Data (ongoing)
- Overall Precision/Recall: 
- Sentiment Score 0 Precision: 
- Sentiment Score 0  Recall: 

# NOTE: Hardware Stats
The process does take a long time, days for the Ma/K's case.
2 years of records took about 3 days with the use of 12 CPU cores and 16GB RAM.
20 years is still ongoing with about one week to pull the records from the SEC.
So, this takes patience to gather and compile those reports.
