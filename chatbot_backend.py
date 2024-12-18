# File: chatbot_backend.py

# Import necessary libraries
from flask import Flask, request, jsonify  # Flask framework for creating the backend API
import openai  # OpenAI library to interact with GPT models
import os  # OS module for environment variable management (optional)

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI API key
# Set the OpenAI API key. Replace with your actual API key or retrieve it from environment variables.
#openai.api_key = "sk-proj-2j0A"  # Ensure the API key is set in your environment variables
openai.api_key = "YOUR_API_KEY"  # Ensure the API key is set in your environment variables

@app.route('/chat', methods=['POST'])  # Define a POST route for the chatbot
def chat():
    """
    Endpoint to interact with the ChatGPT model.
    Expects a JSON payload with the 'message' field.
    """
    try:
        # Retrieve the JSON data sent in the POST request
        data = request.json
        user_message = data.get('message')  # Extract the user message from the JSON payload

        # Check if the 'message' field is provided in the request
        if not user_message:
            return jsonify({"error": "Message field is required"}), 400  # Return error if 'message' is missing

        # Call the OpenAI API to get the chatbot response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Define system prompt
                {"role": "user", "content": user_message}  # Add user's input to the conversation
            ]
        )

        # Extract the AI's response from the API's result
        ai_message = response['choices'][0]['message']['content']
        return jsonify({"response": ai_message})  # Return the AI's response as JSON

    except Exception as e:
        # Handle any exceptions and return an error message
        return jsonify({"error": str(e)}), 500

# Run the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on all available IPs on port 5000
