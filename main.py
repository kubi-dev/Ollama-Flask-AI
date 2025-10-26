from ollama import chat
from ollama import ChatResponse
from flask import Flask, render_template,request, redirect

app = Flask(__name__)
# You need ollama running for this function
def chatbot_ollama(pytanie):
    response: ChatResponse = chat(model='deepseek-r1:8b', messages=[
      {
        'role': 'user',
        'content': pytanie,
      },
    ])
    print("[DEBUG] Wysłano zapytanie")
    return response.message.content

@app.route('/')
def index():
    return render_template('main.html')
    
@app.route('/anwser', methods=['POST','GET'])
def anwser():
    if request.method == 'POST':
        text = request.form['text']
        anwser = chatbot_ollama(text)
        return render_template('anwser.html', anwser=anwser)
    return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)

    