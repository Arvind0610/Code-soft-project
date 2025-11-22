import re
import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.user_name = None
        self.responses = {
            r"\bhello\b|\bhi\b|\bhey\b": "Hello! How can I assist you today?",
            r"\bhow are you\b": "I'm functioning great. Thank you for asking!",
            r"\bname\b": "I am CodBot, your virtual assistant created for the CodSoft Internship.",
            r"\btime\b": f"The current time is {datetime.datetime.now().strftime('%I:%M %p')}.",
            r"\bdate\b": f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}.",
            r"\btask\b|\bproject\b": "You need to complete: Rule-based Chatbot, Tic-Tac-Toe AI, Image Captioning.",
            r"\bhelp\b": "Sure, tell me what you need help with.",
            r"\bwho am i\b": "You are an awesome user working on the CodSoft internship!",
            r"\bbye\b|\bexit\b": "Goodbye! Have a productive day."
        }

    def match_response(self, text):
        text = text.lower()
        for pattern, response in self.responses.items():
            if re.search(pattern, text):
                return response
        return "I didn't understand that. Could you please rephrase?"

    def start(self):
        print("CodBot Activated. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            response = self.match_response(user_input)
            print("Bot:", response)
            if user_input.lower() in ["bye", "exit"]:
                break


if __name__ == "__main__":
    bot = RuleBasedChatbot()
    bot.start()
