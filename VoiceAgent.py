import pyttsx3
import speech_recognition as sr
import openai

# Set OpenAI API Key (replace with your key)
openai.api_key = "your_openai_api_key"

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Captures voice input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            speak("The speech recognition service is unavailable.")
            return None
        except sr.WaitTimeoutError:
            speak("You didn't say anything.")
            return None

def chat_with_gpt(prompt):
    """Generates a response using OpenAI's GPT."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """Main loop for JARVIS."""
    speak("Hello, I am JARVIS. How can I assist you today?")
    while True:
        user_command = listen()
        if user_command:
            if "exit" in user_command.lower() or "quit" in user_command.lower():
                speak("Goodbye! Have a great day!")
                break
            else:
                response = chat_with_gpt(user_command)
                print(f"JARVIS: {response}")
                speak(response)

if __name__ == "__main__":
    main()
