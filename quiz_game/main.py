from question_model import Question
from quiz_brain import QuizBrain
from data import Data

def main():
    question_bank = []
    question_data = Data().get_data()
    
    for question in question_data:
        question_bank.append(Question(question["question"], question["type"], question["correct_answer"], question["incorrect_answers"]))
    
    quiz = QuizBrain(question_bank)
    
    while quiz.still_has_questions():
        quiz.next_question()
        
    print("You've completed the quiz!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
if __name__ == "__main__":
    main()