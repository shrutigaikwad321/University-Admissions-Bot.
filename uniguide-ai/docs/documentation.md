
📘 PROJECT DOCUMENTATION
🎓 University Admissions Bot – UniGuide AI
1️⃣ Introduction

The University Admissions Bot (UniGuide AI) is a web-based intelligent chatbot designed to simplify and compress university admission requirements and application guidelines.

Students often face confusion while understanding eligibility criteria, entrance exams, document requirements, and timelines. This chatbot provides:

Summarized program requirements

Smart program recommendations

Application timelines

Admission checklist guidance

The system is built using:

Python (Flask)

HTML

CSS

JavaScript

No database or hardware components are used.

2️⃣ Problem Statement

Students struggle with:

Complex admission requirements

Multiple entrance exams

Document confusion

Lack of clear application guidance

There is a need for a simple, interactive digital assistant that:

Compresses long eligibility information

Guides students step-by-step

Provides quick answers instantly

3️⃣ Objectives

To design an interactive chatbot for university admissions.

To summarize and compress program requirements.

To recommend suitable programs based on student stream.

To generate admission timelines.

To provide a document checklist.

4️⃣ System Architecture
Architecture Type:

Client-Server Web Architecture

User (Browser)
      ↓
HTML/CSS/JS Frontend
      ↓
Flask Backend (app.py)
      ↓
Admissions Data Logic (admissions_data.py)

Components:

Frontend

Chat UI

Sends user message using JavaScript fetch API

Backend

Receives user message

Processes keyword-based logic

Returns summarized response

Data Module

Contains program details

Contains compression and recommendation logic

5️⃣ Features
1. Requirement Compression

Converts long program descriptions into short bullet-point format.

2. Program Recommendation

Suggests programs based on:

Science → BTech

Commerce → BBA/MBA

Arts → BBA

3. Application Timeline Generator

Provides step-by-step admission process.

4. Document Checklist Guidance

Displays required documents.

5. Interactive Chat Interface

Real-time messaging system using fetch API.

6️⃣ Technologies Used
Technology	Purpose
Python	Backend logic
Flask	Web framework
HTML	Structure
CSS	Styling
JavaScript	Chat interaction
JSON	Data communication
7️⃣ Working Methodology

User types a query in the chat interface.

JavaScript sends the message to Flask backend.

Backend checks:

If program name exists → compress requirements

If "recommend" keyword → recommend program

If "timeline" keyword → show steps

Response is sent back as JSON.

Frontend displays response.

8️⃣ Advantages

No database required

Lightweight and fast

Easy to expand

Beginner-friendly architecture

Can be upgraded to AI/NLP version

9️⃣ Limitations

Keyword-based logic (not advanced NLP)

Static data

No user authentication

🔟 Future Enhancements

Integration with AI API (OpenAI)

PDF document upload verification

Voice-based interaction

University-specific filtering

Admission deadline reminders

Admin panel

Database integration

1️⃣1️⃣ Conclusion

The University Admissions Bot successfully simplifies the admission process by compressing complex guidelines into easy-to-understand summaries. It improves student experience and reduces confusion during college applications.

The system is scalable and can be enhanced with AI and NLP techniques in the future.