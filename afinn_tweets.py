import sys
import csv

#twitterData = sys.argv[1] #csv file

def tweet_dict(twitterData):  
    ''' (file) -> list of dictionaries
    This method should take your .csv
    file and create a list of dictionaries.
    '''
    twitter_list_dict = []
    twitterfile = open(twitterData)
    twitterreader = csv.reader(twitterfile)
    for line in twitterreader:
        twitter_list_dict.append(line[0])
    return twitter_list_dict


def sentiment_dict(sentimentData):
    ''' (file) -> dictionary
    This method should take your sentiment file
    and create a dictionary in the form {word: value}
    '''
    afinnfile = open(sentimentData) 
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = float(score)  # Convert the score to an integer.
       
    return scores # Print every (term, score) pair in the dictionary

def main():
    tweets = tweet_dict("C:/Users/saurabh/Desktop/ankita/onlytweets.csv")
    sentiment = sentiment_dict("C:/Users/saurabh/Desktop/ankita/AFINN-111.txt")
    
  
    for index in range(len(tweets)):
        
        tweet_word = tweets[index].split()
        sent_score = 0 # sentiment score della frase

        
        for word in tweet_word:
            word = word.rstrip('?:!.,;"!@')
            word = word.replace("\n", "")
          
            if not (word.encode('utf-8', 'ignore') == ""):
                if word.encode('utf-8') in sentiment.keys():
                    sent_score = sent_score + float(sentiment[word])
                    


        print tweets[index] + " --- "+ str(sent_score)

if __name__ == '__main__':
    main()