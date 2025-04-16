# Testing quiz
import pytest
from quiz import Quiz, load_questions

# Sample questions for testing
sample_questions = {
    "1": {
        "text": "Sample question?",
        "options": ["A", "B", "C", "D"],
        "answer": 1
    }
}


def test_load_questions():
    # Positive Test: Check if function loads questions correctly
    assert load_questions('quiz_content.json') is not None

    # Negative Test: Check if function returns None when file is not found
    with pytest.raises(FileNotFoundError):
        load_questions('quiz_content2.json')


def test_initialize_quiz():
    # Positive Test: Check if quiz initializes with a score of 0
    quiz = Quiz(sample_questions)
    assert quiz.score == 0

    # Negative Test: Check if quiz initializes with a score of 1 or something else
    quiz = Quiz(sample_questions)
    assert quiz.score != 1

    quiz = Quiz(sample_questions)
    assert quiz.score != 1.0

    quiz = Quiz(sample_questions)
    assert quiz.score != True

    quiz = Quiz(sample_questions)
    assert quiz.score != ()

    quiz = Quiz(sample_questions)
    assert quiz.score != "a"


def test_check_answer():
    quiz = Quiz(sample_questions)
    # Positive Test: Check if correct answer is identified
    assert quiz.check_answer(1) == True

    # Negative Test: Check if incorrect answer is identified
    assert quiz.check_answer(2) == False

    assert quiz.check_answer(3) == False

    assert quiz.check_answer(4) == False


def test_has_more_questions():
    quiz = Quiz(sample_questions)
    # Positive Test: Check if there are more questions initially
    assert quiz.has_more_questions() == True

    # Negative Test: Check if there are no more questions initially
    assert quiz.has_more_questions() != False


def test_display_final_score(capsys):
    quiz = Quiz(sample_questions)
    quiz.display_final_score()
    captured = capsys.readouterr()
    # Positive Test: Check if the final score is displayed
    assert "Your score:" in captured.out





