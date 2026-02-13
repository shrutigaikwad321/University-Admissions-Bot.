from flask import Flask, render_template, request, jsonify
from admissions_data import programs, compress_requirements, recommend_program

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    # Requirement Compression
    for program in programs:
        if program.lower() in user_message:
            summary = compress_requirements(programs[program])
            return jsonify({"response": summary})

    # Recommendation Mode
    if "recommend" in user_message:
        response = recommend_program(user_message)
        return jsonify({"response": response})

    # Timeline Mode
    if "timeline" in user_message:
        return jsonify({"response": """
📅 Application Timeline:
1. Research Programs
2. Check Eligibility
3. Prepare Documents
4. Fill Application Form
5. Pay Application Fee
6. Attend Interview (if required)
7. Confirm Admission
        """})

    return jsonify({"response": "Please ask about a specific program or type 'recommend' for suggestions."})

if __name__ == "__main__":
    app.run(debug=True)
