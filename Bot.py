import tkinter as tk
# from tkinter import messagebox
import openai

openai.api_key = "asst_dRLDUr8p25YyZOBladEBFTcR"

class Chatbot:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot")
        
        self.chat_log = tk.Text(self.window, bd=1, bg="white", width=50, height=8, font=("Arial", 12))
        self.chat_log.config(state=tk.DISABLED)
        
        self.scrollbar = tk.Scrollbar(self.window, command=self.chat_log.yview, cursor="heart")
        self.chat_log['yscrollcommand'] = self.scrollbar.set
        
        self.message = tk.Entry(self.window, bd=0, bg="white", width=29, font=("Arial", 12))
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        
        self.scrollbar.place(x=376, y=6, height=386)
        self.chat_log.place(x=6, y=6, height=386, width=370)
        self.message.place(x=128, y=401, height=90, width=265)
        self.send_button.place(x=6, y=401, height=90)

    def send_message(self):
        user_message = self.message.get()
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "You: " + user_message + "\n")
        self.chat_log.config(state=tk.DISABLED)

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=1024,
            temperature=0.5,
        )
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, "Bot: " + response.choices[0].text + "\n")
        self.chat_log.config(state=tk.DISABLED)

        self.chat_log.insert(tk.END, "Bot: " + response.choices[0].text + "\n")
        self.message.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
