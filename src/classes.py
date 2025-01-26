from typing import List
from src.exercises import *
import exercise_class
from exercise_class import Exercise
from exercise_class import choose_exercise
import random

class PPL:
    def __init__(self, limited = False):
        self.plan = {"Push A": List[Exercise], "Pull A": List[Exercise],"Legs A": List[Exercise],
                     "Push B": List[Exercise], "Pull B": List[Exercise],"Legs B": List[Exercise]}
        self.limited = limited
        self.generatePlan(self.limited)

    def generatePlan(self, limited : bool):
        for workout in self.plan:
            temp = []
            if limited:
                if workout.startswith("Push"):
                    temp.append(choose_exercise(chest_exercises, limited=True))
                    temp.append(choose_exercise(chest_exercises, limited=True))
                    temp.append(choose_exercise(shoulder_exercises, limited=True))
                    temp.append(choose_exercise(triceps_exercises, limited=True))
                    temp.append(choose_exercise(triceps_exercises, limited=True))
                elif workout.startswith("Pull"):
                    temp.append(choose_exercise(back_exercises, limited=True))
                    temp.append(choose_exercise(back_exercises, limited=True))
                    temp.append(choose_exercise(shoulder_exercises, limited=True))
                    temp.append(choose_exercise(bicep_exercises, limited=True))
                    temp.append(choose_exercise(bicep_exercises, limited=True))
                elif workout.startswith("Legs"):
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
            else:
                if workout.startswith("Push"):
                    temp.append(choose_exercise(chest_exercises))
                    temp.append(choose_exercise(chest_exercises))
                    temp.append(choose_exercise(shoulder_exercises))
                    temp.append(choose_exercise(triceps_exercises))
                    temp.append(choose_exercise(triceps_exercises))
                elif workout.startswith("Pull"):
                    temp.append(choose_exercise(back_exercises))
                    temp.append(choose_exercise(back_exercises))
                    temp.append(choose_exercise(shoulder_exercises))
                    temp.append(choose_exercise(bicep_exercises))
                    temp.append(choose_exercise(bicep_exercises))
                elif workout.startswith("Legs"):
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
            self.plan[workout] = temp


    def __str__(self):
        output = ""
        for name, exercises in self.plan.items():
            output += f"{name}\n"
            for exercise in exercises:
                output += f"    {exercise}\n"
        return output

class UL:
    def __init__(self, limited = False):
        self.plan = {"Upper A": List[Exercise], "Lower A": List[Exercise],
                     "Upper B": List[Exercise], "Lower B": List[Exercise],
                     "Upper C": List[Exercise], "Lower C": List[Exercise]}
        self.limited = limited
        self.generatePlan(self.limited)

    def generatePlan(self, limited : bool):
        for workout in self.plan:
            temp = []
            if limited:
                if workout.startswith("Upper"):
                    temp.append(choose_exercise(chest_exercises, limited=True))
                    temp.append(choose_exercise(back_exercises, limited=True))
                    temp.append(choose_exercise(shoulder_exercises, limited=True))
                    temp.append(choose_exercise(bicep_exercises, limited=True))
                    temp.append(choose_exercise(triceps_exercises, limited=True))
                elif workout.startswith("Lower"):
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
                    temp.append(choose_exercise(leg_exercises, limited=True))
                self.plan[workout] = temp
            else:
                if workout.startswith("Upper"):
                    temp.append(choose_exercise(chest_exercises))
                    temp.append(choose_exercise(back_exercises))
                    temp.append(choose_exercise(shoulder_exercises))
                    temp.append(choose_exercise(bicep_exercises))
                    temp.append(choose_exercise(triceps_exercises))
                elif workout.startswith("Lower"):
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
                    temp.append(choose_exercise(leg_exercises))
                self.plan[workout] = temp

    def __str__(self):
        output = ""
        for name, exercises in self.plan.items():
            output += f"{name}\n"
            for exercise in exercises:
                output += f"    {exercise}\n"
        return output

class FB:
    def __init__(self, limited = False):
        self.plan = {"Fullbody A": List[Exercise], "Fullbody B": List[Exercise], "Fullbody C": List[Exercise]}
        self.limited = limited
        self.generatePlan(self.limited)

    def generatePlan(self, limited : bool):
        for workout in self.plan:
            temp = []
            if limited:
                temp.append(choose_exercise(chest_exercises, limited=True))
                temp.append(choose_exercise(back_exercises, limited=True))
                temp.append(choose_exercise(shoulder_exercises, limited=True))
                temp.append(choose_exercise(bicep_exercises, limited=True))
                temp.append(choose_exercise(triceps_exercises, limited=True))
                temp.append(choose_exercise(leg_exercises, limited=True))
            else:
                temp.append(choose_exercise(chest_exercises))
                temp.append(choose_exercise(back_exercises))
                temp.append(choose_exercise(shoulder_exercises))
                temp.append(choose_exercise(bicep_exercises))
                temp.append(choose_exercise(triceps_exercises))
                temp.append(choose_exercise(leg_exercises))
            self.plan[workout] = temp


    def __str__(self):
        output = ""
        for name, exercises in self.plan.items():
            output += f"{name}\n"
            for exercise in exercises:
                output += f"    {exercise}\n"
        return output
