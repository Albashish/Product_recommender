#import public libraries
import tensorflow as tf
import tensorflow_hub as hub
import json
import numpy as np

'''
dataset():
Arguments: None
Function: Create embeddings for all the products in the dataset using Universal Sentence Encoder and product descriptions of the product.
Output: Returns embeddings and the corresponding product urls.
'''
def dataset():
    embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
    #read from the product dataset
    with open('sample.json','r') as f:
        clothing_data = json.load(f)
    urls = []
    description = []
    for k,v in clothing_data.items():
        urls.append(k)
        description.append(v.get('Product Details ','None'))
    embeddings = []
    #Iterate through all descriptions and calculate embeddings for every product
    for i in range(len(description)):
        embeddings.append(embed([description[i]]))
    return embeddings,urls