import tkinter as tk
import json


class QuizFrame(tk.Frame):
    """
    A class for displaying and managing a quiz.

    Attributes:
        master (tk.Tk): The main tkinter window.
        student_frame: The student dashboard frame to return to.
        user: The current user.
        quiz_data (dict): The quiz questions and answers.
        current_question (int): The index of the current question.
        correct_answers (int): The count of correct answers.
        selected_option (tk.StringVar): The selected answer option.

    Methods:
        load_question(): Load and display the current question and answer options.
        next_question(): Proceed to the next question in the quiz.
        show_results(): Display the quiz results, including the user's score.
        return_to_dashboard(): Return to the student dashboard frame.
    """
    def __init__(self, master, student_frame, user, quiz_data):
        """
        Initializes the QuizFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            student_frame: The student dashboard frame to return to.
            user: The current user.
            quiz_data (dict): The quiz questions and answers.
        """
        super().__init__(master)
        self.master = master
        self.user = user
        self.student_frame = student_frame
        self.quiz_data = quiz_data
        self.current_question = 1
        self.correct_answers = 0
        self.selected_option = tk.StringVar(value="0") 
        
        # Create labels for question and options
        self.question_label = tk.Label(self, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)
        
        self.option_labels = []
        # Create a frame to contain the options
        options_frame = tk.Frame(self)
        options_frame.pack(pady=10)

        self.option_labels = []
        # Create a frame to contain the options
        options_frame = tk.Frame(self)
        options_frame.pack(pady=10)

        self.option_labels = []

        # Create a frame to contain the options
        options_frame = tk.Frame(self)
        options_frame.pack(pady=10)

        self.option_labels = []

        for i in range(4):

            option_label = tk.Label(options_frame, text="", font=("Arial", 12), pady=5)
            option_label.grid(row= i//2, column= i%2, padx=10, sticky="w")  # Use grid layout for option labels

            self.option_labels.append(option_label)

            option_radio = tk.Radiobutton(options_frame, variable=self.selected_option, value=str(i + 1))
            option_radio.place(in_=option_label, relx=1.0, rely=0.0)  # Place radio button right next to the option label

        # Create a Next Button
        next_button = tk.Button(self, text="Submit", background="#FF9966", font=("Arial", 15),
                                width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.next_question)
        next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        """
        Load and display the current question and answer options.
        """
        self.selected_option.set("0")  # Reset the selected option

        question_data = self.quiz_data.get(str(self.current_question))
        if question_data:
            self.question_label.config(text=question_data["text"])
            options = question_data["options"]
            for i in range(4):
                self.option_labels[i].config(text=options[i])
        else:
            # No more questions, show the results or handle accordingly
            self.show_results()

    def next_question(self):
        """
        Proceed to the next question in the quiz.
        """
        # Check if the selected answer is correct
        question_data = self.quiz_data.get(str(self.current_question))
        selected_option = self.selected_option.get()
        if question_data and selected_option == question_data["answer"]:
            # Update the count of correct answers
            self.correct_answers += 1

        # Go to the next question
        self.current_question += 1
        self.selected_option.set("")
        self.load_question()

    def show_results(self):
        """
        Display the quiz results, including the user's score.
        """
        # Calculate the user's score
        total_questions = len(self.quiz_data)
        user_score = self.correct_answers / total_questions * 100

        # Display the user's score
        self.question_label.config(text=f"You got {self.correct_answers} out of {total_questions} questions correct.")
        for i in range(4):
            self.option_labels[i].pack_forget()

        # Display the user's score as a percentage
        score_label = tk.Label(self, text=f"Your score: {user_score:.2f}%", font=("Arial", 14))
        score_label.pack(pady=10)

        # Optionally, you can provide an option to return to the dashboard or retry the quiz
        return_button = tk.Button(self, text="Return to Dashboard", background="#FF9966", font=("Arial", 15),
                                  width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.return_to_dashboard)
        return_button.pack(pady=10)

    def return_to_dashboard(self):
        """
        Return to the student dashboard frame.
        """
        # Hide the current frame
        self.place_forget()

        # Show the student dashboard frame
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

