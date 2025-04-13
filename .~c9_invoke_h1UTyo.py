from flask import Flask, render_template
import boto3

app = Flask(__name__)

BUCKET_NAME = 'meu-site-galeria-imagens'
PASTA = 'uploads/'

s3 = boto3.client('s3')

@app.route('/')
def index():
    imagens = []

    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=PASTA)
    for obj in response.get('Contents', []):
        key = obj['Key']
        if key.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            url = f"https://meu-site-galeria-imagens.s3.amazonaws.com/{key}"
            imagens.append(url)

    return render_template('index.html', imagens=imagens)

if __name__ == '__main__':
    # Definindo host como 0.0.0.0 para permitir acesso externo (Cloud9)
    app.run(debug=True, host='0.0.0.0', port=8080)
