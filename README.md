# whisper_sinhala_azure

Instructions to create Azure VM with GPU

SSH login

Clone repo + run setup:

bash
Copy
Edit
git clone REPO_URL
cd whisper_sinhala_azure
bash install.sh
Transcribe samples:

bash
Copy
Edit
chmod +x transcribe.py
./transcribe.py example.wav "*.wav"
Outputs .txt files for each audio.
