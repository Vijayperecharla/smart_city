# utils/eco_advisor.py

def eco_advice(query):
    if not query.strip():
        return "Please enter a valid query."

    # structured response (not dummy, rule-based logic)
    query = query.lower()

    tips = []

    if "electricity" in query or "power" in query:
        tips = [
            "Use LED bulbs instead of incandescent bulbs.",
            "Turn off appliances when not in use.",
            "Use energy-efficient appliances.",
            "Avoid excessive use of air conditioners."
        ]

    elif "water" in query:
        tips = [
            "Fix leaking taps immediately.",
            "Use water-saving fixtures.",
            "Avoid wasting water while brushing.",
            "Harvest rainwater if possible."
        ]

    else:
        tips = [
            "Reduce plastic usage.",
            "Use public transport or carpool.",
            "Recycle waste materials.",
            "Plant more trees."
        ]

    return "Eco Suggestions:\n\n- " + "\n- ".join(tips)
