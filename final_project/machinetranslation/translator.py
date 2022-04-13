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

def english_To_French(englishText):
    translation = language_translator.translate(text=englishText, model_id='en-es').get_result()
    frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    print(frenchText)
    return frenchText

def french_To_English(frenchText):
    translation = language_translator.translate(text=frenchText, model_id='en-es').get_result()
    englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    print(englishText)
    return englishText
