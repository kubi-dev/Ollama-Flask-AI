DeepSeek R1 Chatbot

This is a simple chatbot project that uses the Ollama platform and the DeepSeek-R1:8B model, accessed via a Flask web application.

Prerequisites

To run this project, you need the following:

    Python 3: The core language environment.

    Ollama: A platform for running large language models locally.

    DeepSeek-R1:8B Model: You must have this specific model pulled and running in Ollama.

Ollama Setup

    Install Ollama according to the instructions on the official website.

    Pull the model by running the following command in your terminal:
    Bash

    ollama pull deepseek-coder:6.7b-instruct

    (Note: Based on the requested model name deepseek-r1:8b, the correct Ollama model tag is likely deepseek-coder:6.7b-instruct or similar. Please verify the exact tag if different.)

Installation and Running

Follow these steps to get the project running:

1. Install Python Packages

Install the necessary Python dependencies using pip:
Bash

pip install flask ollama

2. Run the Application

Start the chatbot application by executing the main Python script:
Bash

py main.py

The application will typically start a web server, which you can then access in your browser.