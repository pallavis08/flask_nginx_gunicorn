# import transformers

# hfmodel = transformers.pipeline('sentiment-analysis', model="nlptown/bert-base-multilingual-uncased-sentiment")
# # inference
# def get_prediction(message,model):
#     results = model(message)
#     return results

# message = "I am very happy"
# results = get_prediction(message, hfmodel)
# my_prediction = f'The feeling of this text is {results[0]["label"]} with probability of {results[0]["score"]*100}%.'
# print(my_prediction)
# print(results)

#make a POST request locally
# import requests
# text_input = {"text" : "I am happy"}
# res = requests.post('http://127.0.0.1:5000', json=text_input)
# print('response from server:',res.text)

#make a POST request 
import requests
text_input = {"text" : "I bought this product one month ago. I am very happy with its performane. It is giving excellent result so far. 
              It is very fast and efficient and reliable product. I will highly recommend it to others."}
res = requests.post('http://127.0.0.1:8080', json=text_input)
print('response from server:',res.text)
