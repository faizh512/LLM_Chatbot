# Echo Bot

## Overview:
- The Echo Bot is a simple chatbot built using Streamlit and Google's Generative AI (Gemini 1.5 Flash model). The app takes user input, processes it through the Gemini model, and responds with relevant output in real-time. It's designed to demonstrate interaction with a Generative AI model in a web-based interface.

## Prerequisites:
- **Python 3.x**
- **Streamlit**: Install by running `pip install streamlit`
- **dotenv**: Install by running `pip install python-dotenv`
- **Google Generative AI**: You'll need an API key from Google Generative AI and set it up in your environment variables.

## Environment Setup:
1. Ensure you have Python 3.x installed on your machine.
2. Install the required libraries using pip:
    ```bash
    pip install streamlit python-dotenv google-generativeai
    ```
3. Obtain your Google API key from the [Google Cloud Console](https://console.cloud.google.com/) and add it to an `.env` file in your project directory. The `.env` file should look like this:
    ```bash
    GOOGLE_API_KEY=your-google-api-key-here
    ```

## How to Run the App:
1. Clone the repository or save the script file to your local machine.
2. Navigate to the directory containing the script and install the necessary dependencies by running:
    ```bash
    pip install streamlit python-dotenv google-generativeai
    ```
3. Create a `.env` file in the project root and add your Google API key.
4. Run the Streamlit app by executing:
    ```bash
    streamlit run <script_name>.py
    ```
5. The app will launch in your default web browser, and you can start interacting with the chatbot by entering text in the input field.

## Features:
- **Generative AI Model**: The app uses Google's Gemini 1.5 Flash model to generate human-like responses based on user input.
- **Real-Time Chat**: Users can interact with the chatbot, which processes and responds to messages in real-time.
- **Session State for Chat History**: The chat history is maintained using Streamlit's session state, allowing users to view the entire conversation.
  
  ### Live Preview: 
  - The conversation history is updated live, with both user and AI-generated responses clearly displayed.

  ### File Information:
  - **Script File**: Contains the logic for interacting with the chatbot and rendering the conversation on the web app.
  - **Environment File**: The `.env` file securely stores the API key required for accessing Google's Generative AI.

  ### Example Usage:
  - Type any message into the chat input and hit submit.
  - The AI will generate a response based on the message and display it in the chat window.
  - The entire conversation is shown on the page, including both user and AI messages.

## License:
- This project is licensed under the MIT License.
- Feel free to modify and adapt the Echo Bot for your own use cases!
