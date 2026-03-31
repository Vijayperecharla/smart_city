# utils/feedback_handler.py

from transformers import pipeline

# Use a lightweight model (or replace with Granite API if available)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

CATEGORIES = {
    "garbage": "Sanitation Department",
    "traffic": "Traffic Management",
    "water": "Water Works",
    "noise": "Noise Control",
    "electricity": "Power Department",
    "pollution": "Environmental Board"
}

def classify_feedback(text):
    for keyword in CATEGORIES:
        if keyword in text.lower():
            return CATEGORIES[keyword]
    return "General Support"

def handle_feedback(issue_text):
    if not issue_text.strip():
        return "Please enter a valid issue."

    try:
        # Summarize feedback
        summary = summarizer(issue_text, max_length=50, min_length=15, do_sample=False)[0]['summary_text']
        department = classify_feedback(issue_text)

        response = f"📝 **Summary:** {summary}\n📌 **Routed to:** {department}"
        return response
    except Exception as e:
        return f"⚠️ Error processing feedback: {str(e)}"
