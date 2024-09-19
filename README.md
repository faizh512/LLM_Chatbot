# Simple LLM By Using Ollama

- ## Overview:
  - This is a simple application built using Streamlit that allows users to input an English sentence and receive its translation into French. The translation is powered by the `llama3` model, integrated via LangChain's Ollama. The app provides a user-friendly interface for real-time translations.

- ## Prerequisites:
  - Python 3.x
  - **Streamlit**: Install by running `pip install streamlit`
  - **Langchain-Ollama**: Install by running `pip install langchain-ollama`

- ## How to Run the App:
  - Clone the repository or save the script file to your local machine.
  - Navigate to the directory containing the script and install the necessary dependencies:

    ```bash
    pip install streamlit langchain-ollama
    ```

  - Run the Streamlit app by executing:

    ```bash
    streamlit run <script_name>.py
    ```

  - The app will launch in your default web browser. You can start entering English sentences for translation into French.

- ## Features:
  - **Translation**: Input an English sentence, and the app will translate it to French using the `llama3` model.
  - **User-friendly Interface**: Simple and clean interface using Streamlit.
  - **Locally Hosted Model**: The `llama3` model is hosted locally and accessed via `http://localhost:8000`.

  - ### Live Preview: 
    - The translated text is displayed in real-time after entering the input and clicking the submit button.

  - ### File Information:
    - **Script File**: Contains the logic for input, translation, and displaying the output.
    - **LangChain and Ollama**: LangChain is used for interacting with the `llama3` model, and the model is hosted locally.

  - ### Example Usage:
    - Enter an English sentence into the input field.
    - Click "Submit."
    - The French translation will be displayed on the page.

- ## License:
  - This project is under the MIT License.
  - Feel free to modify the app and adapt it for your specific needs!
