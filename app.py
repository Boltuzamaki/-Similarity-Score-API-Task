from flask import Flask, jsonify, render_template, request
import random 
import numpy as np 
from utils import *
app = Flask(__name__)


# Loading embedding in memory when server started 
embeddings_index = dict()
with open('./embedding/glove.6B.50d.txt',  encoding="utf8") as file:
    for line in file:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs


## POST request 
@app.route("/similarity", methods=["POST"])
def similarity_calculate():
    if request.method=="POST":
        try:
            # Extracting value of params 
            sen1 = request.args.get("sen1")
            sen2 = request.args.get("sen2")
            # Calculating sentence vector of both sentences 
            vec1 = avg_feature_vector(sen1, embeddings_index, 50)
            vec2 = avg_feature_vector(sen2, embeddings_index, 50)
            # Calculating similarity matrix from sentence vector 
            cos_similarity = cosine_similarity_calc(vec1, vec2)
            return jsonify(response = {"Cosine similarity": f'{cos_similarity}'}), 200
        except Exception as e:
            print(e)
            return jsonify(resonse = { "error": "Please provide both Params,sen1 and sen2"}), 404
        



if __name__ == '__main__':
    app.run(debug=False)