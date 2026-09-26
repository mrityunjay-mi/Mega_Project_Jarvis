# Mega_Project_Jarvis
# Jarvis - Voice Activated Virtual Assistant 🤖

Jarvis is a Python-based voice assistant built using the `speech_recognition` library. It listens for a specific wake word ("Jarvis"), acknowledges the user, and executes pre-defined web commands like opening websites or playing specific music from a custom library.

Inspired by the "Code With Harry" tutorial series.

## 🚀 Features
- **Wake Word Detection:** Listens continuously for the word "Jarvis" before accepting commands.
- **Text-to-Speech:** Responds with voice confirmations using `pyttsx3`.
- **Web Automation:** Opens Google, YouTube, and Manga platforms instantly via voice.
- **Custom Music Library:** Plays specific songs mapped in a local `musicLibrary` module.

## 🛠️ Tech Stack & Prerequisites
- **Language:** Python 3.x
- **Libraries Used:**
  - `speech_recognition` (For capturing and converting audio)
  - `pyttsx3` (For offline text-to-speech synthesis)
  - `pocketsphinx` (Optional, for offline recognition support)
  - `webbrowser` (Built-in Python module for web navigation)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **Set up a Virtual Environment (Recommended):**
   ```bash
   # Create venv
   python -m venv venv
   
   # Activate venv (Windows)
   .\venv\Scripts\activate
   
   # Activate venv (Mac/Linux)
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install speechrecognition pyttsx3 pocketsphinx
   ```
   *Note: If you are on Linux, you may also need to install `pyaudio` system dependencies (e.g., `sudo apt-get install python3-pyaudio`).*

## 🎮 How to Use

1. Ensure your microphone is plugged in and working.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Wait for the terminal to print `Listening....`.
4. Say **"Jarvis"**. The assistant will reply with *"Yes master"*.
5. Speak one of the supported commands:
   - *"Open Google"*
   - *"Open Youtube"*
   - *"Play [song_name]"* (Ensure the song exists in your `musicLibrary.py`)

## 📂 Project Structure
```text
├── main.py            # Main application logic and voice loop
├── musicLibrary.py     # Dictionary mapping song names to URLs
├── requirements.txt   # List of project dependencies
└── README.md          # Project documentation
```

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
