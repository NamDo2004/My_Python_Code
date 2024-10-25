import random
from cauhoi import questions, Question

class AiLaTrieuPhu:
    def __init__(self):
        self.score = 0
        self.questions_taken = set()

    def get_random_question(self):
        remaining_questions = set(range(len(questions))) - self.questions_taken
        if not remaining_questions:
            return None
        question_index = min(remaining_questions)  # Get the smallest remaining question index
        self.questions_taken.add(question_index)
        return questions[question_index]

    def shuffle_options(self, options):
        return options

    def display_question(self, question):
        print(f"Câu hỏi: {question.content}")
        shuffled_options = self.shuffle_options(question.options)
        for i, option in enumerate(shuffled_options, 1):
            print(f"{i}. {option}")

        user_input = input("Nhập đáp án (1, 2, 3, 4): ")
        chosen_option = int(user_input)

        return shuffled_options.index(question.options[chosen_option - 1]) + 1

    def play_game(self):
        with open("game_results.txt", "w", encoding="utf-8") as file:
            for i in range(1, 16):
                question = self.get_random_question()
                if not question:
                    file.write("Hết câu hỏi.\n")
                    break

                file.write(f"\nCâu số {i}/15 - Tiền: {10**(i-1):,} đồng\n")
                chosen_option = self.display_question(question)

                if chosen_option == question.correct_answer:
                    self.score = 10**(i-1)
                    file.write(f"Trả lời đúng! Bạn có {self.score:,} đồng.\n")
                else:
                    file.write("Sai rồi! Kết thúc trò chơi.\n")
                    break

                user_input = input("Bạn muốn dừng lại không? (Nhập 'y' để dừng): ")
                file.write(f"Bạn muốn dừng lại không? (Nhập 'y' để dừng): {user_input}\n")

                if user_input.lower() == 'y':
                    file.write(f"Chúc mừng! Bạn đã dừng lại với số tiền là: {self.score:,} đồng\n")
                    break

if __name__ == "__main__":
    game = AiLaTrieuPhu()
    game.play_game()
