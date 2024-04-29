import requests
import json

class QData:
    def __init__(self, amount, cat, diff):
        self.amount = amount
        self.cat = cat
        self.diff = diff
        self.type = "boolean" # "multiple" or "boolean
        
    def get_data(self):
        if self.cat == 'any' and self.diff == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&type={self.type}"
        elif self.cat == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&difficulty={self.diff}&type={self.type}"
        elif self.diff == 'any':
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}&type={self.type}"
        else:
            url = f"https://opentdb.com/api.php?amount={self.amount}&category={self.cat}&difficulty={self.diff}&type={self.type}"
        
        response = requests.get(url)
        data = json.loads(response.text)
        return data
    
    def get_questions(self):
        data = self.get_data()
        questions = data['results']
        return questions
    
    def get_true_answer(self, question):
        return question['correct_answer']