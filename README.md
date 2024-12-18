# Generative AI Chatbot

This repository contains the code to build a Generative AI-powered chatbot using Python. The project includes a Flask backend to interact with the OpenAI API and a Streamlit frontend to provide a user-friendly interface for users to communicate with the chatbot.

---

## Features
- **AI-Powered Chatbot**: Uses OpenAI's GPT model to generate intelligent and contextual responses.
- **Flask Backend**: Handles API requests and integrates with OpenAI.
- **Streamlit Frontend**: Provides a clean and interactive web interface for users.
- **Easy Setup**: Minimal dependencies, with clear instructions to get started quickly.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Workflow](#workflow)
5. [Troubleshooting](#troubleshooting)
6. [Future Improvements](#future-improvements)

---

## Installation

### Prerequisites
- Python 3.8 or later
- OpenAI API Key ([Get one here](https://platform.openai.com/signup/))

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/assadchaudhry/generative-ai-chatbot.git
   cd generative-ai-chatbot
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv chatbot_env
   source chatbot_env/bin/activate  # On Windows: chatbot_env\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API Key:
   - Open `chatbot_backend.py` and replace `"your-openai-api-key"` with your actual API key.

---

## Usage

### Running the Backend
1. Start the Flask backend:
   ```bash
   python chatbot_backend.py
   ```
2. The backend API will run at `http://localhost:5000/chat`.

### Running the Frontend
1. Launch the Streamlit frontend:
   ```bash
   streamlit run chatbot_frontend.py
   ```
2. Access the app in your browser at `http://localhost:8501`.

---

## Project Structure

```
|-- chatbot_backend.py    # Backend API with Flask
|-- chatbot_frontend.py   # Frontend interface with Streamlit
|-- requirements.txt       # List of dependencies
```

---

## Workflow
1. **User Input**: The user enters a message in the Streamlit frontend.
2. **Backend Processing**: The frontend sends the message to the Flask API, which forwards it to the OpenAI API.
3. **AI Response**: OpenAI generates a response, which is sent back to the frontend.
4. **Display**: The frontend displays the AI's response to the user.

---

## Troubleshooting

### Common Issues
- **Invalid API Key**: Ensure your OpenAI API key is set correctly in `chatbot_backend2.py`.
- **Connection Errors**: Verify that the backend is running at `http://localhost:5000`.
- **Streamlit Errors**: Ensure Streamlit is installed and updated.

### Debugging Tips
- Use logs to trace issues in both the backend and frontend.
- Test API endpoints using tools like Postman or curl.

---

## Future Improvements
- Add user authentication for secured access.
- Enhance the chatbot with memory to handle longer conversations.
- Deploy the app to a cloud platform for public use.
- Improve the UI/UX of the frontend with additional features.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments
- [OpenAI](https://openai.com/) for their amazing GPT model.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.
- [Streamlit](https://streamlit.io/) for making frontend development simple and intuitive.

---

## Author
**Assad Chaudhry**  
[assad.ca](https://assad.ca)
