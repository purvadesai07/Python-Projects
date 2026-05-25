import time
import random
sentences = [
    "Python is fun to learn.",
    "I like travelling a lot.",
    "I want to learn new languages.",
    "I wish to live at New York.",
    "I wish to get a job at My Dream Company.",
]
sentence = random.choice(sentences)
print(sentence)

print("------------------------TYPING SPEED TEXTER------------------------")
print("Type the following sentence: ")
print(sentence)
input("Press ENTER to start......")

start = time.time()
typed = input("Start Typing: ")
end = time.time()
time_taken = end - start

word_count = len(sentence.split())
wpm = (word_count / time_taken) * 60

correct_chars = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
         correct_chars += 1
accuracy = (correct_chars / len(sentence)) * 100

print("-----------------Results ----------------------")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Words Per Minute:", round(wpm, 2))
print("Accuracy:", round(accuracy, 2), "%")

if accuracy == 100:
    print("Excellent typing! 🎉")
elif accuracy >= 80:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")
