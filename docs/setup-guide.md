# Setup Guide

Follow these steps to set up the project locally.

---

## Prerequisites
- Python >= 3.8
- Node.js >= 16
- Docker (optional, for containerization)
- PostgreSQL database

---

## Installation

### Clone the repository
```bash
git clone https://github.com/USERNAME/REPOSITORY.git
cd REPOSITORY
```

### Install dependencies
1. Python
```bash
pip install -r requirements.txt
```
2. Javascript
```bash
npm install
```

---

## Running locally
1. Configure the enviorment variables in `.env`
2. Start the application:
```bash
python src/main.py
```
3. Open `http://localhost:8000`

---

## Using Docker
1. Build and start the container:
```bash
docker-compose up --build
```
2. Access the app at `http://localhost:8000`
