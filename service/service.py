import requests


request_result = requests.get('http://172.17.0.1:5000/')
if request_result.status_code == 200:
    text = request_result.json()['text']
    response_text = '. '.join([text, 'Service result.'])
    requests.post('http://172.17.0.1:5000/test', data = {'text':response_text})
