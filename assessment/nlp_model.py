from transformers import pipeline

# Load once
classifier = pipeline("sentiment-analysis")

def get_text_score(text):
    if not text:
        return 0

    result = classifier(text[:512])[0]  # limit length

    if result['label'] == 'NEGATIVE':
        return result['score'] * 1.5   # weight
    return 0