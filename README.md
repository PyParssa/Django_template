# Django VPS-Ready Docker Template 🚀

A streamlined, production-ready template for deploying Django applications to any VPS (DigitalOcean, Linode, AWS EC2, etc.) using Docker and Gunicorn. 

This template removes the friction of initial DevOps setup, letting you go from repository to live server in minutes.

## ✨ Features

* **Django 5.x** – Clean, modern project structure.
* **Dockerized** – Fully containerized application using lightweight Python Alpine/Slim images.
* **Gunicorn** – Production-grade WSGI HTTP server configured and ready.
* **Environment Variables** – Ready-to-go `.env` configuration for security.
* **Static Files Handling** – Pre-configured with WhiteNoise for efficient static file serving in production.

---

## 🚀 Quick Start

### 1. Local Development
Clone the repo and spin up the containers:
```bash
git clone <your-repo-url>
cd <your-repo-name>
docker-compose up --build
