class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        if current_question.type == "boolean":
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            self.check_answer(user_answer, current_question.answer)
        elif current_question.type == "multiple":
            print(f"Q.{self.question_number}: {current_question.text}")
            answers = current_question.answers
            for i in range(len(answers)):
                print(f"{i + 1}. {answers[i]}")
            user_answer = input("Enter the number of your choice: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
                self.check_answer(answers[int(user_answer) - 1], current_question.answer)
            else:
                print("Invalid choice. Please try again.")
                self.next_question()
        else:
            print("Invalid question type.")
            self.next_question()
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)