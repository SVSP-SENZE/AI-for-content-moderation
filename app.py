import os
from flask import Flask, render_template,request,jsonify
app= Flask(__name__)

@app.route('/upload',methods=['POST'])
def upload_video():
    uploaded_file=request.files['my_video']
    save_path = os.path.join(os.getcwd(), uploaded_file.filename)
    uploaded_file.save(save_path)
    return jsonify({
        "message":"file received and saved successfully"

    })
if __name__=='__main__':
    app.run(debug=True)