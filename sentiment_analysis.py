import spacy
import pandas as pd
from textblob import TextBlob


def analyze_sentiment(text):
    # Analyze sentiment of the given text using TextBlob.
    # Returns a tuple of polarity and subjectivity.

    blob = TextBlob(text) 
    sentiment = blob.sentiment
    return sentiment


def sentimental_and_similarity(dataframe):
  # Analyze sentiment and compute similarity of sentences in the given DataFrame.

    try:
        nlp = spacy.load("en_core_web_sm")
        nlp_medium = spacy.load('en_core_web_md')
    except OSError as e:
        print("Error loading spaCy models:", e)

    list_sentences = []
    for review in dataframe:
        doc = nlp(review)
        tokens = []
         
        for token in doc: 
            if not token.is_stop:
                cleaned_token = token.text.lower().strip()
                tokens.append(cleaned_token)
        
        cleaned_sentences = " ".join(tokens)
        list_sentences.append(cleaned_sentences)
    count = 0
    # Analyze sentiment
    for sentence in list_sentences:
        sentiment = analyze_sentiment(sentence)
        print(f"Sentence: {sentence}, Sentiment: {sentiment}\n")       
        compared = []
        
        # Compute similarity
        sum_of_similarity = 0
        # Looping through sentences for similarity
        for sentence_ in list_sentences:
            compared.append(sentence)
            
            try:
                similarity = nlp_medium(sentence).similarity(nlp_medium(sentence_))
            except Exception as e:
                print("Error computing similarity:", e)
            # Compare sentences for similarity
            if sentence_ not in compared:
                sum_of_similarity +=  similarity
                count += 1                            
                print(f"Similarity of '{sentence}' with: '{sentence_}' is: {similarity}.\n")
        if count > 0:
            print(f"Average similarity: {sum_of_similarity/(count-1)} \n\n") 
    
    
try:
    amazon_dataframe = pd.read_csv("amazon_product_reviews.csv").dropna(subset=["reviews.text"])
except FileNotFoundError:
    print("Error: File not found.")
except pd.errors.ParserError:
    print("Error: Invalid file format.")

sentimental_and_similarity(amazon_dataframe["reviews.text"].sample(n=5))

print(f"Data frame Columns: {amazon_dataframe.shape[1]} Rows: {amazon_dataframe.shape[0]}") 
