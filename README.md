# jervise_voice
# Jarvis Voice Assistant (Python)

A **Jarvis-style voice assistant** built in Python that works **offline** using **Vosk** for speech recognition and **pyttsx3** for text-to-speech. The assistant responds to a wake word **"Jarvis"** and executes commands like opening websites, telling time, or exiting.

---

## **Features**

- **Wake Word Detection:** Activate assistant by saying `"Jarvis"`
- **Voice Commands:**
  - Tell current time
  - Open websites (e.g., YouTube, Google)
  - Exit assistant
- **Offline Functionality:** No internet required for voice recognition
- **Cross-Platform:** Works on Windows, Linux, and MacOS
- **Text-to-Speech:** Uses system voice for responses

---

## **Tech Stack**

- Python 3.x
- [Vosk](https://alphacephei.com/vosk/) (Offline Speech Recognition)
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) (Text-to-Speech)
- [sounddevice](https://python-sounddevice.readthedocs.io/) (Audio input/output)

---

## **Demo Video**

Insert a short demo video here showing:

- Wake word `"Jarvis"`
- Sample commands: `"Time"`, `"Open YouTube"`, `"Exit"`

---

## **Installation**

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/jarvis-voice-assistant.git
cd jarvis-voice-assistant
