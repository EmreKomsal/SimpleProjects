class Question():
    def __init__(self, q_text, q_type, q_correct, q_incorrect):
        self.text = q_text
        self.type = q_type
        self.correct_answer = q_correct
        self.incorrect_answers = q_incorrect
        
        if self.type == "boolean":
            self.answer = self.correct_answer
            
        elif self.type == "multiple":
            self.answer = self.correct_answer
            self.incorrect_answers.append(self.correct_answer)
            self.answers = self.incorrect_answers
            self.answers.sort()
