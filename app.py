from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล SQLite
conn = sqlite3.connect('questions.db')
c = conn.cursor()

# สร้างตาราง questions ในฐานข้อมูล
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, answer TEXT, choice1 TEXT, choice2 TEXT, choice3 TEXT, choice4 TEXT)''')
conn.commit()


@app.route('/')
def admin():
    # เรียกดูโจทย์ทั้งหมดจากฐานข้อมูล
    c.execute("SELECT * FROM questions")
    questions = c.fetchall()
    return render_template('admin.html', questions=questions)


@app.route('/add_question', methods=['POST'])
def add_question():
    # รับข้อมูลจากฟอร์มและบันทึกลงในฐานข้อมูล
    question = request.form['question']
    answer = request.form['answer']
    choice1 = request.form['choice1']
    choice2 = request.form['choice2']
    choice3 = request.form['choice3']
    choice4 = request.form['choice4']
    c.execute("INSERT INTO questions (question, answer, choice1, choice2, choice3, choice4) VALUES (?, ?, ?, ?, ?, ?)",
              (question, answer, choice1, choice2, choice3, choice4))
    conn.commit()
    return redirect(url_for('admin'))


@app.route('/delete_question/<int:id>', methods=['POST'])
def delete_question(id):
    # ลบโจทย์จากฐานข้อมูล
    c.execute("DELETE FROM questions WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)
