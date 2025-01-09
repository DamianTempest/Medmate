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
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime


# Screen Classes
class PageScreen(Screen):
    pass

class NghtScreen(Screen):
    pass

class LoginScreen(Screen):
    def validate_login(self):
        # Example logic for login validation
        email = self.ids.email.text
        password = self.ids.password.text

        if not email or not password:
            print("Email and password cannot be empty.")
        elif "@" not in email:
            print("Invalid email address.")
        else:
            print("Login successful.")
            self.manager.current = "home"

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
            chat_messages.text += f"\nYou: {message}"
            chat_input.text = ""

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
        sm.add_widget(NghtScreen(name="nun"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(PatientProfileScreen(name="patientprofile"))
        sm.add_widget(EditPatientScreen(name="editpatient"))        
        sm.add_widget(ContactListScreen(name="contact_list"))
        sm.add_widget(ConversationScreen(name="conversation"))
        sm.add_widget(ChatScreen(name="chat"))  # Add the ChatScreen here
        sm.add_widget(Chat2Screen(name="chat2"))
        sm.add_widget(Chat3Screen(name="chat3"))
        return sm



# Run the App
if __name__ == "__main__":
    MedMateApp().run()
