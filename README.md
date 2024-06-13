README.md
# Project Overview
This project utilizes various tools and libraries to fetch, process, and query information from lectures and model architectures related to Stanford's CS324 course and LLM (Large Language Model) papers.

# Prerequisites
Before running the code, ensure you have Python installed. Clone the repository and navigate into it:
<br>

`git clone <repository_url>`<br>
`cd <repository_directory>`<br>
# Installation<br>
Setup Python Environment:<br>

# Create and activate virtual environment (optional but recommended)
`python -m venv venv`<br>
`source venv/bin/activate`<br>   # On Windows use `venv\Scripts\activate`<br>
# Install Dependencies:

`pip install -r requirements.txt`<br>
# Configuration
Environment Variables:<br>
Create a .env file in the root directory of the project.<br>
Add your Google API key:<br>
`GOOGLE_API_KEY=your_google_api_key_here`<br>
Replace your_google_api_key_here with your actual Google API key.<br>
# Usage
To run the script and interact with the query agent:<br>

`python script_name.py`
Follow the prompts to enter your questions. Type exit to quit.<br>

# Details
Fetch Data: Retrieves lecture notes and model architectures from specified URLs.<br>
Vector Embeddings: Utilizes Google Generative AI for generating embeddings and creates a vector store using FAISS.<br>
Query Agent: Uses a ChatGoogleGenerativeAI model to answer questions based on the generated vector embeddings.<br>
# References
Sentence Transformers
Google Generative AI
FAISS
LangChain
