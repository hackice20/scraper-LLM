import praw # type: ignore
import os
import json
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

# Function to fetch subreddit posts
def fetch_subreddit_posts(subreddit_name, query, limit=30):
    """
    Fetches posts from a subreddit related to a specific query.
    """
    try:
        subreddit = reddit.subreddit(subreddit_name)
        search_results = subreddit.search(query, limit=limit)
        
        results = []
        for post in search_results:
            image_url = post.url if post.url.endswith((".jpg", ".jpeg", ".png", ".gif")) else None
            external_link = post.url if not image_url else None

            results.append({
                "title": post.title,
                "selftext": post.selftext,
                "image_url": image_url,
                "external_link": external_link,
            })
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []

# Save results to a JSON file
def save_to_json(data, filename="reddit_posts.json"):
    """
    Saves the data to a JSON file.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")

# Example usage
if __name__ == "__main__":
    subreddit_name = input("Enter subreddit name (e.g., 'learnpython', 'AskReddit'): ")
    query = input("Enter the search query: ")
    posts = fetch_subreddit_posts(subreddit_name=subreddit_name, query=query, limit=10)

    print(f"\nFetched {len(posts)} posts related to '{query}' from r/{subreddit_name}:\n")

    # Save posts to a JSON file without Llama3 analysis
    save_to_json(posts)
