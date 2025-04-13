# Imagem base do Python
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir flask boto3

# Expor a porta que o Flask vai usar
EXPOSE 8080

# Comando para rodar a aplicação
CMD ["python", "app.py"]
