from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

# Add questions to question bank
question_bank = []
num_of_questions = 10
for _ in range(num_of_questions):
    question = random.choice(question_data)
    question_data.remove(question)
    question_bank.append(Question(question.get("question"), question.get("correct_answer")))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
