import boto3
from flask import Flask, jsonify, render_template

app = Flask(__name__)

s3 = boto3.client('s3')
bucket_name = 'meu-site-galeria-imagens'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_images', methods=['GET'])
def get_images():
    # Obter a lista de objetos do S3
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix='uploads/')
    
    # Extraindo as chaves das imagens
    image_keys = [content['Key'] for content in response.get('Contents', [])]

    # Gerando URLs assinadas para as imagens
    image_urls = []
    for key in image_keys:
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': key},
            ExpiresIn=3600  # URL válida por 1 hora
        )
        image_urls.append(url)

    return jsonify(image_urls)  # Retorna a lista de URLs das imagens

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
