# utils/sensor_dashboard.py

def get_city_metrics():
    # Simulated data — replace with live API or sensor integrations
    metrics = {
        "Air Quality (PM2.5)": "Moderate (74 µg/m³)",
        "Noise Level": "Low (48 dB)",
        "Water Quality (pH)": "Good (7.2)",
        "Traffic Flow": "Heavy in Downtown, Smooth elsewhere",
        "Energy Usage": "City Grid at 78% load"
    }

    result = "\n".join([f"{key}: {value}" for key, value in metrics.items()])
    return result
