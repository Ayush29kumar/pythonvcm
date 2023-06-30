import requests

API_KEY = "AIzaSyDuCGU27tdlo7BL3xtTzRZE_5X54JmmR5U"


query = "speling"

url = f"https://language.googleapis.com/v1/documents:analyzeSyntax?key={API_KEY}"
data = {
    "document": {
        "type": "PLAIN_TEXT",
        "content": query
    },
    "features": {
        "extractSyntax": True
    },
    "encodingType": "UTF8"
}
response = requests.post(url, json=data)

if response.ok:
    results = response.json().get("tokens")
    corrections = []
    for result in results:
        if result.get("partOfSpeech").get("tag") == "VERB" and result.get("suggestionInfo"):
            corrections.extend(result.get("suggestionInfo").get("suggestions"))
    print("Did you mean:")
    for correction in corrections:
        print(correction.get("text"))
else:
    print("Error:", response.status_code, response.text)
