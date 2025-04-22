class Question:
    '''Custom class for user object'''
    def __init__(self, q_text: str, q_answer: str) -> None:
        '''Constructor method to initialise attributes'''
        self.text = q_text
        self.answer = q_answer
