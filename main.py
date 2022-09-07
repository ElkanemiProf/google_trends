from pytrends.request import TrendReq
import pandas as pd
import time
# INSTRUCTIONS
# Create a new csv file in the same directory as your project and name is keyword_list
# in the csv file, thA1 cell must be written, Keyword
startTime = time.time()
# This method returns the time as a floating point number expressed in seconds
pytrend = TrendReq(hl='en-GB', tz=360)
#a connection to google trends is initiated and some parameters are also passed

# create a list with one item, "Keywords" and stores it in a variable "colnames"
colnames = ["keywords"]
# create a keyword_list.csv file in the same directory as your project and in the A1 column name it as "Keywords"
# read that csv file and save it as a dataframe denoted by df
keyword_list_data_frame = pd.read_csv("keyword_list.csv", names=colnames)

refined_data_frame = keyword_list_data_frame["keywords"].values.tolist()
# here, we are using pandas to get the content of a specific column, "Keywords" that you earlier created  in order to
# convert the elements of that column into a list
refined_data_frame.remove("Keywords")

dataset = []
# create an empty list, dataset
# loop through the individual items in the dataframe keyword column
# then get the interests over time specified: could be weekly, monthly or daily
# we drop a column "isPartial" from the output we got and finally append it to the dataset list
for item in range(0, len(refined_data_frame)):
    keywords = [refined_data_frame[item]]
    pytrend.build_payload(
        kw_list=keywords,
        cat=0,
        timeframe='today 12-m',
        geo='GB')
    data = pytrend.interest_over_time()
    if not data.empty:
        data = data.drop(labels=['isPartial'], axis='columns')
        dataset.append(data)

result = pd.concat(dataset, axis=1)
# concatenate the dataset output and store in a variable result, then convert it to a csv file
result.to_csv('search3_trends.csv')

# then prints out the time it takes for it to execute this code
executionTime = (time.time() - startTime)
print('Execution time in sec.: ' + str(executionTime))
