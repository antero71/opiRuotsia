class Checker():
    def __init__(self, right_answer):
        self.right_answer=right_answer


    def check(self,answer):
        print(len(self.right_answer))
        points = 0
        for a in self.right_answer:
            if answer.__contains__(a) and len(self.right_answer)==4:
                points += 1
            elif answer.__contains__(a) and len(self.right_answer)==2:
                points += 2
            elif answer.__contains__(a) and len(self.right_answer)==1:
                points += 4
            elif answer.__contains__(a) and len(self.right_answer)==3:
                points += 4
        #print("points ", points)
        if points > 0 and points < 4 and len(self.right_answer)<4:
            points=4
        #print("You get ", points," points")
        return points