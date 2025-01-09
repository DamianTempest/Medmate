from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data mapping
HEALTH_TIPS = {
    "general": [
        "Drink at least 8 glasses of water daily.",
        "Include more fruits and vegetables in your diet.",
        "Get at least 7 hours of sleep every night.",
    ],
    "diabetes": ["Monitor your blood sugar levels regularly.", "Avoid sugary foods."],
    "hypertension": [
        "Reduce your salt intake.",
        "Engage in 30 minutes of physical activity daily.",
    ],
}

REMINDERS = [
    "Take your medication on time.",
    "Schedule your annual health check-up.",
    "Get your flu vaccination this month.",
]


@app.route("/health_tips", methods=["POST"])
def health_tips():
    data = request.json
    user_data = data.get("user_data", "").lower()

    tips = set(HEALTH_TIPS["general"])  # General health tips

    # Analyze user data to provide personalized tips
    if "diabetes: yes" in user_data:
        tips.update(HEALTH_TIPS["diabetes"])
    if "hypertension: yes" in user_data:
        tips.update(HEALTH_TIPS["hypertension"])

    # Include reminders
    tips.update(REMINDERS)

    return jsonify({"tips": "\n".join(tips)})


if __name__ == "__main__":
    app.run(debug=True)
