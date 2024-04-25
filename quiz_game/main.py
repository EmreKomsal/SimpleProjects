from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


def main():
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(_text = question_text, _answer = question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_list = question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
        
    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.q_number}.")

if __name__ == "__main__":
    main()