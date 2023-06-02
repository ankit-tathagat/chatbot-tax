# Buidling a chatbot for tax related queries

This repo contains one notebook and two basic Streamlit apps:
- `file_processing.ipynb`: A notebook containing a step by step process of tokenising, chunking and embedding your data in a vector database.
- `search.py`: A Streamlit app providing simple Q&A via a search bar to query your knowledge base. It also provides Upload file capabilities(WIP) to add documents to your knowledge base.
- `chat.py`: A Streamlit app providing a simple Chatbot via a search bar to query your knowledge base.

To run either version of the app, please follow the instructions:

## How it works

- **Steps to run on your local system**
    - Clone the repository from the github
    - Create a openai account and get api-key from [here](https://platform.openai.com/account/api-keys)
    - Download Docker and setup redis
        - To set this up locally, you will need to install Docker first and then run the following command: ```docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest```.
        - More Info: [docs for Redis Stack](https://redis.io/docs/stack/get-started/install/docker/).
    - Create a new virtual environment on your local machine
        - python -m venv /path/to/new/virtual/environment        
    - Activate your new virtual environment
        - venv\Scripts\activate.bat
    - Install all the dependencies 
        - pip install requirements.txt    
    - Open `file_processing.ipynb` and follow the steps inside the notebook.
    - Once your Redis database is completely up and running then come back to your virtual environment terminal
        - Run the following commands: streamlit run Search.py     