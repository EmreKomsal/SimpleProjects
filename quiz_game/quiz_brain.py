class QuizBrain:
    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list
        self.score = 0
        
    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    
    def next_question(self):
        current_question = self.q_list[self.q_number]
        if self.q_number == 0:
            print(f"Welcome to the Quiz Game! You will be asked {len(self.q_list)} questions.")
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}.")
        print("\n")