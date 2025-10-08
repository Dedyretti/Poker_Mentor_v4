#!/bin/bash
echo "Python version:"
python3 --version
echo "Pip version:"
pip --version
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Starting bot..."
python3 bot/webhook_server.py