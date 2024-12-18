import streamlit as st
import requests

# Configure the page title and icon for the Streamlit app
st.set_page_config(page_title="Generative AI Chatbot", page_icon="🤖")

# Set the main title and description for the chatbot app
st.title("🤖 Generative AI Chatbot")
st.write("Chat with a generative AI model powered by OpenAI!")

# Initialize the session state to store chat messages if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []  # Stores a list of messages exchanged between user and AI

# Function to send user input to the backend API and retrieve the AI's response
def generate_response(user_input):
    try:
        # URL of the backend API endpoint for processing user input
        url = "http://localhost:5000/chat"
        # Payload to send user input to the API
        payload = {"message": user_input}
        # Headers specifying the content type for the API request
        headers = {"Content-Type": "application/json"}
        # Send a POST request to the API
        response = requests.post(url, json=payload, headers=headers)

        # Check if the API response was successful
        if response.status_code == 200:
            # Return the AI's response from the API's JSON output
            return response.json().get("response", "No response received.")
        else:
            # Handle non-200 status codes by returning an error message
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        # Handle exceptions, such as network errors, and return an error message
        return f"Error: {str(e)}"

# Create a form for user input, clearing the input field after submission
with st.form("chat_form", clear_on_submit=True):
    # Input field for the user to type their message
    user_input = st.text_input("You:", placeholder="Type your message here...")
    # Submit button for sending the message
    submit_button = st.form_submit_button("Send")

# Handle form submission: process user input and generate AI response
if submit_button and user_input:
    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "text": user_input})
    # Get the AI's response using the generate_response function
    ai_response = generate_response(user_input)
    # Add the AI's response to the session state
    st.session_state.messages.append({"role": "ai", "text": ai_response})

# Display the chat history with user and AI messages
for message in st.session_state.messages:
    if message["role"] == "user":
        # Display user messages in bold
        st.markdown(f"**You:** {message['text']}")
    else:
        # Display AI messages in bold
        st.markdown(f"**AI:** {message['text']}")
