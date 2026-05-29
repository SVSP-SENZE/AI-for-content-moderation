import os
from flask import Flask, render_template, request, jsonify
from main import content_moderation

app = Flask(__name__)

# Ensure uploads directory exists
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'my_video' not in request.files:
        return jsonify({"error": "No video file part"}), 400
    
    uploaded_file = request.files['my_video']
    user_text = request.form.get('text', '') # Optional text from user

    if uploaded_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    save_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(save_path)

    # Trigger the AI content moderation pipeline
    try:
        report = content_moderation(save_path, user_text)
        return jsonify({
            "status": "success",
            "filename": uploaded_file.filename,
            "analysis_report": report
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)