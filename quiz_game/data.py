import requests
import html

class Data:
    def __init__(self, url = None, q_count = 10):
        if url is None:
            print("Welcome to the Trivia Game!")
            print("Would you like to customize your game?")
            choice = input("Enter yes or no: ")
            choice = choice.lower()
            if choice == "yes":
                print("You can customize the number of questions, category, difficulty, and type of questions.")
                q_count = int(input("Enter the number of questions you would like: "))
                while q_count < 1 or q_count > 50:
                    print("Invalid number of questions. Please enter a number between 1 and 50.")
                    q_count = int(input("Enter the number of questions you would like: "))
                cat = self.cat()
                diff = self.diff()
                type = self.type()
                if cat != 0 and type != "random":
                    self.url = f"https://opentdb.com/api.php?amount={q_count}&category={cat}&difficulty={diff}&type={type}"
                elif cat == 0 and type != "random":
                    self.url = f"https://opentdb.com/api.php?amount={q_count}&difficulty={diff}&type={type}"
                elif cat != 0 and type == "random":
                    self.url = f"https://opentdb.com/api.php?amount={q_count}&category={cat}&difficulty={diff}"
                elif cat == 0 and type == "random":
                    self.url = f"https://opentdb.com/api.php?amount={q_count}&difficulty={diff}"
                else: 
                    self.url = f"https://opentdb.com/api.php?amount={q_count}&difficulty={diff}&type={type}"
            else:
                self.url = f"https://opentdb.com/api.php?amount={q_count}"
        else:
            self.url = url
        self.data = requests.get(self.url).json()["results"]
        self.question_data = []
        self.question_text = ""
        self.question_type = ""
        
    def get_data(self):
        for question in self.data:
            self.question_text = html.unescape(question["question"])
            self.question_type = question["type"]
            if self.question_type == "boolean":
                self.question_data.append({"question": self.question_text, "type": self.question_type, "correct_answer": html.unescape(question["correct_answer"]), "incorrect_answers": [html.unescape(answer) for answer in question["incorrect_answers"]]})
            elif self.question_type == "multiple":
                self.question_data.append({"question": self.question_text, "type": self.question_type, "correct_answer": html.unescape(question["correct_answer"]), "incorrect_answers": [html.unescape(answer) for answer in question["incorrect_answers"]]})
        return self.question_data
    
    def type(self):
        print("Welcome to the Trivia Game!")
        print("How would you like to play?")
        print("1. True or False")
        print("2. Multiple Choice")
        print("3. Random")
        choice = input("Enter the number of your choice: ")
        choice = choice.lower()
        ch_lib = {"1": "boolean", "2": "multiple", "3": "random", "true": "boolean", "false": "boolean", "multiple": "multiple", "choice": "multiple", "random": "random"}
        if choice in ch_lib:
            return ch_lib[choice]
        else:
            print("Invalid choice. Please try again.")
            return self.type()
    
    def diff(self):
        print("What difficulty would you like to play?")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = input("Enter the number of your choice: ")
        choice = choice.lower()
        ch_lib = {"1": "easy", "2": "medium", "3": "hard", "easy": "easy", "medium": "medium", "hard": "hard"}
        if choice in ch_lib:
            return ch_lib[choice]
        else:
            print("Invalid choice. Please try again.")
            return self.diff()
        
    def cat(self):
        print("What category would you like to play?")
        print("1. General Knowledge")
        print("2. Books")
        print("3. Film")
        print("4. Music")
        print("5. Musicals & Theatres")
        print("6. Television")
        print("7. Video Games")
        print("8. Board Games")
        print("9. Science & Nature")
        print("10. Computers")
        print("11. Mathematics")
        print("12. Mythology")
        print("13. Sports")
        print("14. Geography")
        print("15. History")
        print("16. Politics")
        print("17. Art")
        print("18. Celebrities")
        print("19. Animals")
        print("20. Vehicles")
        print("21. Comics")
        print("22. Gadgets")
        print("23. Anime & Manga")
        print("24. Cartoons & Animations")
        print("25. Any Category")
        choice = input("Enter the number of your choice: ")
        choice = choice.lower()
        choice_lib = {
            "1": 9, "general knowledge": 9,
            "2": 10, "books": 10,
            "3": 11, "film": 11,
            "4": 12, "music": 12,
            "5": 13, "musicals & theatres": 13,
            "6": 14, "television": 14,
            "7": 15, "video games": 15,
            "8": 16, "board games": 16,
            "9": 17, "science & nature": 17,
            "10": 18, "computers": 18,
            "11": 19, "mathematics": 19,
            "12": 20, "mythology": 20,
            "13": 21, "sports": 21,
            "14": 22, "geography": 22,
            "15": 23, "history": 23,
            "16": 24, "politics": 24,
            "17": 25, "art": 25,
            "18": 26, "celebrities": 26,
            "19": 27, "animals": 27,
            "20": 28, "vehicles": 28,
            "21": 29, "comics": 29,
            "22": 30, "gadgets": 30,
            "23": 31, "anime & manga": 31,
            "24": 32, "cartoons & animations": 32,
            "25": 0, "any category": 0
        }
        choice_key = choice_lib.get(choice)
        if choice_key is not None:
            return choice_key
        else:
            print("Invalid choice. Please try again.")
            return self.cat()