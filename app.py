import os
from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.preview.generative_models import GenerativeModel

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "<paste your path do json with credentials here>"
PROJECT_ID = '<your project id>'
REGION = 'us-central1'

vertexai.init(project=PROJECT_ID, location=REGION)
gemini_pro_model = GenerativeModel("gemini-1.0-pro")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    input_text = request.json.get('text')

    # Use Vertex AI API to summarize the text
    text = f"What illustration should I use for this text (respond with 1-2 words): {input_text}"
    model_response = gemini_pro_model.generate_content(text)
    summarized_text = model_response.candidates[0].content.parts[0].text

    return jsonify({'summarized_text': summarized_text})

if __name__ == '__main__':
    app.run(debug=True)
