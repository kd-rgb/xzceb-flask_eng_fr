import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    """Create the English to French translator process"""
    translation = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    frenchtext = json.dumps(translation, indent=2, ensure_ascii=False)
    print(frenchtext)
    return frenchtext

def french_to_english(frenchtext):
    """Create the French to English translator process"""
    translation = language_translator.translate(text=frenchtext, model_id='fr-en').get_result()
    englishtext = json.dumps(translation, indent=2, ensure_ascii=False)
    print(englishtext)
    return englishtext
