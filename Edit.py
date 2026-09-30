from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex, platform
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.spinner import Spinner
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.spinner import Spinner
from AI_ChatBox import HealthcareApp
from kivy.uix.popup import Popup
import random
import requests


class HealthcareApp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "HealthcareApp"
        self.greetings = []

    def fetch_greeting(self):
        # Example using random and requests
        random_greeting = random.choice([
            "Hello! How can I help?",
            "Good day! What do you need?",
            "Hi! Let’s make today better!"
        ])
        self.greetings.append(random_greeting)
        return random_greeting

    def get_health_data(self):
        # Example API call using `requests`
        try:
            response = requests.get("https://api.example.com/healthdata")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Unable to fetch health data"}
        except Exception as e:
            return {"error": str(e)}


# Screen Classes
class PageScreen(Screen):
    pass

# LoginScreen
class LoginScreen(Screen):
    def validate_login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not email or not password:
            self.ids.error_label.text = "Both fields are required!"
            return

        if "@" not in email:
            self.ids.error_label.text = "Invalid email format!"
            return

        self.ids.error_label.text = "Login successful!"
        self.manager.current = "home"  # Navigate to HomeScreen


# SignUpScreen
class SignUpScreen(Screen):
    def validate_signup(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not email or not password:
            self.ids.error_label.text = "All fields are required!"
            return

        if "@" not in email:
            self.ids.error_label.text = "Invalid email format!"
            return

        if len(password) < 6:
            self.ids.error_label.text = "Password too short!"
            return

        self.ids.error_label.text = "Sign up successful!"
        self.manager.current = "home"  # Navigate to LoginScreen

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
 '''   def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Layout for the HomeScreen
        layout = BoxLayout(orientation='vertical', spacing=20, padding=20)'''

        # Extra button to open the popup
 '''       extra_button = Button(
            text="Show Extra Options",
            size_hint=(None, None),
            size=("200dp", "50dp"),
            background_color=get_color_from_hex('#2196F3'),
            bold=True
        )
        extra_button.bind(on_press=self.show_extra_popup)
        layout.add_widget(extra_button)

        self.add_widget(layout)'''

def show_extra_popup(self, instance):
        # Open the ExtraScreen popup
        popup = ExtraPopup()
        popup.open()



class ExtraPopup(Popup):

        pass

class HealthcareScreen(Screen):
    pass

class ContactUsScreen(Screen):
    pass

class PatientProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.patient_list = ["Mr. Smith", "Mrs. Jane", "Mr. Joe"]  # Dynamic data source
        self.populate_patient_list()

    def populate_patient_list(self):
        rv = self.ids.patient_list_rv
        rv.data = [{"text": name} for name in self.patient_list]
    pass

class EditPatientScreen(Screen):
    pass


class AI_ChatBoxScreen(Screen):
    pass

class ContactListScreen(Screen):
    pass

class PatientsScreen(Screen):
    pass

class PatientschatScreen(Screen):
    pass

class SignUpDocScreen(Screen):
    pass

class LoginDocScreen(Screen):
    pass

class DieticianScreen(Screen):
    def generate_suggestion(self):
        # Get user input from the GUI
        name = self.ids.name_input.text.strip()
        preference = self.ids.preference_spinner.text.lower()
        allergies = self.ids.allergies_input.text.lower().split(",") if self.ids.allergies_input.text else []
        goal = self.ids.goal_spinner.text.lower()

        # Meal Database
        meal_database ={
    "vegetarian": [
        {"Eba and Egusi Soup": ["cassava", "egusi", "spinach", "tomatoes", "palm oil"]},
        {"Jollof Rice with Plantains": ["rice", "tomato", "onion", "bell pepper", "plantains"]},
        {"Gari Fortor": ["gari", "vegetables", "tomato paste", "onion", "palm oil"]},
        {"Kontomire Stew": ["cocoyam leaves", "tomato", "onions", "palm oil", "saltfish"]},
        {"Chibom": ["gari", "tomato paste", "peanut butter", "onion", "avocado"]},
        {"Fried Plantains with Beans": ["plantains", "beans", "tomatoes", "onions", "spices"]}
    ],
    "vegan": [
        {"Red Red": ["beans", "palm oil", "plantains", "tomato", "onions"]},
        {"Kelewele": ["ripe plantains", "ginger", "garlic", "chili pepper", "palm oil"]},
        {"Peanut Soup": ["peanut butter", "tomato", "onion", "spinach", "yams"]},
        {"Aboboi": ["corn", "beans", "cabbage", "tomatoes", "onions"]},
        {"Palm Nut Soup": ["palm nuts", "onion", "tomato", "spinach", "yams"]},
        {"Fried Yam with Pepper Sauce": ["yam", "tomato", "onion", "chilies", "oil"]}
    ],
    "keto": [
        {"Grilled Tilapia with Fufu": ["tilapia", "fufu", "palm oil", "spices"]},
        {"Omo Tuo (Rice Balls) with Groundnut Soup": ["rice balls", "groundnut", "chicken", "tomatoes", "onions"]},
        {"Pork with Garden Eggs": ["pork", "garden eggs", "tomatoes", "onions", "green pepper"]},
        {"Keto Vegetable Soup": ["spinach", "tomato", "onion", "coconut oil", "fish"]},
        {"Grilled Chicken with Avocado": ["chicken", "avocado", "tomatoes", "onions", "palm oil"]},
        {"Grilled Snails with Garden Eggs": ["snails", "garden eggs", "onions", "tomatoes", "pepper"]}
    ],
    "paleo": [
        {"Fried Fish with Cocoyam": ["fish", "cocoyam", "palm oil", "garlic", "onion"]},
        {"Porridge with Millet": ["millet", "groundnut paste", "ginger", "sugar"]},
        {"Bitterleaf Soup with Goat Meat": ["goat meat", "bitterleaf", "tomato", "onion", "palm oil"]},
        {"Coconut Rice with Grilled Chicken": ["coconut", "rice", "chicken", "tomato", "onions"]},
        {"Tuo Zaafi with Groundnut Soup": ["millet", "groundnut", "meat", "tomatoes", "palm oil"]},
        {"Boiled Plantain with Fish Stew": ["plantain", "fish", "tomato", "onion", "spices"]}
    ],
    "omnivorous": [
        {"Banku and Okra Soup": ["banku", "okra", "fish", "goat meat", "palm oil"]},
        {"Grilled Chicken with Jollof Rice": ["chicken", "rice", "tomato paste", "onion", "plantain"]},
        {"Beef Kebabs with Fried Yam": ["beef", "onion", "bell pepper", "yam", "spices"]},
        {"Fried Rice with Chicken": ["rice", "chicken", "carrots", "peas", "onions"]},
        {"Baked Chicken with Plantain": ["chicken", "plantain", "tomato", "onions", "palm oil"]},
        {"Pork with Rice Balls": ["pork", "rice balls", "tomatoes", "onions", "green pepper"]}
    ]
}

        # Filter Meals
        suggested_meals = meal_database.get(preference, meal_database["omnivorous"])
        for allergen in allergies:
            suggested_meals = [meal for meal in suggested_meals if allergen not in meal.lower()]

        # Select a Meal
        if suggested_meals:
            meal_suggestion = random.choice(suggested_meals)
        else:
            meal_suggestion = "Sorry, no suitable meal found based on your preferences."

        # Display the Meal Suggestion in a Popup
        popup_content = Label(text=f"Hi {name}, based on your input:\n{meal_suggestion}")
        suggestion_popup = Popup(
            title="Your Meal Suggestion",
            content=popup_content,
            size_hint=(0.8, 0.4),
        )
        suggestion_popup.open()




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
        if platform != 'android':
            Window.size = (400, 600)
        
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
        sm.add_widget(SignUpDocScreen(name="signup.doc"))
        sm.add_widget(LoginDocScreen(name="login.doc"))
        sm.add_widget(DieticianScreen(name="Dietician"))
        sm.add_widget(HealthcareScreen(name="AI"))

        try:
            sm.add_widget(HealthcareScreen(name="ai"))
        except Exception as e:
            print(f"Error adding HealthcareScreen: {e}")
        return sm



# Run the App
if __name__ == "__main__":
    MedMateApp().run()


'''Button:
                background_color: 1, 1, 1, 0.5
                text: "Editpatient"
                color:0, 0, 1
                size_hint: .5,None
                pos_hint:{"center_x":.4}
                on_press: app.root.current = "editpatient"
            Button:
                background_color: 1, 1, 1, 0.5
                text: "Sympt0ms Checker"
                color:0, 0, 1
                size_hint: .5,None
                pos_hint:{"center_x":.4}
                on_press: app.root.current = "Sym"'''