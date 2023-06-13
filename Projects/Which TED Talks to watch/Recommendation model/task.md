# Compute similarities
We need a similarity measure to compute how similar each TED Talk is to every other TED Talk. 
A common choice is the cosine similarity, which measures the cosine of the angle between two vectors. 
The closer the cosine similarity is to 1, the more similar the items are.

# Create a function for recommendations 
The function should take the title of a TED Talk and output recommendations. To get recommendations, we will get the index of the TED Talk in our DataFrame, get the list of cosine similarity scores for that TED Talk, and then sort the scores to get the indexes of the TED Talks with the highest similarity. We can then use these indexes to get the recommended TED Talks from our DataFrame.

# Task
Fill in the code in the [task.py](file://task.py) file.

**Important Note:** Please note, this is a simple example and the quality of the recommendations can be significantly improved with 
more sophisticated preprocessing and by using more relevant content to compute the similarities. 
For example, you could use more sophisticated NLP techniques during preprocessing.
