from flask import Flask, jsonify, render_template, request
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

s3 = boto3.client('s3')
bucket_name = 'meu-site-galeria-imagens'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_images', methods=['GET'])
def get_images():
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix='uploads/')
    
    image_keys = [
        content['Key'] for content in response.get('Contents', [])
        if content['Key'] != 'uploads/' and content['Key'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf'))
    ]

    image_urls = [
        s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600
        )
        for key in image_keys
    ]

    return jsonify(image_urls)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'message': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'Nome de arquivo inválido'}), 400

    filename = secure_filename(file.filename)
    s3.upload_fileobj(file, bucket_name, f'uploads/{filename}')
    return jsonify({'message': 'Arquivo enviado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
