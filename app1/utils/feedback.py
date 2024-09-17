# app1/utils/feedback.py

# Classe base para Feedback
class Feedback:
    def __init__(self, content):
        self.content = content

    def display_feedback(self):
        return self.content


# Subclasses de Feedback (usando Herança e Polimorfismo)
class TextFeedback(Feedback):
    def __init__(self, content):
        super().__init__(content)

    def display_feedback(self):
        return f"Comentário: {self.content}"


class RatingFeedback(Feedback):
    def __init__(self, rating):
        super().__init__(rating)

    def display_feedback(self):
        return f"Nota: {self.content}/10"


# Função que recebe um feedback de um usuário e retorna a exibição
def get_user_feedback(feedback_type, content):
    if feedback_type == 'text':
        feedback = TextFeedback(content)
    elif feedback_type == 'rating':
        feedback = RatingFeedback(content)
    else:
        feedback = Feedback(content)
    
    return feedback.display_feedback()
