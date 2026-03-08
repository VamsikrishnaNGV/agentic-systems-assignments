# Part 3: Difference Between First and Last Score
# Create a class called StudentPerformance which does the following:

# Takes a list of scores as input while creating the object.

# Create a method called score_difference() which:

# Finds the difference between the last score and the first score using indexing.
# If the list is empty, handle it using exception handling and print:
# No scores available to calculate difference
# Example Input:

# scores = [55, 65, 75, 85]
# Output:

# Difference between last and first score is: 30


class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores
    
    def score_difference(self):
        try:
            if len(self.scores) == 0: 
                raise Exception
            
            last_score = self.scores[-1]
            first_score = self.scores[0]
            
            print('Difference between last and first score is: ', last_score - first_score)
        
        except:
           print('No scores available to calculate difference')    
        
scores = [55, 65, 75, 85]
studentPerformance = StudentPerformance(scores)
studentPerformance.score_difference()