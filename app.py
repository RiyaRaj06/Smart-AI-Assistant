from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Question Answering
def answer_question(question):
    question = question.lower()

    if "hello" in question or "hi" in question:
        return "Hello! How can I help you today?"

    elif "how are you" in question:
        return "I am fine and ready to help you."

    elif "who are you" in question:
        return "I am your Smart AI Assistant."

    elif "what is ai" in question or "artificial intelligence" in question:
        return "Artificial Intelligence (AI) is the simulation of human intelligence by machines."

    elif "what is data science" in question:
        return "Data Science is the field of extracting useful insights from data."

    elif "what is machine learning" in question:
        return "Machine Learning is a branch of AI that enables computers to learn from data."

    elif "capital of india" in question:
        return "The capital of India is New Delhi."

    elif "capital of france" in question:
        return "The capital of France is Paris."

    elif "who invented python" in question:
        return "Python was created by Guido van Rossum in 1991."
    
    elif "good morning" in question:
        return "Good morning! Have a great day."

    elif "good evening" in question:
        return "Good evening! How can I assist you?"

    elif "what is flask" in question:
        return "Flask is a lightweight Python web framework."

    elif "what is python" in question:
        return "Python is a popular programming language known for its simplicity."

    elif "tips for studying" in question:
        return "Study regularly, make notes, practice questions, and avoid distractions."
    
    elif "what is python" in question:
        return """
Python is a high-level, interpreted programming language.

It is easy to learn and widely used in:
1. Web Development
2. Data Science
3. Artificial Intelligence
4. Machine Learning
5. Automation

Python was created by Guido van Rossum and released in 1991.
"""

    else:
        return "Sorry, I don't know the answer to that question."

# Summarization
def summarize_text(text):
    sentences = text.split(".")
    return ".".join(sentences[:2])

# Creative Content
def generate_content(topic):
    return f"""
Once upon a time, there was a magical world where {topic} changed everyone's life.
People learned valuable lessons and lived happily ever after.
"""

# Study Advice
def study_advice(topic):
    return f"""
Study Advice for {topic}:

1. Create a study timetable.
2. Practice regularly.
3. Make short notes.
4. Revise important topics.
5. Solve previous year questions.
6. Avoid distractions while studying.
7. Take short breaks to stay focused.
"""

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        function = request.form["function"]
        user_input = request.form["user_input"]

        if function == "question":
            response = answer_question(user_input)

        elif function == "summary":
            response = summarize_text(user_input)

        elif function == "creative":
            response = generate_content(user_input)

        elif function == "advice":
            response = study_advice(user_input)

    return render_template("index.html", response=response)

@app.route("/feedback", methods=["POST"])
def feedback():

    user_feedback = request.form["feedback"]

    with open("feedback.txt", "a") as file:
        file.write(user_feedback + "\n")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)