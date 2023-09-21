import random
import main as m
say = m.engine

# Define an empty dictionary to store Danish-English sentence pairs
danish_english = {}
files = ["question", "mix"]
# Read sentences from a text file in the specified format

def readIn(danish_english, files):
    for f in files:
        with open(f+".txt", 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split('|')
                if len(parts) == 2:
                    danish_english[parts[0].strip()] = parts[1].strip()
    return danish_english

# Function to generate a quiz question with 5 possible answers
def generate_quiz_question(danish_english):
    # Select a random Danish sentence as the question
    question = random.choice(list(danish_english.keys()))
    
    # Select the correct English translation
    correct_answer = danish_english[question]
    
    # Create a list of possible answers
    answers = [correct_answer]
    
    # Generate 4 more random incorrect answers
    while len(answers) < 5:
        random_answer = random.choice(list(danish_english.values()))
        if random_answer not in answers:
            answers.append(random_answer)
    
    # Shuffle the answers so that the correct answer is not always in the same position
    random.shuffle(answers)
    
    return question, correct_answer, answers

# Generate a quiz question
question, correct_answer, answers = generate_quiz_question(readIn(danish_english, files))

# Print the question and possible answers
print("Translate the following Danish sentence to English:")

print(question)



for i, answer in enumerate(answers):
    print(f"{i + 1}. {answer}")
    
# say it
text = question
say.say(text)
say.runAndWait()

# Prompt the user to select an answer (1-5)
user_choice = int(input("Enter the number of your answer (1-5): "))


# Check if the user's answer is correct
if answers[user_choice - 1] == correct_answer:
    print("Correct! Well done.")
else:
    print("Incorrect. The correct answer is:", correct_answer)