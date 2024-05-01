print("Hello")
print("SonChaFa")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "Loveable things"
character_quality = "Living Life"
print(character_name + " and Relationship always comes with responsibilities")
print("Along with the happiness you have to be ready to deal with annoying situations")
print("If you are living with family," + character_quality + " becomes actually easy")
print("After all " + character_name + " makes " + character_quality + " complete ")





from MCQs import Question
question_prompts = [
    "Who is the first person of India?\n(a) President\n(b) Prime minister\n(c) Home minister\n(d) chief minister\n\n" ,
    "Who is the first president of india?\n(a) Dr.Rajendra Prasad\n(b) Dr. B.R.Ambedkar\n(c) Lal Bahadur Shastri\n(d) Jawaharlal Nehru\n\n" ,
    "Which of the following is Constitution day of india?\n(a) 15th August\n(b) 26th January\n(c) 26th November\n(d) 22 January\n\n" ,
    "Who is the fisrt indian who passed out ICA exam conducted by british?\n(a) Satyenranath Tagore\n(b) B.R.Ambedkar\n (c) Swami Vivekanand\n(d) Raja Ram Mohan Roy\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + "correct" )

run_test(questions)