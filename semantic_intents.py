# This file conatins embedding logic for semantic intents in a virtual office AI application.

import openai
import numpy as np
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# Load intent descriptions
with open('intents.json') as f:
    intents = json.load(f)



# Function to get embeddings for a given text
# Uses OpenAI's text-embedding-3-small model
def get_embedding(text):
    response = openai.Embedding.create(
        input=[text],
        model="text-embedding-3-small"
    )
    return np.array(response['data'][0]['embedding'])

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Generate and store intent embeddings once
intent_vectors = []
for intent in intents:
    desc = intent["description"]
    vec = get_embedding(desc)
    intent_vectors.append((intent["tag"], vec))

# Function to classify intent based on semantic similarity
# Uses cosine similarity to find the closest intent vector
def classify_semantic(message, threshold=0.75):
    user_vec = get_embedding(message)
    best_match = None
    best_score = -1

    for tag, intent_vec in intent_vectors:
        sim = cosine_similarity(user_vec, intent_vec)
        if sim > best_score:
            best_score = sim
            best_match = tag

    if best_score >= threshold:
        return best_match
    return "default"
