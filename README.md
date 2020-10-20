# Updated corrections
This program does work, but requires some corrections in order to operate due to versionings.

The code in this fork has the fixes.

Also, be sure to create the following sub-folders, as the code does not create them as given in the postings:
- filings
- cleaned_filings
- whole_file_diffs

And when the code has been place, need to make the following edits to the gcp_automl_predictor.py file (replace the Insert Here words)
- project_id: (Line 11) Insert your Project ID from the Google Predict.py into the Quotes. Just the unquie characters.
- model_id: (Line 12) Insert your Model ID from the Google Predict.py into the Quotes. Just the unquie characters.

Example From Google of Execute the Request field: projects/121212121212/locations/us-central1/models/LNG121212121212121212121212
- project_id = "121212121212"
- model_id = "LNG121212121212121212121212"

# For Python3 Environment
This was tested using Linux Mint v19, which would work with Linux Ubuntu v20.

Python3 is been installed into the base O/Ss and therefore just need the following applications. Run the following commands:

- sudo apt-get install python3-pip
- sudo apt-get install python3-pandas
- sudo pip3 install bs4
- sudo pip3 install yfinance
- sudo pip3 install fuzzywuzzy
- sudo pip3 install numpy
- sudo pip3 install python-edgar
- sudo pip3 install nltk
- python3 -c 'import nltk; nltk.download("punkt")'
- pip3 install python-Levenshtein
- python3 -m pip install "dask[complete]"
- pip3 install google-api-core
- pip3 install google-api-python-client
- pip3 install google-cloud-automl
- pip3 install google-cloud-storage
- pip3 install alpaca_trade_api

Follow the instructions from the links below, but use "python3" or "pip3" when the command line instructions have "python" or "pip".

# Bug with YFinance (and the Fix)
There is a bug with YFinance in that some of the stocks will not be reported, due to not having all of the available information (or missing some of it). To rectify this, use either of these codes.

Go to the yfinance base.py file (/usr/lib/python3.8/dist-packages/yfinance/base.py)

Edit line 286:
- Old Line: self._institutional_holders = holders[1]
- New Line:  self._institutional_holders = holders[1] if len(holders) > 1 else[]

Or use this set of codes:
- https://github.com/ranaroussi/yfinance/issues/208#issuecomment-608284124


# Create a Service Account for Google ML
With the instructions below and of the current code in this fork, a Service Account will need to be created.
When at the Google Cloud Platform part of the article(s) below, to create the Service Account:
- Click on the three horizontal lines left of the Google Cloud Platform menu bar.
- Click on IAM & Admin > Then Click on Service Accounts
- Provide a Name for the account
- Leave the Service Account ID as is, it should be already set to the project
- Provide a description if you like
- Click on Create
- Select Role: AutoML - Predictor
- Click on Continue
- Click on Update
- Download the JSON key file
- Once downloaded, move the json file to a preferred place or within this script's folder.
- Edit the file, "gcp_automl_predictor.py"
- Insert the path and filename of the json file into the quotes of line 14
- Example: os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/MyUserName/Python/Algo/MySecFile.json"

# To Run the MakeTrades.py Script
Run the script with the following command:
- python3 MakeTrades.py --keys InsertYourAlpacaIDHere --secret InsertYourAlpacaSecretKeyHere --model InsertYourFullGoogleModelNameHere
- Example: python3 MakeTrades.py --keys FGDFGSDFGHSDFGSD --secret AGFDGasdaf3243wfsaDSFSAADFA345sSDRSEss --model projects/121212121212/locations/us-central1/models/LNG121212121212121212121212

# Original Articles with Instructions for the quarterly-earnings-machine-learning-algo
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

Results of 20 Years of Data
- Overall Precision/Recall: 31.2%
- Sentiment Score 0 Precision: 33.96%
- Sentiment Score 0  Recall: 28.82%

# NOTE: Hardware Stats
The process does take a long time, days for the Ma/K's case.
2 years of records took about 3 days with the use of 12 CPU cores and 16GB RAM.
20 years took about two weeks. Judging from the results, just go with 2 to 10 years worth of data.

# Results
So far, with just the 2 years of records for the Googgle AutoML and 5 days of testing, it was able to give Short Indicators for LOOP, TSRI and NNPP (but has changed tickers). However, both LOOP and TSRI are not 'shortable' with Alpaca, most likely due to the negative news which dove LOOP prices down (about one week after the Q-10 report) and TSRI is pretty much a penny stock. Though do note, that the program worked correctly for LOOP. The report was on Oct 7th 2020 and had a price drop the next few days (before the big bombshell news story on the 13/14th of October.).

However, the question becomes, how often does the AutoML fail to provide a Result of "0" for reports, which should be rated as such? 

Although, even with the best of Q-10 reports with record high profits, can lead to a stock price drop.

¯\\\_(ツ)\_/¯
