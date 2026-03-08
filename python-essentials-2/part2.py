# Part 2: Highest of Last Two Scores
# Create a class called StudentScores which does the following:

# Takes a list of scores as input while creating the object.

# Create a method called highest_last_two() which:

# Finds the highest score among the last two scores using negative indexing.
# If the list has less than 2 scores, handle it using exception handling and print:
# Not enough scores to find highest value
# Example Input:

# scores = [45, 67, 89, 72]
# Output:

# Highest score among last two is: 89

class StudentScores:
    def __init__(self, scores):
        self.scores = scores
    
    def highest_last_two(self):
        try:
            if len(self.scores) < 2:
                raise Exception

            else:
                last_two_highest = self.scores[-2:]
                hightest_score = max(last_two_highest)
                print('Highest score among last two is: ', hightest_score)
                
        except:
            print('Not enough scores to find highest value')            
    
scores = [45, 67, 89, 72]
studentScores = StudentScores(scores)
studentScores.highest_last_two()  