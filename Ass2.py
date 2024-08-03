def find_runner_up_score(scores):
    unique_scores = set(scores)
    unique_scores.remove(max(unique_scores))
    return max(unique_scores)

n = int(input("Enter the number of participants: "))

scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

if len(scores) != n:
    print("Number of scores entered does not match the number of participantes.")
else:
    runner_up_score = find_runner_up_score(scores)
    print("The runner up score is:", runner_up_score)
