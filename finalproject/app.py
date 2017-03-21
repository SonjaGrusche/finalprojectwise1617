from flask import Flask, session, request
from flask import url_for, redirect, render_template
from random import randint
import resources

app = Flask(__name__)

@app.route('/', methods=['GET'])
def start_get():
    return render_template('start.html')

@app.route('/questionnaire', methods=['GET'])
def questionnaire_get():
    return render_template('questionnaire.html', questions=resources.questions)

@app.route('/questionnaire', methods=['POST'])
def questionnaire_post():
    totals = 0
    for i in range(1, 11):
        try:
            totals += int(request.form.get('question' + str(i)))
        except TypeError:
            return render_template('questionnaire.html', questions=resources.questions, error=1)
    return redirect(url_for('result', total=totals+20))

@app.route('/result/<int:total>')
def result(total):
    if total in range(0, 10):
        type = 0
    elif total in range(10, 20):
        type = 1
    elif total in range(20, 26):
        type = 2
    elif total in range(26, 30):
        type = 3
    elif total in range(30, 33):
        type = 4
    website = resources.links[type][randint(0, len(resources.links[type])-1)]
    return render_template('results.html', site=website)

app.secret_key = '1234supersecret'

if __name__ == "__main__":
    app.run()
