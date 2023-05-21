#import public libraries
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
#import function for embeddings in dataset.py file.
from dataset import dataset

'''
product_recommender():
Argument: query -> str. This query is given by the user.
Function: The function is used to calculate cosine similarity between the embeddings of input query and the embeddings of products in the dataset.
          The top-n similar products are then recommended to the user.
Returns: Urls of the top similar products.
'''
def product_recommender(query):
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
    cos_sim = []
    #calculate embeddings of the input query
    query_embedding = embed([query])
    #load the embeddings of products in the dataset
    embeddings,urls = dataset()
    #iterate through all the products and calculate pairwise cosine similarity.
    for i in range(len(urls)):
        cosine = cosine_similarity(embeddings[i].numpy().reshape(1,-1),query_embedding.numpy().reshape(1,-1))
        cos_sim.append(cosine[0][0])

    n = 4
    #sort the array to get indices of top-n similar products
    top_indices = np.argsort(np.array(cos_sim))[::-1][:n]
    #get the urls of the top-n similar products
    top_urls = [urls[i] for i in top_indices]
    return top_urls
