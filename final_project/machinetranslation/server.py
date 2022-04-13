import json
import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request


app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated English text to French"
    translated_text = machinetranslation.translator.english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated French text to English"
    translated_text = machinetranslation.translator.french_to_english(text_to_translate)
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
