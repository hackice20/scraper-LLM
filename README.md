### **README: Reddit Scraper + Llama3 Integration**

---

## **Overview**

This project consists of two Python scripts designed to work together to create a pipeline for scraping Reddit posts, saving them as structured JSON data, and leveraging embeddings with a local **Llama3** model to provide intelligent answers based on the data.

The system allows users to query the Llama3 model about the scraped Reddit data. By embedding the posts into vector representations, the project ensures that the model generates contextually relevant responses. This approach is particularly useful for summarizing large datasets or answering questions based on specific data sources.

---

## **Project Structure**

### **1. Reddit Scraper Script (`main.py`)**
This script retrieves posts from Reddit based on a specific search term or subreddit, processes the data, and saves it as a structured JSON file.

- **Key Features**:
  - Scrapes a specified number of Reddit posts related to a search term.
  - Collects post details like title, body, images, and links.
  - Outputs the data in a clean JSON format for further processing.

- **Output**: A JSON file containing Reddit post data.

---

### **2. Embeddings + Llama3 Script (`final.py`)**
This script takes the JSON data from the Reddit scraper, converts it into embeddings, and uses a local **Llama3** model to answer user queries based on the data.

- **Key Features**:
  - Parses the JSON file into paragraphs or chunks.
  - Generates vector embeddings for both the data and the user query using a model like `nomic-embed-text`.
  - Matches the user query with the most relevant chunks of Reddit data based on cosine similarity.
  - Provides answers through the Llama3 model using the relevant context.

- **Output**: Context-aware responses to user queries based on the Reddit data.

---

## **Workflow**

### **Step 1: Scrape Reddit Data**
1. Run `main.py` to fetch posts based on a given search term or subreddit.
2. Specify the number of posts to retrieve and the output file name.
3. The script generates a JSON file with the retrieved posts.

### **Step 2: Query Llama3**
1. Run `final.py` to load the generated JSON file.
2. The script embeds the Reddit data and allows the user to input a query.
3. It matches the query with the most relevant chunks from the embeddings and uses Llama3 to generate a response.

---

## **Example Use Case**

1. **Scraping Reddit**:
   - Search for posts about *"latest SaaS tools"* on Reddit.
   - Save the results in `reddit_posts.json`.

2. **Querying Llama3**:
   - Ask the system: *"What are the top tools mentioned in the posts?"*
   - The system provides an intelligent answer derived from the scraped Reddit data.

---

## **Key Dependencies**
1. **For Reddit Scraper**:
   - `praw` for accessing Reddit data.
   - `requests` for downloading images or additional links (if required).

2. **For Embeddings + Llama3**:
   - `ollama` for embedding generation and Llama3 interaction.
   - `numpy` for cosine similarity calculations.
   - `json` for parsing and handling the scraped data.

---

## **Features**

### **1. Reddit Scraper**
- Supports fetching multiple posts from any subreddit or search query.
- Captures the title, body, image links, and external URLs from Reddit posts.

### **2. Llama3 Query System**
- Converts scraped data into high-dimensional vector embeddings for efficient similarity matching.
- Leverages the Llama3 model to generate context-aware answers to user queries.

### **3. Modular and Extensible**
- The embedding and Llama3 system is independent of Reddit data, allowing other sources to be added seamlessly.
- API keys and configurations are managed securely using environment variables.

---

## **Future Improvements**
1. **Expand Data Sources**:
   - Extend the scraper to include other platforms like Twitter, YouTube, or news APIs.
2. **Enhanced Query Handling**:
   - Add multi-turn conversations and follow-up question support for Llama3.
3. **Improved Embeddings**:
   - Experiment with more advanced embedding models for better similarity matching.

---

## **Credits**
- **PRAW**: For simplifying Reddit data retrieval.
- **Ollama**: For enabling local Llama3 model interaction.
- **Numpy**: For vector math and similarity computations.

---  
## **Output**
<p align="center">
  <img src="scraped data.png" alt="Reddit Scraper Output" width="600"/>
  <br/>
  <i>Example of data scraped from Reddit posts.</i>
</p>

<p align="center">
  <img src="bad generation.png" alt="Reddit Scraper Output" width="600"/>
  <br/>
  <i>Bad output generated from context.</i>
</p>

<p align="center">
  <img src="good generation.png" alt="Reddit Scraper Output" width="600"/>
  <br/>
  <i>Good output generated from context + better prompt.</i>
</p>

Feel free to customize this pipeline for your specific use case or extend it to include more advanced features!
