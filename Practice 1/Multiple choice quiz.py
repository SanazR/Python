from Question import Questions
question_prompts=[
    "What color are apples?\na) Red\nb) Blue\nc) Black\n\n",
    "What is the answer of 2*64?\na) 256\nb) 128\nc) 72\n\n",
    "What is the natural and basic shape?\na) Square\nb) Circle\nc) Triangle\n\n"
]


questions= [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "b"),
    Questions(question_prompts[2], "c"),
]



def run_test(questions):
    score = 0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You Got " + str(score) +" / " + str(len(questions)) + " corret.")

run_test(questions)