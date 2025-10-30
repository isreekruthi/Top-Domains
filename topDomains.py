#import statement needed for the pandas function using dataframes
import pandas as pd

#this will load the csv file into a pandas dataframe, named here as 'df'
#the first row should be treated as data so we mark header as None
df = pd.read_csv('top-1m.csv', header = None)

#this function, named domainNames, takes 'dataframe' as an input and lists all similar domains in 'urlList'
def domainNames(dataframe):
    urlList = list(dataframe[1])
#domain_names will store the new list
    domain_names = [] 
    for url in urlList:

        #defines dsplit
        dsplit = url.split('.')
        
        if len(dsplit) >= 2:
            domain_names.append(dsplit[-2])
        else:
            domain_names.append('')
    return domain_names
        
#apply the function to our dataframe
df['domain'] = domainNames(df)

#function to get the frequency of each domain
#value_counts is a pandas function where the domain names are listed as indexes and values are listed as the number of times each unique domain appears
#the result is stored in domainCount
domainCount = df['domain'].value_counts()

#domain count of frequency less than 3.5
#< checks for true or false and then adds each true value to the sum
domainFrequency = (domainCount < 3.5).sum()

print("There are", domainFrequency, "domains with a frequency less than 3.5.")