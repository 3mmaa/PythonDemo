import random

def average(group_members):
    total_experience = 0
    for member in group_members:
        experience = float(input(f"Please enter {member}'s experience in Python (0-10): "))
        if 0 <= experience <= 10:
            total_experience += experience
        else:
            print(f"Invalid input for {member}'s experience. Please enter a value between 0 and 10.")
    
    if len(group_members) > 0:
        avg_experience = total_experience / len(group_members)
        return avg_experience
    else:
        return 0

# Generate a random group size between 5 and 15
group_size = random.randint(5, 15)
group_members = [f"Member {i}" for i in range(1, group_size + 1)]

avg = average(group_members)
print(f"The average experience in the group is: {avg:.2f}")