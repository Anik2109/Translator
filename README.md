Speech Recognition and Translation Script
This Python script captures audio from your microphone, recognizes speech using Google Speech Recognition, translates the recognized text from English to Hindi using Google Translate, and converts the translated text to speech. The translated speech is then played back to the user.

Features
Audio Recording: Captures audio from the microphone.
Speech Recognition: Converts spoken language into text.
Text Translation: Translates recognized text from English to Hindi.
Text-to-Speech: Converts the translated text into audio.
Cross-Platform Audio Playback: Plays the translated audio on Windows, macOS, and Linux.
Requirements
Ensure you have Python 3.6+ installed. You also need to install the following Python libraries:

SpeechRecognition for speech-to-text recognition.
googletrans==4.0.0-rc1 for text translation.
gTTS for text-to-speech conversion.
pyaudio for audio capturing.
numpy for handling audio data.
Installation
Clone the repository and navigate into the directory:

bash
Copy code
git clone https://github.com/Anik2109/Translator.git
cd speech-recognition-translation
Install the required libraries using pip:

bash
Copy code
pip install --upgrade googletrans==4.0.0-rc1 gtts pyaudio numpy
Usage
Ensure your microphone and speakers are working properly.

Run the script:

bash
Copy code
python script_name.py
Replace script_name.py with the name of your script file (e.g., speech_recognition_translation.py).

Speak into the microphone when prompted. The script will record your speech for 5 seconds, recognize the speech, translate it to Hindi, and play the translated audio.


Troubleshooting
Common Issues
NameError: name 'webbrowser' is not defined

Solution: Ensure you have import webbrowser at the beginning of your script.

AttributeError: 'NoneType' object has no attribute 'group'

Solution: Ensure you have the correct version of googletrans installed. Upgrade to 4.0.0-rc1 using pip install --upgrade googletrans==4.0.0-rc1.

pyaudio Installation Issues

Solution: pyaudio can sometimes be tricky to install. On Windows, you can use precompiled binaries from here.

General Issues
No sound during playback: Ensure that your speakers or headphones are working properly.
Cannot access microphone: Check your microphone permissions and settings.
Contributing
Feel free to contribute to the project by submitting issues, bug fixes, or feature requests. Fork the repository, make your changes, and submit a pull request!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Google Speech Recognition API: For converting speech to text.
Google Translate API: For translating text between languages.
gTTS: For text-to-speech conversion.
PyAudio: For audio capture.
Contact
For any questions or feedback, please open an issue or contact anik.kaushesh@gmail.com.
