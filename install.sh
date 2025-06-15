#!/bin/bash
set -e

echo "🧠 Updating system..."
sudo apt update
sudo apt install -y git ffmpeg python3 python3-pip

echo "📦 Installing Whisper..."
pip3 install --upgrade pip
pip3 install openai-whisper

echo "✅ Whisper install ready!"
