import os
from flask import Flask, request, render_template
from ocr import detect
from translator import translate

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        file = request.files['file']
        
        # Check if a file was submitted
        if 'file' not in request.files:
            return "No file part"
        
        # Check if the file is empty
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Save the uploaded file
            image_path = os.path.join('uploads', file.filename)
            file.save(image_path)
            
            # Perform OCR on the uploaded image
            ocr_result = detect(image_path)
            
            return render_template('result.html', ocr_result=ocr_result)
    
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    ocr_result = request.form['ocr_result']
    selected_language = request.form['language']
    
    # Perform translation on the OCR result
    translated_text = translate(ocr_result, selected_language)
    
    return render_template('result.html', ocr_result=ocr_result, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
