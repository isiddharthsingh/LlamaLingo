import streamlit as st # type: ignore
from openai import OpenAI

# Set up the Streamlit App
st.title("Llama-3 Chatbot 🦙🤖")  # Display the title of the app
st.caption("Chat with the Llama-3 chatbot! 🦙🤖")  # Display a caption below the title

# Point to the local server setup using LM Studio
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")  # Initialize the OpenAI client with local server setup

# Initialize the chat history
if "messages" not in st.session_state:  # Check if the 'messages' key is not in the session state
    st.session_state.messages = []  # Initialize an empty list for chat history

# Display the chat history
for message in st.session_state.messages:  # Iterate through each message in the chat history
    with st.chat_message(message["role"]):  # Create a chat message container for each message
        st.markdown(message["content"])  # Display the message content

# Accept user input
if prompt := st.chat_input("Hi, Im here to help! What can I assist you with today?"):  # Display an input box and get user input
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})  # Append the user message to chat history
    # Display user message in chat message container
    with st.chat_message("user"):  # Create a chat message container for the user message
        st.markdown(prompt)  # Display the user message content
    # Generate response
    response = client.chat.completions.create(  # Call the OpenAI API to generate a response
        model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",  # Specify the model to use
        messages=st.session_state.messages,  # Pass the chat history to the API
        temperature=0.8  # Set the temperature for response generation
    )
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})  # Append the assistant's response to chat history
    # Display assistant response in chat message container
    with st.chat_message("assistant"):  # Create a chat message container for the assistant's response
        st.markdown(response.choices[0].message.content)  # Display the assistant's response content
