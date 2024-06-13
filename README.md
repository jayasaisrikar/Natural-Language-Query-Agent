README.md
Project Overview
This project utilizes various tools and libraries to fetch, process, and query information from lectures and model architectures related to Stanford's CS324 course and LLM (Large Language Model) papers.

Prerequisites
Before running the code, ensure you have Python installed. Clone the repository and navigate into it:


git clone <repository_url>
cd <repository_directory>
Installation
Setup Python Environment:

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
Configuration
Environment Variables:
Create a .env file in the root directory of the project.
Add your Google API key:
makefile
Copy code
GOOGLE_API_KEY=your_google_api_key_here
Replace your_google_api_key_here with your actual Google API key.
Usage
To run the script and interact with the query agent:

python script_name.py
Follow the prompts to enter your questions. Type exit to quit.

Details
Fetch Data: Retrieves lecture notes and model architectures from specified URLs.
Vector Embeddings: Utilizes Google Generative AI for generating embeddings and creates a vector store using FAISS.
Query Agent: Uses a ChatGoogleGenerativeAI model to answer questions based on the generated vector embeddings.
References
Sentence Transformers
Google Generative AI
FAISS
LangChain