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
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import random
import requests


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
    pass

class ExtraScreen(Screen):   
    pass

class ContactUsScreen(Screen):
    pass

class PatientProfileScreen(Screen):
    pass

class EditPatientScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Save_Changes(self, instance):
        # Get values from the input fields
        name = self.ids.name_input.text
        age = self.ids.age_input.text
        country = self.ids.country_input.text
        medical_history = self.ids.medical_history_input.text
        current_medications = self.ids.current_medications_input.text
        current_activities = self.ids.current_activities_input.text

        # Example: Print the values (replace with actual save logic)
        print(f"Name: {name}, Age: {age}, Country: {country}")
        print(f"Medical History: {medical_history}")
        print(f"Current Medications: {current_medications}")
        print(f"Current Activities: {current_activities}")

        # Add your save logic here (e.g., update a database or file)
        # Feedback to the user could also be added
        
        # Show success popup after saving
        popup = Popup(
            title='Success',
            content=Label(text='Profile saved successfully!'),
            size_hint=(None, None),
            size=(300, 150)
        )
        popup.open()

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
        name = self.ids.name_input.text.strip() or "User"
        preference = self.ids.preference_spinner.text.lower()
        allergies = self.ids.allergies_input.text.lower().split(",") if self.ids.allergies_input.text else []
        goal = self.ids.goal_spinner.text.lower()  # This can be used for further customization later.

        # Meal Database
        meal_database = {
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
            suggested_meals = [
                meal for meal in suggested_meals
                if allergen not in [ingredient for ingredients in meal.values() for ingredient in ingredients]
            ]

        # Select a Meal
        if suggested_meals:
            meal_choice = random.choice(suggested_meals)
            meal_name = list(meal_choice.keys())[0]
            meal_ingredients = ", ".join(list(meal_choice.values())[0])
            meal_suggestion = f"{meal_name}\nIngredients: {meal_ingredients}"
        else:
            meal_suggestion = "Sorry, no suitable meal found based on your preferences."

        # Display the Meal Suggestion in a Popup
        popup_content = Label(text=f"Hi {name}, based on your input:\n\n{meal_suggestion}")
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
        sm.add_widget(ExtraScreen(name="Extra"))
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
        
        return sm



# Run the App
if __name__ == "__main__":
    MedMateApp().run()
