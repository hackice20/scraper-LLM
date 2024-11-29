import ollama # type: ignore
import time
import os
import json
import numpy as np # type: ignore
from numpy.linalg import norm # type: ignore

# Load the Reddit JSON file
def load_reddit_json(filename="reddit_posts.json"):
    with open(filename, "r") as f:
        return json.load(f)

# Save embeddings to a file
def save_embeddings(filename, embeddings):
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")
    with open(f"embeddings/{filename}.json", "w") as f:
        json.dump(embeddings, f)

# Load embeddings from a file
def load_embeddings(filename):
    if not os.path.exists(f"embeddings/{filename}.json"):
        return None
    with open(f"embeddings/{filename}.json", "r") as f:
        return json.load(f)

# Generate embeddings using Ollama's API
def get_embeddings(posts, filename, modelname="nomic-embed-text"):
    embeddings = load_embeddings(filename)
    if embeddings:
        return embeddings
    
    # Generate embeddings for all posts
    embeddings = []
    for post in posts:
        content = f"{post['title']} {post['selftext']}"
        embedding = ollama.embeddings(model=modelname, prompt=content)["embedding"]
        embeddings.append(embedding)
        time.sleep(0.5)  # Avoid rate-limiting issues
    save_embeddings(filename, embeddings)
    return embeddings

# Find the most similar chunks using cosine similarity
def find_most_similar(needle, haystack):
    needle_norm = norm(needle)
    similarity_scores = [
        np.dot(needle, item) / (needle_norm * norm(item)) for item in haystack
    ]
    return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)

# Main function
def main():
    SYSTEM_PROMPT = """You are a helpful assistant that would think less and genrate quick responses related to the prompts"""
    reddit_json_file = "reddit_posts.json"
    embeddings_file = "reddit_embeddings"

    # Load Reddit posts
    posts = load_reddit_json(reddit_json_file)
    print(f"Loaded {len(posts)} posts from {reddit_json_file}")

    # Generate or load embeddings
    embeddings = get_embeddings(posts, embeddings_file)

    while True:
        # User input
        prompt = input("\nWhat do you want to know? (Type 'exit' to quit) -> ")
        if prompt.lower() == "exit":
            break

        # Generate embedding for the query prompt
        prompt_embedding = ollama.embeddings(
            model="nomic-embed-text", prompt=prompt
        )["embedding"]

        # Find the most similar Reddit posts
        most_similar_chunks = find_most_similar(prompt_embedding, embeddings)[:5]

        # Prepare context from the most similar chunks
        context = "\n".join(
            f"Title: {posts[item[1]]['title']}\n{posts[item[1]]['selftext']}\n"
            for item in most_similar_chunks
        )

        # Query Llama3 with the context
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT + "\n\n" + context},
                {"role": "user", "content": prompt},
            ],
        )

        print("\n--- Llama3 Response ---")
        print(response["message"]["content"])
        print("\n")

if __name__ == "__main__":
    main()
