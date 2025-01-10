from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
import requests

# Screen Classes
class PageScreen(Screen):
    pass

class LoginScreen(Screen):
    def validate_login(self):
        email = self.ids.email.text
        password = self.ids.password.text

    def on_focus_email(self, widget):
        # Clear error message when the user focuses on the email field
        self.root.ids.error_label.text = ""

    def on_focus_password(self, widget):
        # Clear error message when the user focuses on the password field
        self.root.ids.error_label.text = ""

    def login(self, email, password):
        # Basic input validation
        if not email or not password:
            self.root.ids.error_label.text = "Both fields are required!"
            return

        # API call for login
        try:
            response = requests.post("http://your-api-url.com/login", json={"email": email, "password": password})

            if response.status_code == 200:
                # Handle successful login (you can navigate to home screen here)
                self.root.ids.error_label.text = "Login successful!"
                self.root.current = "home"
            else:
                self.root.ids.error_label.text = "Invalid username or password."

        except requests.exceptions.RequestException as e:
            # Handle network issues
            self.root.ids.error_label.text = f"Network error: {str(e)}"
                

class SignUpScreen(Screen):
    def create_account(self):
        email = self.ids.email.text
        password = self.ids.password.text

        if not email and not password:
            print("All fields are required!")
        elif "@" not in email:
            print("Enter a valid email address!")
        else:
            print("Account created successfully!")
            self.manager.current = "login"

class NghtScreen(Screen):
    pass

class CommunityScreen(Screen):
    pass

class ResearchScreen(Screen):
    pass

class NewsScreen(Screen):
    pass

class PatientScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class ContactUsScreen(Screen):
    pass

class PatientProfileScreen(Screen):
    pass

class EditPatientScreen(Screen):
    pass

class ContactListScreen(Screen):
    pass

class PatientsScreen(Screen):
    pass

class PatientschatScreen(Screen):
    pass

class SymptomCheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def Analyze_Symptoms(self, instance):
        # Ensure we access the correct input field
        symptoms = self.symptom_input.text.strip()  # Accessing symptom_input here
        if not symptoms:
            self.result_label.text = "Please enter your symptoms."
            return
        
        # Update progress bar and show loading
        self.progress_bar.value = 20
        self.result_label.text = "Analyzing your symptoms..."
        
        try:
            # Replace with your actual server endpoint
            response = requests.post(
                "http://127.0.0.1:5000/check", json={"symptoms": symptoms}, timeout=10
            )

            # Update progress bar
            self.progress_bar.value = 60

            if response.status_code == 200:
                result = response.json()
                self.result_label.text = result.get("analysis", "No analysis found.")
            else:
                self.result_label.text = "Error: Could not connect to server."
                self.progress_bar.value = 0
        except requests.exceptions.RequestException as e:
            self.result_label.text = f"Error: {e}"
            self.progress_bar.value = 0

class ConversationScreen(Screen):
    def suggest_medicine(self, query):
        print(f"Received query: {query}")
    MEDICINE_SUGGESTIONS = {
        "cold": "Paracetamol, Cough Syrup",
        "fever": "Ibuprofen, Acetaminophen",
        "headache": "Aspirin, Naproxen",
        "stomach ache": "Antacid, Buscopan",
    }

    def suggest_medicine(self, disease_name):
        disease_name = disease_name.lower()
        return self.MEDICINE_SUGGESTIONS.get(disease_name, "Consult a healthcare professional.")

class chatapp1Screen(Screen):
    pass

class ChatScreen(Screen):
    def send_message(self):
        timestamp = datetime.now().strftime("%H:%M")
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            # Append the message with timestamp
            chat_messages.text += f"\nYou ({timestamp}): {message}"
            chat_input.text = ""

            # Scroll to the latest message
            chat_messages.parent.scroll_y = 0

class Chat2Screen(Screen):
    def send_message(self):
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""

class Chat3Screen(Screen):
    def send_message(self):
        chat_input = self.ids.chat_input
        chat_messages = self.ids.chat_messages

        message = chat_input.text
        if message.strip():
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""





class MedMateApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PageScreen(name="page"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(NghtScreen(name="nun"))
        sm.add_widget(CommunityScreen(name="Com"))
        sm.add_widget(ResearchScreen(name="Res"))
        sm.add_widget(NewsScreen(name="news"))
        sm.add_widget(PatientScreen(name="pat"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(PatientProfileScreen(name="patientprofile"))
        sm.add_widget(EditPatientScreen(name="editpatient"))        
        sm.add_widget(ContactListScreen(name="contact_list"))
        sm.add_widget(ConversationScreen(name="conversation"))
        sm.add_widget(ChatScreen(name="chat"))  # Add the ChatScreen here
        sm.add_widget(Chat2Screen(name="chat2"))
        sm.add_widget(Chat3Screen(name="chat3"))
        sm.add_widget(PatientsScreen(name="Patients"))
        sm.add_widget(PatientschatScreen(name="chat.1"))
        sm.add_widget(SymptomCheckerScreen(name="Sym"))
        return sm



# Run the App
if __name__ == "__main__":
    MedMateApp().run()
