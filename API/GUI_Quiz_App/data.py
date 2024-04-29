import requests
import json

class QData:
    def __init__(self, amount, cat, diff, type):
        self.amount = amount
        self.cat = cat
        self.diff = diff
        self.type = type
        
    def get_data(self):
        if self.cat == 'any' and self.diff == 'any' and self.type == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}"
        elif self.cat == 'any' and self.diff == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&type={self.type}"
        elif self.cat == 'any' and self.type == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&difficulty={self.diff}"
        elif self.diff == 'any' and self.type == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}"
        elif self.cat == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&difficulty={self.diff}&type={self.type}"
        elif self.diff == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}&type={self.type}"
        elif self.type == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}&difficulty={self.diff}"
        else:
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}&difficulty={self.diff}&type={self.type}"
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    
    def get_questions(self):
        data = self.get_data()
        questions = data['results']
        return questions
    
    def get_answers(self, question):
        answers = question['incorrect_answers']
        answers.append(question['correct_answer'])
        return answers
    
    def get_correct_answer(self, question):
        return question['correct_answer']