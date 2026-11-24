user_scores = []

for i in range(5):
    i += 1
    user_score = int(input(f"Enter Quiz {i} score: "))
    user_scores.append(user_score)

quantity = len(user_scores)
total = sum(user_scores)
ave = sum(user_scores)/len(user_scores)
highest = max(user_scores)
lowest = min(user_scores)
ascend = sorted(user_scores)
descend = sorted(user_scores, reverse = True)

print()
print("===== QUIZ SCORE REPORT =====")
print(f"Quiz Scores: {user_scores}")
print(f"Number of Quizzes: {quantity}")
print(f"Total Score: {total}")
print(f"Average Score: {ave:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Ascending: {ascend}")
print(f"Descending: {descend}")
print(f"Original Scores {user_scores}")