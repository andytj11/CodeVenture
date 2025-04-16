import tkinter as tk


class WordSearchGameFrame(tk.Frame):
    """
    A class for the Word Search game frame in the tkinter interface.

    Attributes:
        master (tk.Tk): The main tkinter window.
        student_frame: The student dashboard frame for navigation.
        grid (list): A 2D grid representing the game board.
        words (list): The target words to find.
        found_words (list): Words that have been found.
        remaining_words (list): Words yet to be found.
        word_entry (tk.Entry): Entry field for entering words.
        submit_button (tk.Button): Button for submitting words.
        back_button (tk.Button): Button to go back to the student frame.
        message_label (tk.Label): Label for displaying messages.

    Methods:
        display_grid(): Display the game grid.
        check_word(): Check if the entered word is valid and in the target words.
        display_message(message, remaining_words): Display a message and update the remaining words.
        go_back_to_student_frame(): Return to the student dashboard frame.
    """
    def __init__(self, master, student_frame):
        """
        Initializes the WordSearchGameFrame.

        Args:
            master (tk.Tk): The main tkinter window.
            student_frame: The student dashboard frame for navigation.
        """
        super().__init__(master)
        self.master = master
        self.student_frame = student_frame
        self.grid = [
            ['P', 'Y', 'T', 'H', 'O', 'N', 'Q', 'W'],
            ['A', 'B', 'D', 'E', 'L', 'I', 'S', 'T'],
            ['M', 'U', 'T', 'A', 'B', 'L', 'E', 'C'],
            ['F', 'U', 'N', 'C', 'T', 'I', 'O', 'N'],
            ['L', 'O', 'O', 'P', 'R', 'A', 'N', 'D'],
            ['S', 'T', 'R', 'I', 'N', 'G', 'S', 'T'],
            ['O', 'B', 'J', 'E', 'C', 'T', 'S', 'F'],
            ['D', 'E', 'F', 'C', 'L', 'A', 'S', 'S']
        ]

        self.words = ["PYTHON", "LIST", "FUNCTION", "LOOP", "STRINGS", "OBJECT", "CLASS", "DEF"]
        self.found_words = []

        self.remaining_words = self.words.copy()

        self.word_entry = tk.Entry(self, font=("Arial", 15), width=30)
        self.word_entry.grid(row=0, column=0, columnspan=2, pady=10)

        self.submit_button = tk.Button(self, text="Submit Word", background="#FF9966", font=("Arial", 15),
                                      width=15, height=1, borderwidth=2, relief=tk.RAISED, command=self.check_word)
        self.submit_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.back_button = tk.Button(self, text="Back to Student Frame", background="#FF9966", font=("Arial", 15),
                                    width=20, height=1, borderwidth=2, relief=tk.RAISED, command=self.go_back_to_student_frame)
        self.back_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.display_grid()  # Call this method to display the grid.

        self.message_label = tk.Label(self, text="", font=("Arial", 12))
        self.message_label.grid(row=17, column=0, columnspan=2)

    def display_grid(self):
        """Display the game grid."""
        for row_index, row in enumerate(self.grid):
            grid_row = ' '.join(row)
            tk.Label(self, text=grid_row, font=("Arial", 15)).grid(row=row_index + 7, column=0, columnspan=2)

    def check_word(self):
        """Check if the entered word is valid and in the target words."""
        word = self.word_entry.get().upper()
        if word in self.remaining_words:
            self.remaining_words.remove(word)
            if word in self.words and word not in self.found_words:
                self.found_words.append(word)
                self.display_message(f"Word '{word}' found!", self.remaining_words)
            else:
                self.display_message(f"'{word}' is not a word to look for.", self.remaining_words)
        else:
            self.display_message(f"'{word}' is not a word to look for.", self.remaining_words)

    def display_message(self, message, remaining_words):
        """
        Display a message and update the remaining words.

        Args:
            message (str): The message to display.
            remaining_words (list): The list of remaining words.
        """
        if remaining_words:
            message += f" {len(remaining_words)} remaining."
        else:
            message += " All words are found. You may go back to Student Dashboard."

        self.message_label.config(text=message)
        self.word_entry.delete(0, tk.END)  # Clear the entry field

    def go_back_to_student_frame(self):
        """Return to the student dashboard frame."""
        self.place_forget()
        # Show the student dashboard frame
        self.student_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
