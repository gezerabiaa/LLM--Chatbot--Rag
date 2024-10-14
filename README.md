# Chatbot Project

This project is a chatbot application that can answer users' questions. The application uses a knowledge base to find the most appropriate answers to users' queries using the fuzzy matching method.

## Features

- **Knowledge Base Loading**: It can load data from a knowledge base file in JSON format.

- **Text Normalization**: It processes texts to better understand user queries by normalizing Turkish characters.

- **Fuzzy Matching**: It finds the closest match by comparing user queries with keywords in the knowledge base.

- **RAG Integration**: When an answer is not found in the knowledge base, it generates knowledge with a language model API.
