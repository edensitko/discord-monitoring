#!/bin/bash

echo "🔧 מתקין את כל הדרוש ומפעיל את השירותים..."

sudo apt update && sudo apt install -y docker.io docker-compose git

sudo usermod -aG docker $USER

echo "🐳 בונה ומפעיל את הקונטיינרים עם docker-compose..."
sudo docker-compose up -d --build

echo "✅ סיום ההתקנה. תוכל לבדוק את Prometheus בדפדפן בכתובת http://<your-server-ip>:9090"
