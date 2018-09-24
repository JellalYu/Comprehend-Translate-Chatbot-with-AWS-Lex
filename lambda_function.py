import os, boto3

ESCALATION_INTENT_MESSAGE="Seems that you are having troubles with our service. Would you like to be transferred to the associate?"
FULFILMENT_CLOSURE_MESSAGE="Oh I'm sorry to hear about that. How can I help you?"
Skr_MESSAGE="Wow, that's very well. Have a great day"
Three_MESSAGE="Yes I can not agree more!"
What_MESSAGE="What are you talking about?"


escalation_intent_name = os.getenv('ESACALATION_INTENT_NAME', None)

client = boto3.client('comprehend')

translate_client = boto3.client("translate")

#SUPPORTED_LANGUAGES = ['ar', 'zh', 'fr', 'de', 'pt', 'es']


def lambda_handler(event, context):
    response = translate_client.translate_text(Text=event['inputTranscript'],SourceLanguageCode='zh',TargetLanguageCode='en')
    #response2 = print(response['TranslatedText'].encode('utf-8'))
    response3 = response['TranslatedText']
    
    sentiment=client.detect_sentiment(Text=response3,LanguageCode='en')['Sentiment']
    
    if sentiment=='NEGATIVE':
        if escalation_intent_name:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                    },
                    "dialogAction": {
                        "type": "ConfirmIntent", 
                        "message": {
                            "contentType": "PlainText", 
                            "content": ESCALATION_INTENT_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
                    }
            }
        else:
            
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                },
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                    "message": {
                            "contentType": "PlainText",
                            "content": FULFILMENT_CLOSURE_MESSAGE
                    }
                }
            }
    
    elif sentiment=='POSITIVE':
        if escalation_intent_name:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                    },
                    "dialogAction": {
                        "type": "ConfirmIntent", 
                        "message": {
                            "contentType": "PlainText", 
                            "content": ESCALATION_INTENT_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
                    }
            }
        else:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                },
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                    "message": {
                            "contentType": "PlainText",
                            "content": Skr_MESSAGE
                    }
                }
            }
    
    elif sentiment=='NEUTRAL':
        if escalation_intent_name:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                    },
                    "dialogAction": {
                        "type": "ConfirmIntent", 
                        "message": {
                            "contentType": "PlainText", 
                            "content": ESCALATION_INTENT_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
                    }
            }
        else:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                },
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                    "message": {
                            "contentType": "PlainText",
                            "content": Three_MESSAGE
                    }
                }
            }
    
    elif sentiment=='MIXED':
        if escalation_intent_name:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                    },
                    "dialogAction": {
                        "type": "ConfirmIntent", 
                        "message": {
                            "contentType": "PlainText", 
                            "content": ESCALATION_INTENT_MESSAGE
                        }, 
                    "intentName": escalation_intent_name
                    }
            }
        else:
            result = {
                "sessionAttributes": {
                    "sentiment": sentiment
                },
                "dialogAction": {
                    "type": "Close",
                    "fulfillmentState": "Failed",
                    "message": {
                            "contentType": "PlainText",
                            "content": What_MESSAGE
                    }
                }
            }
    
    
    else:
        result ={
            "sessionAttributes": {
                "sentiment": sentiment
            },
            "dialogAction": {
                "type": "Delegate",
                "slots" : event["currentIntent"]["slots"]
            }
        } 
    print(result)    
    return result