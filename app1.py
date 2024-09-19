from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # This allows your frontend to make requests to this server

def get_bot_response(user_message):
    # This function contains the logic for generating bot responses
    # You can expand this to include more complex logic, database queries, etc.
    user_message = user_message.lower()
    if 'admission' in user_message:
        return "For admission inquiries, please visit our Admissions Office or check our website's Admissions page for detailed information about the application process, requirements, and deadlines."
    elif 'courses' in user_message or 'programs' in user_message:
        return "We offer a wide range of undergraduate and graduate programs. You can find a complete list of our courses and programs on our Academic Programs page."
    elif 'tuition' in user_message or 'fees' in user_message:
        return "Tuition and fees vary depending on the program and student status. Please check our Financial Services page for detailed information about costs and payment options."
    elif 'campus' in user_message or 'facilities' in user_message:
        return "Our campus features state-of-the-art classrooms, laboratories, libraries, sports facilities, and student housing. Take a virtual tour on our website to explore our campus!"
    elif 'scholarship' in user_message:
        return "We offer various scholarships based on academic merit, need, and special talents. Visit our Financial Aid office or check the Scholarships section on our website for more information."
    else:
        return "I'm sorry, I don't have specific information about that. Please check our website or contact our admissions office for more detailed assistance."

time.sleep(5)
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)