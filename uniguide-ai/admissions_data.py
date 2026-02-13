programs = {
    "btech": """
Eligibility: 12th with PCM, Minimum 60%.
Entrance Exam Required (JEE/MHT-CET).
Duration: 4 Years.
Documents: Marksheet, ID Proof, Entrance Scorecard.
    """,

    "bba": """
Eligibility: 12th any stream, Minimum 50%.
No entrance required in some colleges.
Duration: 3 Years.
Documents: Marksheet, ID Proof.
    """,

    "mba": """
Eligibility: Graduation with 50%.
Entrance Exam (CAT/MAT).
Duration: 2 Years.
Documents: Degree Certificate, ID Proof.
    """
}

def compress_requirements(text):
    lines = text.strip().split("\n")
    summary = "📌 Program Requirements:\n"
    for line in lines:
        summary += "• " + line.strip() + "\n"
    return summary

def recommend_program(user_input):
    if "science" in user_input:
        return "🔍 Recommended: BTech"
    elif "commerce" in user_input:
        return "🔍 Recommended: BBA or MBA"
    elif "arts" in user_input:
        return "🔍 Recommended: BBA"
    else:
        return "Please mention your stream (Science/Commerce/Arts)."
