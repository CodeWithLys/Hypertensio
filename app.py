from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

MENU_TEXT = (
    "✨ Welcome to Hypertensio - Your Hypertension Support Bot! ✨\n"
    "Reply with the number for info:\n"
    "1. What is Hypertension? 🩺\n"
    "2. Symptoms of Hypertension 🤒\n"
    "3. Causes & Risk Factors ⚠️\n"
    "4. Lifestyle Tips 🍎\n"
    "5. Medication & Monitoring 💊\n"
    "6. When to Seek Help 🚨\n"
    "7. Contact Local Clinic or Doctor 📞\n"
    "8. Volunteer as Doctor 🙌\n"
    "9. Blood Pressure Facts 📊\n\n"
    "For personalized tAI assistant, doctors volunteer, tracking, reminders & MORE🔔, use our Firebase app: https://9000-firebase-studio-1754428033239.cluster-kc2r6y3mtba5mswcmol45orivs.cloudworkstations.dev ❤️\n"
    "Type 'menu' anytime to see this menu again."
)

FIREBASE_PROMPT = "\n\n🔔 Want personalized tracking & reminders? Use our Firebase app: https://9000-firebase-studio-1754428033239.cluster-kc2r6y3mtba5mswcmol45orivs.cloudworkstations.dev ❤️"

BP_FACTS = (
    "📊 Blood Pressure Facts:\n"
    "- Normal: Around 120/80 mmHg\n"
    "- Elevated: 120-129/<80 mmHg\n"
    "- High (Hypertension Stage 1): 130-139/80-89 mmHg\n"
    "- High (Hypertension Stage 2): 140+/90+ mmHg\n"
    "- Low blood pressure: Below 90/60 mmHg\n"
    "If high, lifestyle changes or meds may be needed.\n"
    "If low and symptomatic, drink fluids, eat small meals, and see a doctor."
)

SA_MEDICAL_CONTACTS = (
    "📞 South African Medical Contacts:\n"
    "- Healthline SA: 0800 22 22 23\n"
    "- Netcare 911 Emergency: 082 911\n"
    "- Discovery Health Clinic Finder: 0860 99 88 77\n"
    "- South African Medical Association: info@samedical.org\n"
    "- Department of Health Hotline: 0800 61 10 11\n"
    "\n🌐 Visit their sites for clinic locations:\n"
    "healthline.co.za | discovery.co.za | samedical.org | health.gov.za\n"
    "For emergencies, call Netcare 911 immediately 🚑."
)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['hi', 'hello', 'start', 'menu', '?']:
        msg.body(MENU_TEXT)

    elif incoming_msg == '1':
        msg.body(
            "🩺 Hypertension means high blood pressure, forcing your heart to work harder and "
            "may cause serious problems over time. It's called the 'silent killer' as symptoms "
            "often don’t show."
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '2':
        msg.body(
            "🤒 Symptoms often don’t show, but may include headaches, dizziness, and rare nosebleeds. "
            "Regular monitoring is important."
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '3':
        msg.body(
            "⚠️ Causes & risk factors: family history, high salt intake, obesity, inactivity, smoking, alcohol, stress."
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '4':
        msg.body(
            "🍎 Lifestyle tips:\n- Reduce salt intake\n- Exercise regularly\n- Maintain a healthy weight\n"
            "- Manage stress\n- Avoid tobacco & limit alcohol"
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '5':
        msg.body(
            "💊 Medication may be needed to control blood pressure. Follow your doctor's instructions and "
            "take your meds on time."
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '6':
        msg.body(
            "🚨 Seek urgent help if you experience:\n"
            "- Severe headache\n- Chest pain\n- Sudden weakness\n- Difficulty breathing\n- Confusion or vision problems"
            + FIREBASE_PROMPT
        )

    elif incoming_msg == '7':
        msg.body(SA_MEDICAL_CONTACTS + FIREBASE_PROMPT)

    elif incoming_msg == '8':
        msg.body(
            "🙌 Interested in volunteering? Visit our Firebase app to sign up and help underserved communities."
        )

    elif incoming_msg == '9':
        msg.body(BP_FACTS + FIREBASE_PROMPT)

    else:
        msg.body("❓ Sorry, I didn't understand that. Please select a number from the menu:\n" + MENU_TEXT)

    return str(resp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
