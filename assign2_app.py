import time
import assign2_funcs as runner

print("\n")

# The sections from the home page
sections = runner.scrape_home()

# the questions for the section
for section in sections:
    questions = runner.scrape_section(section)
    for question in questions:
        # the details of the question
        question_detail = runner.scrape_question(question)
        print(question + "\n" + question_detail + "\n\n")
        with open("out.txt", "a") as file:
            file.write(question + "\n" + question_detail + "\n\n")
        time.sleep(3)