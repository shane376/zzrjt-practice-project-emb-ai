# Import the requests library to handle HTTP requests, JSON for preprocessing
import json
import requests

# Sentiment Analysis function
def sentiment_analyzer(text_to_analyse: str) -> dict[str]:
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse} }
    header = header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 
    response = requests.post(url, json = myobj, headers = header)
    
    formatted_response = response.json()
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label, score = None, None
    return {"label":label, "score":score}
