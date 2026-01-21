# Real-time-AI-based-Sign-to-Speech-Speech-to-ASL-Sign-Animation-Conversion

This project is a dual-module accessibility system that bridges communication between hearing-impaired individuals (who use Indian Sign Language, ISL) and non-sign-language users. It provides two complementary interfaces in a unified Tkinter GUI: one converts hand gestures (sign language) to spoken words, and the other converts spoken or typed words to animated sign language. Such systems are designed to “bridge the communication gap for individuals who use sign language”. In our case, the Sign-to-Speech module recognizes ISL gestures in real-time (via webcam) and vocalizes them, while the Speech-to-Sign module accepts speech/text input and displays corresponding 3D sign animations. This makes everyday interactions smoother between deaf and hearing communities, leveraging AI and computer vision to interpret and generate sign language.

Key Features

Real-time ISL Recognition: Uses Google’s MediaPipe Hands for hand-tracking (detecting 21 keypoints per hand) and a custom TensorFlow.js model to classify gestures. Recognized signs (letters/words) are displayed as text and spoken aloud.
<img width="1866" height="868" alt="Screenshot 2026-01-21 121400" src="https://github.com/user-attachments/assets/3a183e0f-46c3-411f-8fd4-659c6a49b35d" />


Speech-to-Animation: Listens to live speech (via the microphone or text input) and converts it into Indian Sign Language animations. The app uses speech recognition (Web Speech API) to get text, then maps words/phrases to pre-made 3D sign animations.
<img width="1920" height="1080" alt="Screenshot 2026-01-21 121809" src="https://github.com/user-attachments/assets/6f104332-f6ff-4faa-8663-f0b91501d1de" />



Cross-Platform GUI: A Python Tkinter interface manages both modules, launching a browser-based sign-detector or a Django-based sign-animation viewer. It supports Windows 10/11 and requires Python 3.10 (32/64 bit) to ensure compatibility with all libraries.

<img width="1621" height="972" alt="Screenshot 2026-01-21 121641" src="https://github.com/user-attachments/assets/bb0fbb55-6e49-4e68-a1e4-aed2f8ecfec0" />


Web-Based ML Inference: The Sign-to-Speech module runs entirely in the browser using TensorFlow.js and MediaPipe, so no server is needed. Once loaded, the ML model executes client-side for fast, on-device gesture recognition.

Custom Animation Assets: The Speech-to-Sign module uses a Blender-created 3D avatar (from the A2SL dataset) to render smooth sign animations. This provides clear, human-like gestures to represent spoken words.

<img width="1712" height="860" alt="image" src="https://github.com/user-attachments/assets/c11f7af2-0ef1-41f8-b96b-e72d895c9dd0" />


System Requirements

Operating System: Windows 10 or 11 (64-bit)

Python: 3.10.x (we recommend creating a virtual environment to match this version)

Browser: Google Chrome (for best MediaPipe and WebGL support)

Hardware: A working webcam for sign capture, and a microphone for speech input.

Internet: Initial download of TensorFlow.js and MediaPipe files, but the app runs offline afterward.

Ensure you have Chrome installed (MediaPipe and TF.js perform best with modern browsers) and that Python 3.10 is used (other versions may cause compatibility issues).

Project Structure

The repository is organized as follows:

MAJOR_PROJECT/
├── sign_to_speech/               # Web interface for sign-to-speech module
│   ├── index.html                # HTML/JS page with webcam-based sign detection
│   └── my_model/
│       ├── metadata.json         # Model metadata for TensorFlow.js
│       ├── model.json            # TF.js model architecture (gesture classifier)
│       └── weights.bin           # Trained model weights (for ISL gestures)
├── speech_to_sign/               # Django-based server for speech-to-sign
│   ├── speech_to_sign_app.py     # Django server entrypoint (manages web app)
│   ├── requirements.txt          # Python dependencies for this module
│   ├── db.sqlite3                # Django database (stores any needed data)
│   ├── templates/                # HTML templates for web pages (e.g., animation display)
│   ├── static/                   # Static assets (CSS, JS, images)
│   └── A2SL/                     # Folder of sign animation assets (3D models, clips)
│       └── * (3D animations and related files)
├── main_gui.py                   # Unified Tkinter GUI launcher
├── feedback.txt                  # Log file for user feedback
├── requirements.txt              # Core dependencies (for the GUI and overall project)
└── README.md                     # This file


This layout clearly separates the two main modules. The sign_to_speech folder contains everything needed for in-browser sign detection (using TensorFlow.js), while speech_to_sign holds the Django app (with an embedded Blender-rendered animation library).

Quick Start

Follow these steps to set up and run the system:

Clone the Repository
Download or clone MAJOR_PROJECT/ onto your Windows machine.

Setup Python Environment
Open a Command Prompt in the project root (MAJOR_PROJECT/) and run:

python -m venv 3.10venv
3.10venv\Scripts\activate


This creates and activates a Python 3.10 virtual environment (required for compatibility).

Install Dependencies
With the venv activated, install the necessary packages:

pip install -r requirements.txt


This installs both Tkinter (GUI) dependencies and any core libraries needed by the modules.

Launch the GUI
Still in the activated environment, start the main interface:

python main_gui.py


A window will appear with buttons for Sign to Speech and Speech to Sign. When you select a module, the system will automatically open your browser:

Sign to Speech: Opens a Chrome tab running sign_to_speech/index.html. It will ask for webcam access. Once granted, the live video feed will be processed for ISL gestures.

Speech to Sign: Starts the Django development server (if not already running) and opens a browser to http://127.0.0.1:8000/. You can then speak or enter text to see the corresponding sign animation.

Use the System

For Sign-to-Speech, perform sign gestures in front of your webcam. The app will display recognized letters/words in text and speak them out loud using the browser’s speech synthesizer (Web Speech API SpeechSynthesis).

For Speech-to-Sign, press the microphone button or type a message. The app will recognize your speech (or read your text), map words to sign animations, and play the 3D sign language sequence.

If everything is set up correctly, the two modules work seamlessly together to translate between spoken language and ISL (with animations).

It also includes the feedback option.
<img width="1606" height="958" alt="Screenshot 2026-01-21 122002" src="https://github.com/user-attachments/assets/d4765c52-3fd9-484c-a384-512bf582f7c2" />


Troubleshooting

Django Server Issues: If the Speech-to-Sign server fails to start via the GUI, try running it manually:

Open a new Command Prompt.

Navigate into speech_to_sign/ and activate a venv there (if separate).

Install its requirements (pip install -r requirements.txt and pip install django if needed).

Run python speech_to_sign_app.py runserver (or python manage.py runserver).

In your browser, go to http://127.0.0.1:8000/.

You should see the speech-to-sign web interface. Return to the main GUI and retry launching the module.

Webcam/Microphone: Ensure your devices are not being used by other applications. The browser might ask for permissions – grant them. In Chrome’s address bar, click the camera/microphone icon to check permissions.

Performance: Close other GPU-intensive applications for smooth MediaPipe performance. Chrome should be up-to-date. If recognition is slow, make sure the video feed is well-lit and your hands are fully visible.

Python Version: Only use Python 3.10. The ML model files and Django code have been tested specifically on 3.10.x. Using a different version may cause errors. Always activate the 3.10venv before running any scripts.

Recreating Environments: If reinstalling dependencies, close all terminals first to avoid conflicts. Then delete and recreate the 3.10venv as shown above.

Module Details
Sign Language → Speech

This browser-based module uses MediaPipe Hands and TensorFlow.js for real-time gesture recognition. Each webcam frame is processed by MediaPipe to detect hand landmarks (21 points per hand). These coordinates are fed into a custom neural network (trained on Indian sign gestures) that runs in the browser via TensorFlow.js. The model classifies the hand pose into a specific ISL letter or word. The recognized text is then both displayed on-screen and converted to audio using the browser’s Text-to-Speech engine (Web Speech API’s SpeechSynthesis).

 <img width="1920" height="1080" alt="Screenshot 2026-01-21 120950" src="https://github.com/user-attachments/assets/1faeff80-00f4-4b85-a00b-0a77875f298b" />
Model Training & Browser Integration

The Sign Language to Speech module uses a custom-trained machine learning model, developed and trained by our team specifically for Indian Sign Language (ISL) recognition.

Model Training

The model was trained offline using Python on a curated dataset of ISL hand gestures.

Hand landmarks were extracted using MediaPipe Hands (21 key points per hand).

These landmarks were used as features to train a gesture classification model.

The training process focused on:

Accurate detection of ISL alphabets and basic words

Real-time performance

Robustness to hand movement and lighting variations

Model Conversion for Web Deployment

After successful training and validation, the trained model was converted for browser compatibility.

The Python-trained model was exported and converted into TensorFlow.js format using the TensorFlow.js converter.

This conversion generates the following files:

model.json – Model architecture

weights.bin – Trained weights

metadata.json – Label and class information

my_model/
├── model.json
├── weights.bin
└── metadata.json

Browser-Based Inference

The converted .json model is loaded directly in the browser using TensorFlow.js.

This allows:

Client-side inference (no backend/server required)

Faster real-time predictions

Improved privacy (no video data is sent to a server)

In summary, the flow is: Webcam → MediaPipe Hands (21 landmarks) → TF.js Classifier → Text → TTS. This runs entirely client-side (no server needed) for low latency. The use of MediaPipe/TF.js enables “real-time performance” even on standard hardware.



Speech → Sign Animation

The Django-powered module handles the reverse translation. It accepts either live microphone input or typed text. Speech input is captured and converted to text using the Web Speech API’s SpeechRecognition interface. The resulting text is then preprocessed (e.g. tokenized) and mapped to corresponding sign gestures. We have a custom mapping from words/phrases to 3D animations (sourced from the A2SL dataset). These animations are rendered in the browser: the HTML/JS front-end requests the appropriate animation file from the server and plays it in sequence.

 <img width="1920" height="1080" alt="Screenshot 2026-01-21 121900" src="https://github.com/user-attachments/assets/2b9e5c74-ad1a-41a8-a213-07f5f514ed4a" />


Notably, the animations are 3D models of a signing avatar created with Blender. For example, one animation might show the avatar signing the ISL gesture for “hello”. The Django backend (speech_to_sign_app.py) manages routing and serves the static animation files located in speech_to_sign/A2SL/. Once the user speaks or enters text, the app looks up each word’s animation clip and displays it. The entire sign sequence is played back-to-back for fluent communication.

Acknowledgements

This project builds on inspiring prior work. We thank Tanmay Jivnani, whose open-source sign-to-speech implementation demonstrates converting ASL to text/speech to bridge communication. We also acknowledge Jigar Gajjar for his Django-based “Audio Speech to Sign Language Converter,” a system that converts spoken English into Indian Sign Language animations. Both of these projects informed our design: Tanmay’s focus on real-time gesture ML and Jigar’s use of 3D animations (Blender) have been particularly helpful. Links to their work are provided below:

Tanmay Jivnani – GitHub • Project Repo (Sign-to-Speech)

https://github.com/tanmayJivnani
https://www.linkedin.com/in/tanmay-jivnani/


Jigar Gajjar – GitHub • Audio-Speech-to-Sign Converter

https://github.com/jigargajjar55
https://github.com/jigargajjar55/Audio-Speech-To-Sign-Language-Converter
Thankyou so much 

Their work exemplifies the cutting-edge of sign language translation technology. We also thank the authors of MediaPipe and TensorFlow.js for enabling on-device machine learning.


Team & Guides

Team Members: Surabhi Kulkarni, Shreya Kallapur, Shrivatsa Deshpande, Sidharth Dindarakopp

Project Guide: Prof. Suraj Kadli

This project was developed in the Electronics & Communication Engineering department, specializing in AI and Computer Vision, as an academic major project.

Important Notes

Python Version: Use Python 3.10 only. The ML model and Django app are tested for 3.10.x.

Virtual Environment: Always activate the 3.10venv before running the GUI or modules to ensure correct dependencies.

Browser: Use Google Chrome for best results (MediaPipe and TF.js use WebGL features that Chrome supports well).

Devices: Ensure your webcam and mic are functional and allowed by the system and browser.

Recreating Setup: If modifying dependencies or encountering errors, close all terminals first, then delete and recreate the virtual environments to start fresh.

License

This software is provided for academic and educational purposes only. It is not licensed for commercial use. The code and model weights (inside sign_to_speech/my_model/) are free to use and modify for research or learning. No warranty is provided – this is experimental code developed by students for a major project.

Sources
