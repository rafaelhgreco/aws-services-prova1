
# Portfólio Técnico: Aplicativo para Armazenamento de Boletos no S3 com Deploy no ECS

Este projeto consiste em um aplicativo Flask empacotado com Docker, com objetivo de facilitar o armazenamento de boletos bancários em um bucket Amazon S3, promovendo organização, rastreabilidade e segurança para o setor financeiro da empresa.


## Solução
Foi desenvolvido um aplicativo web simples, acessível via navegador, que permite upload de boletos PDF diretamente para um bucket S3. 

![Vídeo demonstrativo da solução](https://www.youtube.com/)

Essa solução é:

🔐 Segura (acesso via IAM Role);

📂 Organizada (nome de arquivos com timestamp e identificador);

☁️ Escalável (deploy via ECS e Docker).

## Tecnologias Utilizadas
| Tecnologia       | Função                                             |
|------------------|----------------------------------------------------|
| Flask            | Backend da aplicação em Python                     |
| Docker           | Containerização da aplicação                       |
| AWS S3           | Armazenamento dos boletos                          |
| AWS ECS (Fargate)| Execução escalável e gerenciada da aplicação       |
| AWS ECR          | Registro de imagens Docker                         |
| AWS Cloud9       | Ambiente de desenvolvimento na nuvem              |
| AWS CLI          | Interface de linha de comando para AWS             |
| GitHub Actions   | CI/CD automatizado                                 |

## Fluxo de Desenvolvimento
![Diagrama da Arquitetura](https://i.imgur.com/3mG39hE.png)
### Desenvolvimento com Cloud9
- Cloud9 é utilizado para codificar, buildar e testar a aplicação localmente.

### Containerização com Docker
- A aplicação é empacotada com um Dockerfile.

### Upload da Imagem para o ECR
- Após o build, a imagem é enviada para o Amazon ECR.

### Deploy via Amazon ECS
- Um cluster ECS com Fargate executa a imagem e expõe a porta 8080 para acesso externo.

### Integração com GitHub Actions
- A cada push na branch master, a pipeline:

- Constrói a imagem Docker;

- Faz push para o ECR;

- Força nova implantação no ECS.

##  Boas Práticas Adotadas
- Uso de IAM Role na Task Definition (sem expor credenciais);

- Isolamento da aplicação em containers Docker;

- Deploy em ECS com Fargate (zero manutenção de infraestrutura);

- Uso de variáveis de ambiente e Secrets do GitHub para segurança;

- CI/CD com GitHub Actions para automação de build e deploy;

- Bucket com políticas de versionamento e criptografia ativadas.

## Comandos para Clonar e Rodar no AWS Cloud9

### ▶️ Clonando o repositório:

```bash
git clone https://github.com/rafaelhgreco/aws-services-prova1.git
cd flask-s3-app

---

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py

---

docker build -t flask-s3-app .
docker run -p 8080:8080 -v ~/.aws:/root/.aws flask-s3-app

---

Se estiver desenvolvendo ou testando a aplicação diretamente no AWS Cloud9.
    Clique em Preview → Preview Running Application.
```
## Pipeline CI/CD (GitHub Actions)
Arquivo: .github/workflows/deploy.yml

## Considerações Finais
Esta aplicação atende plenamente a demanda de organização e rastreabilidade de boletos de forma simples e escalável. Além disso, oferece um ótimo exemplo de aplicação real integrando serviços AWS modernos com boas práticas de DevOps.
