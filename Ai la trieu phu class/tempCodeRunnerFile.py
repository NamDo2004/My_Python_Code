print(f"Câu hỏi: {question.content}")
        shuffled_options = self.shuffle_options(question.options)
        for i, option in enumerate(shuffled_options, 1):
            print(f"{i}. {option}")

        user_input = input("Nhập đáp án (1, 2, 3, 4): ")
        chosen_option = int