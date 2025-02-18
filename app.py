from flask import Flask, render_template, request, jsonify
import requests
import uuid
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient
app = Flask(name)


key = "BF8WQCfzUar73JNOqUj5y0dcHU5lW1RGFycJtSeMgPYb366Tf69gJQQJ99BBAC1i4TkXJ3w3AAAbACOGgMDQ"
endpoint = "https://api.cognitive.microsofttranslator.com"


location = "centralus"
path = '/translate'
constructed_url = endpoint + path
params = {
'api-version': '3.0',
'from': 'en',
'to': ['fr', 'zu', 'ur']
}
headers = {
'Ocp-Apim-Subscription-Key': key,
'Ocp-Apim-Subscription-Region': location,
'Content-type': 'application/json',
'X-ClientTraceId': str(uuid.uuid4()),
}
@app.route("/", methods=["GET", "POST"])
def index():
if request.method == "POST":
# Get user input from the form
user_input = request.form.get("text")
# Use the user input in the body
body = [{
'text': user_input
}]
# Send the request to the API
response = requests.post(constructed_url, params=params, headers=headers, json=body)
translation_response = response.json()
# Extract translations from the response
translations = []
for translation in translation_response[0]['translations']:
translations.append({
'language': translation['to'],
'translated_text': translation['text']
})
# Render the page with the translations
return render_template("index.html", translations=translations, original_text=user_input)
# If it's a GET request, just render the form
return render_template("index.html")

if name == "main ":
app.run(debug=True)
