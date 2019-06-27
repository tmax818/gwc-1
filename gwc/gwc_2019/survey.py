# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]
keys = ["name", "age", "hometown", "DOB"]
all_responses = []

done = "no"
while done == "no":
# Iterate over the list of survey questions and take in user responses.
    # Create the dictionary to store the responses.
    answers = {}
    for x in range(len(survey)):
        response = input(survey[x] + ":     ")
        #keys[x] gives the label for each response (name, age)
        #answers[keys[x]] creates an entry in the dictionary with the key we want and sets the value to the response
        answers[keys[x]] = response

    all_responses.append(answers)
    done = input("Are you finished collecting responses? (yes/no) ")

# Print the entire dictionary.
print(all_responses)
