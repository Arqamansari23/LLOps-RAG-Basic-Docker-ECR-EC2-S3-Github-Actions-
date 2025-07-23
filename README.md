
---

# 🔥 LLOps RAG Basic Project with Docker, ECR, EC2, S3 & GitHub Actions

This project demonstrates an end-to-end **RAG (Retrieval-Augmented Generation)** pipeline deployed using **Docker, AWS ECR, EC2, S3**, and automated using **GitHub Actions** for CI/CD. It includes complete environment management, vectorstore, basic query answering, and cloud deployment using best DevOps practices.

---



## 🚀 Features

- Upload PDFs and perform question answering
- Uses **FAISS** for fast vector similarity search
- Embeds with OpenAI/Gemini/any LLM provider
- Stores PDFs and models in **AWS S3**
- Fully Dockerized for reproducible builds
- CI/CD enabled with **GitHub Actions** and **ECR + EC2**
- Clean modular structure (LLM services, vector DB, storage services)

## 📁 Folder Structure


```bash
requirements.txt
app/
├── __init__.py
├── config.py                  # Loads .env variables (API keys, AWS, etc.)
├── main.py                    # Flask app entrypoint
│
├── models/                    # Vector store handling (FAISS/Chroma)
│   ├── __init__.py
│   └── vector_store.py        # Embedding + Retrieval logic
│
├── services/
│   ├── __init__.py
│   ├── llm_service.py         # Call to OpenAI/Gemini LLM
│   └── storage_service.py     # Handles AWS S3 upload/download
│
├── static/
│   └── style.css              # UI styling
│
└── templates/
    └── index.html             # Web interface (PDF upload + Q&A)



```

## 🛠️ How to Run Locally?

### Step 1: Setup Environment Using `uv` (Optional)

```bash
uv init 
uv venv 
```

Activate the environment:

```bash
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/macOS
```

### Step 2: Install Dependencies

```bash
uv pip install -r requirements.txt
```

### Step 3: Run the App

```bash
python app/main.py
```

Visit the app at:

```bash
http://localhost:8000
```

---

## 🐳 Docker & AWS Deployment

### 1. 🔑 Create IAM User in AWS Console

Assign the following **policies** to the IAM user:

* `AmazonEC2FullAccess`
* `AmazonEC2ContainerRegistryFullAccess`

This user will be used to push Docker images to AWS ECR and deploy them on EC2.

---

### 2. 🐋 Create AWS ECR Repository

Create a new ECR repository to host the Docker image.

Example URI:

```
315865595366.dkr.ecr.us-east-1.amazonaws.com/rag
```

---

### 3. 💻 Launch EC2 (Ubuntu) & Install Docker

SSH into your EC2 instance, then install Docker:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Grant Docker access
sudo usermod -aG docker ubuntu
newgrp docker
```

---

### 4. 🏃 Setup EC2 as Self-Hosted GitHub Runner

Go to:

```
GitHub Repo > Settings > Actions > Runners > New self-hosted runner
```

* Choose OS: Linux
* Follow and run the commands given by GitHub on your EC2 instance.

---

### 5. 🔐 Setup GitHub Secrets

Add the following secrets to your repository:

| Secret Name             | Description                                         |
| ----------------------- | --------------------------------------------------- |
| `AWS_ACCESS_KEY_ID`     | IAM user access key                                 |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key                                 |
| `AWS_DEFAULT_REGION`            | e.g. `us-east-1`                                    |
| `ECR_REPO`     | e.g. `315865595366.dkr.ecr.us-east-1.amazonaws.com` |
| `ECR_REPO`   | e.g. `rag`                                          |

---

## 🚀 GitHub Actions Deployment Flow

The `.github/workflows/deploy.yml` does the following automatically when you push to main:

1. **Builds Docker Image** from the source code.
2. **Pushes Docker Image** to AWS ECR.
3. **Triggers Self-Hosted EC2 Runner**.
4. **Pulls Docker Image** from ECR in EC2.
5. **Runs the App in EC2** using Docker.

---

## 📦 .gitignore

```gitignore
# Python-generated files
__pycache__/
*.py[oc]
build/
dist/
wheels/
*.egg-info

# Virtual environments
.venv/

# Environment variable files
.env
.env.*
```

---

## ✨ Tech Stack

* **FastAPI** for backend
* **Docker** for containerization
* **AWS EC2 + ECR** for cloud deployment
* **GitHub Actions** for CI/CD
* **LangChain + FAISS** for RAG implementation

---
