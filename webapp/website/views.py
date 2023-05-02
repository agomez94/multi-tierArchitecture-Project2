from flask import Blueprint, redirect, render_template, url_for, request, jsonify
import requests, random, ast



views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/tests')
def tests():
    response = requests.get('https://l0wvrec6z1.execute-api.us-east-1.amazonaws.com/ST-API/question')
    # response = requests.get('https://5csqob5f5a.execute-api.us-east-1.amazonaws.com/ap-test/question')
    # response = requests.get('https://5csqob5f5a.execute-api.us-east-1.amazonaws.com/ap-test/questionid')
    question_bank = response.json()
    print(question_bank)
    results = []
    return render_template("tests.html", question_bank=question_bank, results=results)



@views.route('/tests/answer_check', methods=['POST'])
def answer_check():
    correct_answers = []
    chosen_answers = []
    #This gives me the question bank as a literal string list, need to jank it into a actual list
    question_bank = ast.literal_eval((request.form.get('question_bank')))
    
    #Loops through grabbing correct answer from list
    for questions in question_bank:
        correct_answers.append(questions[6])


    total_questions = len(correct_answers)
    for questions in question_bank:
        choice_string = (request.form.get(str(questions[1])))
        chosen_answers.append(choice_string[0])
    
    results = []
    for x in range(total_questions):
        if correct_answers[x] == chosen_answers[x]:
            results.append(correct_answers[x] + " is Correct!")

        else:
            results.append(chosen_answers[x] + " is incorrect. The correct answer is "+ correct_answers[x])

    return render_template("tests.html", question_bank=question_bank, results=results)


@views.route('/tests/new_questions', methods=['GET','POST'])
def new_questions():
    if request.form.get('new_questions') == 'new_questions':
        return redirect(url_for("views.tests"))

    # return redirect(url_for('views.tests'))
