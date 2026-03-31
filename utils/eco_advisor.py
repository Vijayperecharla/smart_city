# utils/eco_advisor.py

from transformers import pipeline

# You can replace this with Granite Q&A or Chat API if needed
qa_pipeline = pipeline("text-generation", model="gpt2")

ECO_KNOWLEDGE = """
Here are some eco-friendly tips:
- Use LED bulbs instead of incandescent ones.
- Reduce plastic use and switch to reusable items.
- Compost kitchen waste to reduce landfill impact.
- Unplug devices when not in use.
- Install rainwater harvesting systems.
- Opt for public transport or carpooling to reduce emissions.
- Use energy-efficient appliances (look for Energy Star labels).
"""

def eco_advice(query):
    try:
        prompt = f"Based on sustainable practices, answer the following eco query:\nQuery: {query}\n{ECO_KNOWLEDGE}\nAnswer:"
        response = qa_pipeline(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
        # Remove the prompt part to keep only the generated answer
        return response.split("Answer:")[-1].strip()
    except Exception as e:
        return f"⚠️ Error generating eco advice: {str(e)}"
