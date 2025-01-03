from flask import Flask, request, jsonify, render_template_string
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = "your_openai_api_key"

# Inline HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT Flask App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f9;
        }
        .chat-container {
            width: 400px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        #chat-box {
            height: 300px;
            overflow-y: scroll;
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
        }
        #user-input {
            width: calc(100% - 22px);
            height: 50px;
            margin-bottom: 10px;
        }
        #send-button {
            width: 100%;
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div id="chat-box"></div>
        <textarea id="user-input" placeholder="Type your message..."></textarea>
        <button id="send-button">Send</button>
    </div>
    <script>
        document.getElementById("send-button").addEventListener("click", sendMessage);

        function sendMessage() {
            const userInput = document.getElementById("user-input").value;
            if (!userInput.trim()) return;

            const chatBox = document.getElementById("chat-box");
            chatBox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;
            document.getElementById("user-input").value = "";

            fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userInput }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.reply) {
                        chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
                    } else {
                        chatBox.innerHTML += `<div><strong>Error:</strong> ${data.error}</div>`;
                    }
                    chatBox.scrollTop = chatBox.scrollHeight;
                })
                .catch((error) => {
                    chatBox.innerHTML += `<div><strong>Error:</strong> ${error.message}</div>`;
                });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
