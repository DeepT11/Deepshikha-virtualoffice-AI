import json
from semantic_intents import classify_semantic

with open('intents.json') as f:
    intents = json.load(f)

def classify_intent(message):
    message = message.lower()

    for intent in intents:
        # Keyword-based match
        for keyword in intent.get("keywords", []):
            if keyword in message:
                return intent["tag"]
        # Pattern fallback
        for pattern in intent.get("patterns", []):
            if pattern.lower() in message:
                return intent["tag"]
        
        # fall to semantic classification if no keyword or pattern matches
    return classify_semantic(message)
