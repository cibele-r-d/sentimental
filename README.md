# Report: Sentimental analysis of text reviews in Consumer Reviews of Amazon Products

## 1.Dataset description:

The dataset comprises Amazon product reviews stored in a CSV file named "amazon_product_reviews.csv". It consists of a DataFrame with 24 columns and 5000 rows. The data spans from December 2015 to May 2018. For sentiment analysis, only the **"reviews.text"** column is utilised.



## 2. Preprocessing steps:

- Loading spaCy models for natural language processing.
- Iterating through rows to access reviews separately.
- Tokenization of the Data.
- Removal of blank rows using **‘.dropna’**
- Cleaning the data by excluding stopwords, extra spaces, and capital letters from the final data.

The sentiment of each review is analysed using TextBlob's sentiment analysis feature. Additionally, the similarity between reviews is computed using spaCy's medium English language model and ‘.similarity’. The evaluation includes printing the sentiment of each review and computing the similarity between reviews and the average similarity of each review with the others.

## 3. Evaluation of Results:

### Sample of results:
#### Review 1:


- **Sentence:** "Excellent. Good iPad fraction price."
- **Sentiment:** The sentiment polarity is positive with a score of 0.85, indicating a highly positive sentiment. The subjectivity score is 0.8, suggesting a subjective expression.
Similarity with other sentences: The sentence exhibits high similarity (0.826) with "Recommend product. Works great very compact." This indicates a similar sentiment and possibly related content. Additionally, it shows moderate to high similarity with other sentences, indicating coherence within the reviews.

#### Review 2:


- **Sentence:** "Recommend product. Works great very compact."
- **Sentiment:** The sentiment polarity is positive with a score of 0.8, indicating a positive sentiment. The subjectivity score is 0.75, suggesting a moderately subjective expression.
Similarity with other sentences: This sentence displays high similarity (0.826) with "Excellent. Good iPad fraction price." Additionally, it exhibits moderate similarity with other sentences, indicating consistency in sentiment and possibly related content.


### Overall Analysis:
#### Sentiment Analysis:


- The sentiment analysis reveals predominantly positive sentiments in the consumer reviews, with both examples displaying positive sentiment polarities.
- The subjectivity scores suggest that the expressions in the reviews are subjective, reflecting personal opinions and experiences of the users.


#### Semantic Similarity:


- The computed similarity scores indicate the semantic coherence and relatedness between sentences within the reviews.
- High similarity scores between certain sentences suggest shared content or sentiment, enhancing the understanding of the overall sentiment and themes present in the reviews.


#### Strengths:
- The sentiment analysis accurately captures the overall sentiment expressed in the reviews, providing insights into consumer opinions.
- Semantic similarity computation helps identify related content, contributing to a deeper understanding of review themes and sentiments.


#### Limitations:
- The evaluation relies on similarity scores, which may not fully capture the semantic nuances and context of the reviews.
- The sentiment analysis may oversimplify complex sentiments, potentially missing subtle variations in opinion.


#### Conclusion:
Overall, the sentiment analysis and similarity computation offer valuable insights into the consumer reviews of Amazon products, providing a basis for understanding customer satisfaction and product perceptions. However, further analysis and context may be necessary to fully interpret the sentiments expressed in the reviews.




***Project for HyperionDev Data Science course on sentiment analysis.***
