from flask import Flask, request, jsonify

app = Flask(__name__)

# Example symptom-disease mapping for demonstration
SYMPTOM_MAP = {
    "fever": ["Flu", "COVID-19", "Malaria"],
    "headache": ["Migraine", "Stress", "Dehydration"],
    "fatigue": ["Anemia", "Thyroid issues", "Overwork"],
    "cough": ["Common Cold", "Bronchitis", "COVID-19"],
}


@app.route("/check", methods=["POST"])
def check_symptoms():
    data = request.json
    symptoms = data.get("symptoms", "").lower()

    # Basic symptom matching
    matches = []
    for symptom, diseases in SYMPTOM_MAP.items():
        if symptom in symptoms:
            matches.append(f"{symptom.capitalize()}: {', '.join(diseases)}")

    # Build response
    if matches:
        analysis = "Possible conditions based on your symptoms:\n\n" + "\n".join(matches)
    else:
        analysis = "No matching conditions found. Please consult a healthcare provider."

    return jsonify({"analysis": analysis})


if __name__ == "__main__":
    app.run(debug=True)
