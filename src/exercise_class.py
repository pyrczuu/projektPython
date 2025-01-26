import random

class Exercise:
    def __init__(self, name : str, targeted_muscle : str, easy_access : bool):
        self.name = name
        self.targeted_muscle = targeted_muscle
        self.easy_access = easy_access

    def __str__(self):
        return self.name

def choose_exercise(exercises, limited=False):
    if limited:
        available_exercises = [ex for ex in exercises if ex.easy_access]
    else:
        available_exercises = exercises
    if available_exercises:
        return available_exercises[random.randint(0, len(available_exercises) - 1)]
    else:
        return None
