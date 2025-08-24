from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

MENU_TEXT = (
    "✨ Welcome to Hypertensio - Your Hypertension Support Bot! ✨\n"
    "Reply with the number or keyword for info:\n"
    "1. What is Hypertension? 🩺 (hypertension, high blood pressure)\n"
    "2. Symptoms of Hypertension 🤒 (symptoms, headache, dizziness)\n"
    "3. Causes & Risk Factors ⚠️ (causes, risk factors)\n"
    "4. Lifestyle Tips 🍎 (lifestyle, diet, exercise)\n"
    "5. Medication & Monitoring 💊 (medication, meds, monitoring)\n"
    "6. When to Seek Help 🚨 (help, urgent, emergency)\n"
    "7. Contact Local Clinic or Doctor 📞 (clinic, doctor, contact)\n"
    "8. Volunteer as Doctor 🙌 (volunteer, doctor, help)\n"
    "9. Blood Pressure Facts 📊 (blood pressure, facts)\n\n"
    "For personalized tracking & reminders 🔔, use our Firebase app: "
    "https://studio--hypertensio.us-central1.hosted.app ❤️\n"
    "Type 'menu' anytime to see this menu again."
)

FIREBASE_PROMPT = "\n\n🔔 Get personalized tracking & reminders: https://studio--hypertensio.us-central1.hosted.app ❤️"

SA_MEDICAL_CONTACTS = (
    "📞 South African Medical Contacts:\n"
    "- Healthline SA: 0800 22 22 23\n"
    "- Netcare 911 Emergency: 082 911\n"
    "- Discovery Health Clinic Finder: 0860 99 88 77\n"
    "- SAMA Email: info@samedical.org\n"
    "- Dept of Health Hotline: 0800 61 10 11\n"
    "\nVisit healthline.co.za | discovery.co.za | samedical.org | health.gov.za\n"
    "Call Netcare 911 immediately if it’s an emergency 🚑."
)

BP_FACTS = (
    "📊 Blood Pressure Facts:\n"
    "- Normal: Around 120/80 mmHg\n"
    "- Elevated: 120-129/<80 mmHg\n"
    "- Stage 1: 130-139/80-89 mmHg\n"
    "- Stage 2: 140+/90+ mmHg\n"
    "- Low: Below 90/60 mmHg\n"
    "If high, lifestyle changes or medication may be necessary.\n"
    "If low and symptomatic, drink fluids and see a doctor."
)

INFO_TEXTS = {
    '1': "🩺 Hypertension means high blood pressure, forcing your heart to work harder. "
         "Symptoms often don’t show." + FIREBASE_PROMPT,
    '2': "🤒 Symptoms often don’t show but may include headaches, dizziness, and rare nosebleeds. "
         "Regular monitoring is important." + FIREBASE_PROMPT,
    '3': "⚠️ Causes & risk factors: family history, high salt intake, obesity, inactivity, smoking, alcohol, stress." + FIREBASE_PROMPT,
    '4': "🍎 Lifestyle tips:\n- Reduce salt intake\n- Exercise regularly\n- Maintain a healthy weight\n"
         "- Manage stress\n- Avoid tobacco & limit alcohol" + FIREBASE_PROMPT,
    '5': "💊 Medication may be needed to control blood pressure. Follow your doctor’s instructions and take meds on time." + FIREBASE_PROMPT,
    '6': "🚨 Seek urgent help if you experience:\n- Severe headache\n- Chest pain\n- Sudden weakness\n"
         "- Difficulty breathing\n- Confusion or vision problems" + FIREBASE_PROMPT,
    '7': SA_MEDICAL_CONTACTS + FIREBASE_PROMPT,
    '8': "🙌 Interested in volunteering? Visit our Firebase app to sign up and help underserved communities.",
    '9': BP_FACTS + FIREBASE_PROMPT
}

KEYWORDS = {
    '1': ['hypertension', 'high blood pressure'],
    '2': ['symptoms', 'headache', 'dizziness', 'nosebleed'],
    '3': ['causes', 'risk factors', 'family history', 'obesity', 'salt', 'smoking', 'alcohol', 'stress'],
    '4': ['lifestyle', 'diet', 'exercise', 'weight', 'stress management'],
    '5': ['medication', 'meds', 'monitoring', 'medicine', 'doctor advice'],
    '6': ['help', 'urgent', 'emergency', 'chest pain', 'weakness', 'confusion'],
    '7': ['clinic', 'doctor', 'contact', 'healthline', 'netcare'],
    '8': ['volunteer', 'doctor', 'help', 'signup'],
    '9': ['blood pressure', 'facts', 'bp', 'pressure']
}

def handle_message(body):
    incoming_msg = body.strip().lower()
    if incoming_msg in ['hi', 'hello', 'start', 'menu', '?']:
        return MENU_TEXT
    # Check if the user sent a number
    if incoming_msg in INFO_TEXTS:
        return INFO_TEXTS[incoming_msg]
    # Check if the message contains a keyword
    for key, keywords in KEYWORDS.items():
        if any(word in incoming_msg for word in keywords):
            return INFO_TEXTS[key]
    return "❓ Sorry, I didn't understand that. Reply with a number or keyword, or type 'menu' to see options."

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    resp = MessagingResponse()
    resp.message(handle_message(request.values.get('Body', '')))
    return str(resp)

@app.route('/sms', methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    resp.message(handle_message(request.values.get('Body', '')))
    return str(resp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
