from flask import Flask, render_template, request

app = Flask(__name__)

# ข้อมูลคำถามและคำตอบ
questions = {
    1: {
        'question': 'What is the capital of France?',
        'options': ['London', 'Paris', 'Berlin', 'Rome', 'Madrid', 'Tokyo'],
        'answer': 'Paris'
    }
}

@app.route('/')
def index():
    # ส่งข้อมูลคำถามไปยังเทมเพลต
    return render_template('index.html', question=questions[1]['question'], options=questions[1]['options'])

@app.route('/answer', methods=['POST'])
def answer():
    # รับคำตอบจากผู้ใช้
    user_answer = request.form['answer']

    # เช็คคำตอบ
    correct_answer = questions[1]['answer']
    if user_answer == correct_answer:
        result = 'Correct!'
    else:
        result = f'Incorrect! The correct answer is {correct_answer}'

    return render_template('answer.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)