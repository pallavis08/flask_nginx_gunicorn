from flask import Flask, jsonify, render_template, request, make_response
import transformers

app = Flask(__name__)

hfmodel = transformers.pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")

# hfmodel = transformers.pipeline('sentiment-analysis', model="siebert/sentiment-roberta-large-english")

# inference
def get_prediction(message,model):
    results = model(message)
    return results

@app.route('/', methods=['GET'])
def get():
    """
    Demo test
    :return: some text
    """
    return jsonify({"Working": "Good!"})

@app.route('/', methods=['POST'])
def predict():
    message = request.json['text']
    results = get_prediction(message, hfmodel)
    my_prediction = f'The rating of this text is {results[0]["label"]} with probability of {results[0]["score"]*100}%.'
    return  my_prediction

if __name__ == '__main__':
    # starting app
    app.run(debug=True,host='0.0.0.0')