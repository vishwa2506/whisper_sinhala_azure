#!/usr/bin/env python3
import whisper, glob, os, argparse

def main():
    parser = argparse.ArgumentParser(description="Batch transcribe Sinhala audio files")
    parser.add_argument("files", nargs="+", help="audio files or glob patterns")
    parser.add_argument("-m", "--model", default="medium", choices=["base","small","medium","large"], help="Whisper model")
    args = parser.parse_args()

    model = whisper.load_model(args.model)
    for pattern in args.files:
        for file in glob.glob(pattern):
            print(f"\n🎙️ Transcribing {file} ...")
            res = model.transcribe(file, language="si")
            print(res["text"])
            txt = os.path.splitext(file)[0] + ".txt"
            open(txt, "w", encoding="utf-8").write(res["text"])
            print(f"✅ Saved to {txt}")

if __name__ == "__main__":
    main()
