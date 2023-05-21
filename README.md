# Product_recommender
The main task of the project is to scrape product descriptions from e-commerce websites and based on the input query recommend products.
The input will be a string given by the user and the output will be in a json format containing the links(urls) of the top-n products with similar product descriptions.
The product_data.py and parse.py files are used to scrape the product descriptions for e-commerce website. The website used is www.myntra.com.
The output is stored in sample.json file.
The product descriptions extracted are then used as an input in the dataset.py file to calculate the embeddings(or embedding vectors).
These embeddings are called in the use.py file to calculate the pairwise cosine similarity with the embedding of query.
To calculate the embeddings, Google's universal sentence encoder is used.


