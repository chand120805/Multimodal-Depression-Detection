import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PHQ_QUESTIONS = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, irritable or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself or feeling like a failure",
    "Trouble concentrating on things",
    "Moving or speaking slowly or being restless"
]

OPTIONS = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

def generate_ai_suggestions(q, texts):

    # Build structured input
    structured_input = ""

    for i in range(8):
        structured_input += f"""
        Q{i+1}: {PHQ_QUESTIONS[i]}
        Answer: {OPTIONS[q[i]]}
        User explanation: {texts[i]}
        """

    prompt = f"""
    A user completed a PHQ-8 depression assessment.

    Here are their responses:

    {structured_input}

    Based on these responses:
    Provide 3 to 5 personalized, simple, and supportive suggestions.
    Do NOT give medical diagnosis.
    Keep it short and clear.
    """


    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a helpful mental health assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        text = response.choices[0].message.content

        suggestions = [
            s.strip("- ").strip()
            for s in text.split("\n")
            if len(s.strip()) > 5
        ]

        return suggestions[:5]

    except Exception as e:
        print("GROQ ERROR:", e)

        return [
            "Maintain a healthy routine",
            "Talk to someone you trust",
            "Take care of your mental well-being"
        ]