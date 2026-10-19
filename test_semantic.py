
from semantic_comparison import calculate_semantic_similarity

sentence1 = "I developed a Python application."
sentence2 = "I created a software program using Python."
sentence3 = "The weather is sunny today."

score1 = calculate_semantic_similarity(sentence1, sentence2)
score2 = calculate_semantic_similarity(sentence1, sentence3)

print("Similar sentences score:", round(score1, 2), "%")
print("Different sentences score:", round(score2, 2), "%")
