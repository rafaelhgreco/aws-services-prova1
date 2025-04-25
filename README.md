
# Aplicativo para Armazenamento de Boletos no S3 com Deploy no ECS

Este projeto consiste em um aplicativo Flask empacotado com Docker, com objetivo de facilitar o armazenamento de boletos bancários em um bucket Amazon S3, promovendo organização, rastreabilidade e segurança para o setor financeiro da empresa.


## Solução
Foi desenvolvido um aplicativo web simples, acessível via navegador, que permite upload de boletos PDF diretamente para um bucket S3. 

![Vídeo demonstrativo da solução](https://www.youtube.com/watch?v=7zwC2uqqL0I)

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
![Diagrama da Arquitetura](https://i.imgur.com/LNKs2QT.png)
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

## Justificativa dos Serviços AWS Utilizados
### ☁️ Amazon S3 (Simple Storage Service)
O Amazon S3 foi escolhido para armazenar os boletos gerados pela aplicação devido à sua **alta durabilidade, escalabilidade automática** e **baixo custo por GB armazenado**. Ele é ideal para armazenar arquivos estáticos como PDFs, imagens e documentos, com acesso fácil via API. Além disso:
- Custo extremamente acessível, sendo possível armazenar centenas de arquivos pagando apenas alguns centavos por mês.

### 🐳 Amazon ECS (Fargate)
O Amazon ECS com a tecnologia Fargate foi escolhido para executar os containers Docker da aplicação, eliminando a necessidade de gerenciar servidores.
- **Integração nativa com ECR e CloudWatch**, facilitando deploy e monitoramento.

### 📦 Amazon ECR (Elastic Container Registry)
O Amazon ECR é o repositório privado de imagens Docker da AWS. Ele foi utilizado para:
- Armazenar com segurança as imagens da aplicação;
- Garantir **integração direta com ECS**, facilitando o deploy;
- Eliminar a dependência de registries públicos como Docker Hub.

### 🛠️ AWS Cloud9
O Cloud9 foi utilizado como ambiente de desenvolvimento diretamente na nuvem, com as seguintes vantagens:
- **Pré-configurado com ferramentas AWS e Docker**, economizando tempo de setup;
- Permite codificação, build e testes sem depender de uma máquina local;
- Ideal para projetos colaborativos e desenvolvimento remoto.

### 💻 AWS CLI
A AWS CLI (Command Line Interface) foi utilizada para automatizar comandos no ECR, ECS e S3. Isso possibilita:
- Deploys e atualizações com scripts;
- Integração em pipelines CI/CD;
- Agilidade na configuração de infraestrutura com comandos simples.
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
    - Clique em Preview → Preview Running Application.

flask-s3-app/
├── main.py                   # Lógica principal da aplicação
├── templates/
│   └── index.html            # Template da página
│
├── requirements.txt          # Lista de dependências do projeto
├── Dockerfile                # Dockerfile para empacotar a aplicação
Git
├── README.md                 # Documentação do projeto
```
## Pipeline CI/CD (GitHub Actions)
Arquivo: .github/workflows/deploy.yml


## Considerações Finais
Esta aplicação atende plenamente a demanda de organização e rastreabilidade de boletos de forma simples e escalável. Além disso, oferece um ótimo exemplo de aplicação real integrando serviços AWS modernos com boas práticas de DevOps.
#### Desenvolvimento por Rafael Henrique e Mateus Stringuetti
