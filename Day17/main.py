from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for line in question_data:
    question = Question(line["text"], line["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print(f"You've completed the quiz.\nYour final score was {quiz.score}/{quiz.question_number}")