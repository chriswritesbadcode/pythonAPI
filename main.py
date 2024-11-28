from flask import Flask, request, send_file, jsonify
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.get_json()
        if not data or 'content' not in data:
            return jsonify({'error': 'Invalid input data'}), 400
        
        content = data['content']

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)

        pdf.multi_cell(0, 10, content)

        pdf_path = 'generated_document.pdf'
        pdf.output(pdf_path)

        return send_file(pdf_path, as_attachment=True, download_name='document.pdf')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)