class Quiz:
  def __init__(self):
    self.questions = {
      "What is the capital of France?": "Paris",
      "Which planet is known as the Red Planet?": "Mars",
      "Who painted the famous painting Starry Night?": "Vincent van Gogh",
      "What is the largest mammal on Earth?": "Blue whale",
      "Which language is spoken by most people in China?": "Mandarin"
    }
    self.score = 0

  def display_questions(self):
    for question, answer in self.questions.items():
      user_answer = input(question + " ")
      if user_answer.lower() == answer.lower():
        print("Correct answer!")
        self.score += 1
      else:
        print(f"Incorrect answer. Correct answer is {answer}.")

  def display_result(self):
    print(f"\nYour final score is {self.score} out of {len(self.questions)}.")

def main():
  quiz = Quiz()
  print("Welcome to the quiz program!")
  quiz.display_questions()
  quiz.display_result()

if __name__ == "__main__":
  main()

def store_result(self):
  user_name = input("Enter your name: ")
  with open("scores.txt", "a") as file:
    file.write(f"{user_name}: {self.score}\n")