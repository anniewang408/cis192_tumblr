from flask import request, Flask 
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/api/amswers', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    return {"question": question, "answer": 'this is the answer!'}

@app.route('/api/answers', methods=['POST'])
def create_answer():
    body = request.get_json()
    question, answer = body['question'], body['answer']
    return {"question": question, "answer": answer}

if __name__ == '__main__':
    app.run(port= 5000, debug=True)
