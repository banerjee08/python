from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    ques = Question(question_text, question_answer)
    question_bank.append(ques)



quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


if not quiz.still_has_questions():
    print("You've completed the quiz!!!")
    print(f"Your final score was: {quiz.score} / {len(quiz.question_list)}")

