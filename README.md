# Deploying BERT model for Sentiment Analysis.

I have created a web app where you can post user's comment about any product and it will return How many star, that comment should get with confidance.

Model: I have used Bidirectional Encoder Representation for Transformer (BERT) is an NLP model developed by Google Research. It has achieved state-of-the-art accuracy on several NLP tasks. BERT is pre-trained from unlabeled data extracted from the BooksCorpus with 800M words and English Wikipedia with 2,500M words, which gives architecture/model the ability to better understand the language and to learn variability in data patterns and generalizes well on several NLP tasks. As it is bidirectional that means BERT learns information from both the left and the right side of a token’s context during the training phase.

App: This is a very simple app. We can post any text in json format and it output the rating (in number of stars) and confence level (in %) for that text. It can be used to analyze user/customers comments or reviews. App is build using Flask, a light weight python framework for web development.

Nginx and gunicorn: I have used nginx as my web server. I am using gunicorn as wsgi to process multiple requests at the same time. I am using 4 workers. I am running two docker containers, one for nginx and another for Flask app. 

Test file: I have included a test file. this is to test just the model or to test by POST request to the web server.
