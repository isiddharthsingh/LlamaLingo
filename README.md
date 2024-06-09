
# LlamaLingo

This project is a chatbot application that uses the Llama-3 model to engage in interactive conversations. It provides a user-friendly interface for chatting with the Llama-3 chatbot, powered by a locally hosted OpenAI-compatible API.

## Features

- Engage in interactive conversations with the Llama-3 chatbot
- User-friendly interface built with Streamlit
- Locally hosted server using LM Studio for model exposure
- Real-time chat history and message display


## Requirements

- Python 3.8+
- Streamlit
- OpenAI API
- LM Studio

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/llamalingo.git
    cd llamalingo
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Install and set up LM Studio. Follow the installation instructions on the [LM Studio website](https://lmstudio.ai/download).

## Usage

### Running LM Studio

1. Start LM Studio and download the Llama-3 instruct model.
2. Expose the Llama-3 model as an OpenAI API by starting the server in LM Studio. Ensure it is running on `http://localhost:1234/v1`.

### Running the Streamlit App

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

### Chatting with LlamaLingo

1. Enter your message in the input box.
2. Click the "Send" button or press Enter.
3. View the chatbot's response in the chat history.

### Sample 
![alt text](<Images/Image.jpg>)

## Contributions

While this is a personal project focused on my own learning and development, any constructive feedback, suggestions, or contributions to the existing solutions are always welcome. If you'd like to contribute, please feel free to submit a pull request.

## Contact

For any inquiries or collaborations, feel free to reach out to me via sms10221@nyu.edu.

## Acknowledgements

- [OpenAI](https://openai.com/) for the Llama-3 model
- [Streamlit](https://streamlit.io/) for the web application framework
- [LM Studio](https://lmstudio.ai/) for providing the local server setup and model exposure

