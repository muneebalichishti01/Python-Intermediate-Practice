from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def run_quiz_game() -> None:
    '''Function to implement main logic of program'''
    question_bank = []
    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
        
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You have completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")

def main() -> None:
    '''Main Function to run the program'''
    try:
        run_quiz_game()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
