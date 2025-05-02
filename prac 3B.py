# Candidates
candidates = ["Smanga", "Luzuko", "Nontobeko"]
votes = [0, 0, 0]  # To store votes for each candidate

voter = 1
while voter <= 10:
    print("Vote for your class rep:")
    print("1. Smanga")
    print("2. Luzuko")
    print("3. Nontobeko")
    choice = int(input(f"Voter {voter}, enter your choice (1-3): "))

    if 1 <= choice <= 3:
        votes[choice - 1] += 1
        voter += 1
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

print()
# Calculate total votes
print("---------------------------------")
total_votes = sum(votes)

# Display results
print("--------- Polling Results ----------")
i = 0
while i < len(candidates):
    percentage = (votes[i] / total_votes) * 100
    print(f"{candidates[i]}: {votes[i]} votes ({percentage:.1f}%)")
    i += 1

print(f"Total votes cast: {total_votes}")
print("--------- Polling Results ----------")