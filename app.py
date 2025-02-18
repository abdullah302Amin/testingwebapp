from flask import Flask, render_template, request
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient
import requests
import os
import uuid
import json
app = Flask(__name__)

# Add your key and endpoint
key = os.getenv("TRANSLATOR_KEY", "BF8WQCfzUar73JNOqUj5y0dcHU5lW1RGFycJtSeMgPYb366Tf69gJQQJ99BBAC1i4TkXJ3w3AAAbACOGgMDQ")
endpoint = "https://api.cognitive.microsofttranslator.com"

# Location, also known as region.
location = "centralus"

path = '/translate'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4()),
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input and selected language
        user_input = request.form.get("text")
        target_language = request.form.get("language")

        # Use the user input in the body
        body = [{
            'text': user_input
        }]

        # Update the params with the selected language
        params = {
            'api-version': '3.0',
            'from': 'en',
            'to': [target_language]
        }

        # Send the request to the API
        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        translation_response = response.json()

        # Extract the translated text
        translated_text = translation_response[0]['translations'][0]['text']

        # Render the page with the translation
        return render_template(
            "index.html",
            original_text=user_input,
            translated_text=translated_text,
            target_language=target_language
        )

    # If it's a GET request, just render the form
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
