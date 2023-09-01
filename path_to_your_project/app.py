from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = 'default'
openai.api_base = 'https://anirudhgpt-api.techwithanirudh.repl.co/v1'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.json['message']
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    return jsonify({'message': response['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)