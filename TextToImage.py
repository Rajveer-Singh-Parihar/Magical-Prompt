import os
import uuid
import requests
from flask import Flask, request, jsonify, render_template_string, send_from_directory

# Initialize Flask App
app = Flask(__name__)

# OpenAI API Key (replace with your own API key)
OPENAI_API_KEY = "your_openai_api_key"

# Directory to save generated images
OUTPUT_DIR = "generated_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text-to-Image Generator</title>
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
        .container {
            width: 500px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
        }
        textarea {
            width: calc(100% - 20px);
            height: 100px;
            margin-bottom: 10px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #output {
            margin-top: 20px;
        }
        #output img {
            max-width: 100%;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Text-to-Image Generator</h1>
        <textarea id="prompt" placeholder="Enter your prompt here..."></textarea>
        <button id="generate-button">Generate Image</button>
        <div id="output">
            <h2>Generated Image:</h2>
            <img id="generated-image" src="" alt="Generated Image" style="display: none;">
        </div>
    </div>
    <script>
        document.getElementById("generate-button").addEventListener("click", function() {
            const prompt = document.getElementById("prompt").value;
            if (!prompt.trim()) {
                alert("Please enter a prompt.");
                return;
            }

            fetch("/generate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ prompt: prompt })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    const imgElement = document.getElementById("generated-image");
                    imgElement.src = data.image;
                    imgElement.style.display = "block";
                }
            })
            .catch(error => {
                alert("Error generating image: " + error.message);
            });
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        # Call OpenAI's DALL·E or other text-to-image model
        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
            json={"prompt": prompt, "n": 1, "size": "512x512"},
        )
        response.raise_for_status()
        image_url = response.json()['data'][0]['url']

        # Download the image and save locally
        image_name = f"{uuid.uuid4()}.png"
        image_path = os.path.join(OUTPUT_DIR, image_name)
        with open(image_path, "wb") as f:
            f.write(requests.get(image_url).content)

        return jsonify({"image": f"/generated_images/{image_name}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generated_images/<filename>")
def serve_image(filename):
    return send_from_directory(OUTPUT_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
