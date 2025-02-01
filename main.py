from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.spinner import Spinner
from kivy.utils import get_color_from_hex
from kivy.uix.recycleview import RecycleView
from kivy.uix.progressbar import ProgressBar
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import random
import requests
from dotenv import load_dotenv
from kivy.utils import get_color_from_hex, platform
from screens.dietician_screen import DieticianScreen
from screens.profile_screen import ProfileScreen
from screens.chat_screen import ChatScreen
from ai_response import send_chat_message
from kivy.uix.label import Label
from screens.profile_screen import ProfileScreen
from kivy.clock import Clock
from kivy.uix.image import Image
from screens.chat_screen import ChatScreen
import re





class ai_chatapp(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        
        # App logo/icon
        logo = Image(
            source="Mage.jpg",  # Replace with your logo path
            size_hint=(None, None),
            size=(100, 100),
            pos_hint={"center_x": 0.5}
        )
        
        # Welcome label
        welcome = Label(
            text="Healthcare Assistant",
            font_size="32sp",
            size_hint_y=0.2,
            color=get_color_from_hex("#2196F3"),
            bold=True
        )
        
        # Buttons layout
        buttons_layout = BoxLayout(orientation="vertical", spacing=25, size_hint_y=0.5)
        
        profile_btn = Button(
            text="My Profile",
            size_hint_y=None,
            height="70dp",
            background_color=get_color_from_hex("#2196F3"),
            background_normal="",
            font_size="18sp",
            bold=True
        )
        profile_btn.bind(on_press=lambda x: self.switch_screen("profile"))
        
        chat_btn = Button(
            text="AI Health Assistant",
            size_hint_y=None,
            height="70dp",
            background_color=get_color_from_hex("#4CAF50"),
            background_normal="",
            font_size="18sp",
            bold=True
        )
        chat_btn.bind(on_press=lambda x: self.switch_screen("chat"))
        
        dietician_btn = Button(
            text="Dietician",
            size_hint_y=None,
            height="70dp",
            background_color=get_color_from_hex("#FFC107"),
            background_normal="",
            font_size="18sp",
            bold=True
        )
        dietician_btn.bind(on_press=lambda x: self.switch_screen("dietician"))

        # Back Button
        back_btn = Button(
            text="Back to Home",
            size_hint_y=None,
            height="70dp",
            background_color=get_color_from_hex("#FF5722"),  # Orange-red color
            background_normal="",
            font_size="18sp",
            bold=True
        )
        back_btn.bind(on_press=lambda x: self.switch_screen("Extra"))  # Ensure 'ai_chatapp' is your home screen

        # Add widgets
        layout.add_widget(logo)
        layout.add_widget(welcome)
        layout.add_widget(buttons_layout)
        buttons_layout.add_widget(profile_btn)
        buttons_layout.add_widget(chat_btn)
        buttons_layout.add_widget(dietician_btn)
        buttons_layout.add_widget(back_btn)  # Add back button to layout
        
        self.add_widget(layout)

    def switch_screen(self, screen_name):
        """Helper function to switch between screens"""
        self.manager.current = screen_name



class HealthTips:
    def __init__(self):
        self.tips = [
            "Drink enough water every day!",
            "Exercise for at least 30 minutes daily.",
            "Eat a balanced diet with plenty of fruits and vegetables.",
            "Get 7-8 hours of sleep every night.",
            "Wash your hands regularly to avoid germs.",
            "Take breaks to reduce stress throughout the day.",
            "Don't skip breakfast! Start your day with healthy food.",
            "Avoid smoking and excessive alcohol consumption.",
            "Practice good posture to avoid back pain.",
            "Get regular checkups to monitor your health."
        ]
    
    def get_random_tip(self):
        return random.choice(self.tips)


# Define the TipScreen class to display tips
class TipScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.health_tips = HealthTips()

# Screen Classes
class PageScreen(Screen):
    def show_health_tip(self):
        tip = HealthTips().get_random_tip()
        popup = Popup(
            title='Health Tip',
            content=Label(text=tip),
            size_hint=(None, None),
            size=(300, 150)
        )
        popup.open()

# LoginScreen
class LoginScreen(Screen):
    def validate_login(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()

        if not email or not password:
            self.ids.error_label.text = "All fields are required!"
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
        self.manager.current = "nxt"  # Navigate to LoginScreen

class NghtScreen(Screen):
    pass

class CommunityScreen(Screen):
    pass

class NxtScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.preference_spinner_values = [
            "Ghana", "Nigeria", "Kenya", "South Africa", "Egypt", 
            "France", "Germany", "Italy", "Spain", "United Kingdom", 
            "China", "India", "Japan", "South Korea", "Indonesia", 
            "USA", "Canada", "Mexico", "Brazil", "Argentina", 
            "Colombia", "Australia", "New Zealand"
        ]

    def on_enter(self):
        # Set the spinner values when the screen is entered
        self.ids.preference_spinner.values = self.preference_spinner_values
    def validate_Nxt(self):
        # Check if IDs exist before accessing them
        if not hasattr(self.ids, "name_input") or \
           not hasattr(self.ids, "age_input") or \
           not hasattr(self.ids, "error_label") or \
           not hasattr(self.ids, "preference_spinner"):
            print("Error: One or more widget IDs are missing in the .kv file.")
            return
        
        # Get user input and strip spaces
        name = self.ids.name_input.text.strip()
        age = self.ids.age_input.text.strip()
        

        # Check if any fields are empty
        if not name or not age :
            self.ids.error_label.text = "All fields are required!"
            return
        
        # Set spinner values for country selection
        self.ids.preference_spinner.values = [
            "Ghana", "Nigeria", "Kenya", "South Africa", "Egypt", 
            "France", "Germany", "Italy", "Spain", "United Kingdom",
            "China", "India", "Japan", "South Korea", "Indonesia",
            "USA", "Canada", "Mexico", "Brazil", "Argentina", 
            "Colombia", "Australia", "New Zealand"
        ]
        
        # Bind spinner selection to the country_input text field
        self.ids.preference_spinner.bind(text=self.update_spinner_text)
        
        # After validation, show a success message
        self.ids.error_label.text = "Sign up successful!"
        
        # Ensure screen manager exists before switching screens
        if self.manager:
            self.manager.current = "home"
        else:
            print("Error: Screen manager is not set.")
    
    def update_spinner_text(self, spinner, text):
        # Update the country input field when the spinner is selected
        self.ids.country_input.text = text

'''class NxtScreen(Screen):
   def validate_Nxt(self):
        # Check if IDs exist before accessing them
        if not hasattr(self.ids, "name_input") or \
           not hasattr(self.ids, "age_input") or \
           not hasattr(self.ids, "country_input") or \
           not hasattr(self.ids, "error_label"):
            print("Error: One or more widget IDs are missing in the .kv file.")
            return
        
        # Get user input and strip spaces
        name = self.ids.name_input.text.strip()
        age = self.ids.age_input.text.strip()
        self.country_input = self.ids.country_input
        self.preference_spinner = self.ids.preference_spinner

        # Set the spinner values
        self.preference_spinner.values = ["Ghana", "Nigeria", "Kenya", "South Africa", "Egypt", 
                                          "France", "Germany", "Italy", "Spain", "United Kingdom",
                                          "China", "India", "Japan", "South Korea", "Indonesia",
                                          "USA", "Canada", "Mexico", "Brazil", "Argentina", 
                                          "Colombia", "Australia", "New Zealand"]

        # Bind the text of the spinner to the country_input's text
        self.country_input.bind(text=self.update_spinner_text)

            # Validate input
        if not name or not age:
            self.ids.error_label.text = "All fields are required!"
            return
        
        self.ids.error_label.text = "Sign up successful!"
        
        # Ensure screen manager exists before switching screens
        if self.manager:
            self.manager.current = "home"
        else:
            print("Error: Screen manager is not set.")'''
            


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
    # Create properties to hold patient data
    patient_name = StringProperty("Unknown")
    patient_age = StringProperty("Unknown")
    patient_condition = StringProperty("Unknown")

    def update_profile(self, name, age, condition):
        # Update the screen's properties
        self.patient_name = name
        self.patient_age = age
        self.patient_condition = condition

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

        profile_screen = self.manager.get_screen('patientprofile')
        profile_screen.update_profile(name, age, country)

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
    def validate_logindoc(self):
        email = self.ids.email.text.strip()
        password = self.ids.password.text.strip()
        license = self.ids.license.text.strip()  # Assuming there's a 'license' input field

        if not email or not password or not license:
            self.ids.error_label.text = "All fields are required!"
            return

        if "@" not in email:
            self.ids.error_label.text = "Invalid email format!"
            return

        # Add validation for the doctor's license (assuming it has a specific format, e.g., alphanumeric)
        license_pattern = r'^[A-Za-z]{3}/[A-Za-z]{2}/\d{4}$'  # Pattern for the license format
        if not re.match(license_pattern, license):
            self.ids.error_label.text = "Invalid license format!"
            return

        self.ids.error_label.text = "Login successful!"
        self.manager.current = "nun"  # Navigate to HomeScreen


class Dietician2Screen(Screen):
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

class AboutScreen(Screen):
    pass


class SymptomCheckerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def Analyze_Symptoms(self, instance):
        # Access the input field correctly
        symptoms = self.ids.symptom_input.text.strip() 
        
        result_label = self.ids.get('result_label')
        if result_label:
            result_label.text = "🔍 Analyzing your symptoms..."
        else:
            print("Error: 'result_label' not found in self.ids")
 

        if not symptoms:
            self.ids.result_label.text = "⚠ Please enter your symptoms."
            return

        # Reset progress bar and show analyzing message
        self.ids.progress_bar.value = 10
        self.ids.result_label.text = "🔍 Analyzing your symptoms..."

        # Schedule progressive updates for a smooth UI experience
        Clock.schedule_once(lambda dt: self.update_progress(30), 0.5)
        Clock.schedule_once(lambda dt: self.update_progress(60), 1.0)

        # Send request in a separate thread to prevent UI freeze
        Clock.schedule_once(lambda dt: self.send_request(symptoms), 1.5)

    def update_progress(self, value):
        """Updates the progress bar"""
        self.ids.progress_bar.value = value

    def send_request(self, symptoms):
        """Handles API request and updates UI"""
        try:
            response = requests.post(
                "http://127.0.0.1:5000/check", 
                json={"symptoms": symptoms}, 
                timeout=10
            )

            if response.status_code == 200:
                data = response.json()
                analysis = data.get("analysis", "No analysis available.")
                self.ids.result_label.text = f"🩺 {analysis}"
                self.update_progress(100)
            else:
                self.ids.result_label.text = "⚠ Error: Server unavailable."
                self.update_progress(0)
        
        except requests.exceptions.Timeout:
            self.ids.result_label.text = "⏳ Server took too long to respond. Try again."
            self.update_progress(0)

        except requests.exceptions.RequestException as e:
            self.ids.result_label.text = f"❌ Connection Error: {e}"
            self.update_progress(0)

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

class Chat1Screen(Screen):
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

class HealthTips:
    def __init__(self):
        self.tips = [
            "Drink enough water every day!",
            "Exercise for at least 30 minutes daily.",
            "Eat a balanced diet with plenty of fruits and vegetables.",
            "Get 7-8 hours of sleep every night.",
            "Wash your hands regularly to avoid germs.",
            "Take breaks to reduce stress throughout the day.",
            "Don't skip breakfast! Start your day with healthy food.",
            "Avoid smoking and excessive alcohol consumption.",
            "Practice good posture to avoid back pain.",
            "Get regular checkups to monitor your health.",
            "Aim for at least 30 minutes of exercise each day.",
            "Get enough sleep to rejuvenate your body.",
            "Eat a balanced diet with lots of fruits and vegetables.",
            "Take breaks and move around to avoid sitting too long.",
            "Practice good posture to avoid back and neck strain.",
            "Take time to relax and manage stress effectively.",
            "Keep your mind sharp with regular mental exercises.",
            "Wash your hands regularly to prevent infections.",
            "Limit screen time to reduce eye strain.",
            "Spend time in nature for mental and physical well-being.",
            "Eat smaller, more frequent meals to maintain energy levels.",
            "Don’t skip breakfast, it’s an important meal for energy.",
            "Avoid excessive sugar to maintain healthy blood sugar levels.",
            "Limit processed foods and focus on whole grains.",
            "Stretch daily to maintain flexibility.",
            "Find an activity you love for regular physical activity.",
            "Practice mindfulness or meditation for mental health.",
            "Listen to your body and rest when needed.",
            "Practice good hygiene habits to avoid illnesses.",
            "Incorporate healthy fats like avocados and nuts into your diet.",
            "Limit alcohol intake for better liver health.",
            "Keep a positive mindset to reduce stress levels.",
            "Avoid smoking to protect your lungs and heart.",
            "Have regular health check-ups with your doctor.",
            "Wear sunscreen to protect your skin from UV damage.",
            "Get fresh air regularly to boost mood and energy.",
            "Try a new physical activity to challenge your body.",
            "Take a walk after meals for better digestion.",
            "Use proper ergonomics at your desk to prevent strain.",
            "Stay consistent with your sleep schedule for better rest.",
            "Eat foods rich in fiber for healthy digestion.",
            "Laugh often; it’s good for your mental and physical health.",
            "Set aside time for self-care and relaxation.",
            "Hydrate with herbal teas for additional health benefits.",
            "Avoid excessive caffeine to prevent energy crashes.",
            "Engage in social activities for improved mental health.",
            "Prioritize mental health just as much as physical health.",
            "Practice deep breathing exercises to reduce stress.",
            "Limit junk food intake to maintain a healthy weight.",
            "Ensure proper hydration, especially after exercise.",
            "Use a foam roller to relieve muscle tightness.",
            "Eat foods rich in antioxidants to support your immune system.",
            "Stay connected with loved ones for emotional well-being.",
            "Switch to healthier cooking methods like baking or grilling.",
            "Manage your time effectively to reduce stress.",
            "Get adequate vitamin D from sunlight or supplements.",
            "Try yoga or Pilates for flexibility and strength.",
            "Avoid eating too late in the evening to improve digestion.",
            "Incorporate probiotics into your diet for gut health.",
            "Maintain a healthy weight through balanced nutrition and exercise.",
            "Practice gratitude daily to boost your mood.",
            "Avoid excessive screen time before bed for better sleep.",
            "Take your vitamins regularly for nutritional support.",
            "Get creative with your workouts to keep them fun.",
            "Track your health habits to stay motivated.",
            "Slow down and savor your meals to prevent overeating.",
            "Avoid self-diagnosing; seek professional medical advice.",
            "Ensure your workspace is well-lit to reduce eye strain.",
            "Be mindful of your posture while sitting or standing.",
            "Engage in regular cardio exercises for heart health.",
            "Be kind to yourself; mental health matters.",
            "Learn something new to keep your mind engaged.",
            "Consume healthy snacks like fruits, nuts, or yogurt.",
            "Try to avoid processed sugars and opt for natural sweeteners.",
            "Boost immunity with vitamin-rich foods like citrus fruits.",
            "Limit screen time to improve focus and sleep.",
            "Practice mindfulness while eating to prevent overeating.",
            "Incorporate strength training into your fitness routine.",
            "Check in with your emotions regularly to maintain mental health.",
            "Switch to plant-based meals a few times a week for health benefits.",
            "Stay active throughout the day, even with small movements.",
            "Avoid unhealthy dieting trends and focus on balance.",
            "Find a fitness routine that works for your lifestyle.",
            "Include a variety of colors in your diet for a wider range of nutrients.",
            "Be mindful of portion sizes to avoid overeating.",
            "Spend time doing activities that bring you joy.",
            "Regularly engage in stretching or mobility exercises.",
            "Practice self-compassion and take care of your emotional needs.",
            "Stay hydrated with water and herbal teas, not sugary drinks.",
            "Take time for hobbies or creative outlets for mental wellness.",
            "Make sleep a priority for better physical and mental health.",
            "Stay mindful of your breathing to reduce anxiety.",
            "Incorporate more plant-based meals for overall wellness.",
            "Celebrate your progress and achievements, no matter how small.",
            "Stay motivated by setting small, achievable health goals.",
            "Don’t forget to laugh; it’s great for reducing stress.",
            "Create a positive and inspiring environment at home.",
            "Challenge yourself to try something new each week."

        ]
    
    def get_random_tip(self):
        return random.choice(self.tips)


# Define the TipScreen class to display tips
class TipScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.health_tips = HealthTips()  # Initialize the HealthTips class
        self.label = Label(text=self.health_tips.get_random_tip(), size_hint_y=None, height=44)
        self.add_widget(self.label)

        # Add button to get a new tip
        button = Button(text="Get New Tip", on_press=self.update_tip)
        self.add_widget(button)

    def update_tip(self, instance):
        # Update the label with a new random health tip
        self.label.text = self.health_tips.get_random_tip()











class MedMateApp(App):
    def build(self):
        if platform != 'android':
            Window.size = (400, 600)
        def get_color(self, hex_color):
            return get_color_from_hex(hex_color)
        

        sm = ScreenManager()
        sm.add_widget(PageScreen(name="page"))
        sm.add_widget(TipScreen(name="tip"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignUpScreen(name="signup"))
        sm.add_widget(NxtScreen(name="nxt"))
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
        sm.add_widget(Chat1Screen(name="chat.02"))  # Add the ChatScreen here
        sm.add_widget(Chat2Screen(name="chat2"))
        sm.add_widget(Chat3Screen(name="chat3"))
        sm.add_widget(PatientsScreen(name="Patients"))
        sm.add_widget(PatientschatScreen(name="chat.1"))
        sm.add_widget(SymptomCheckerScreen(name="Sym"))
        sm.add_widget(SignUpDocScreen(name="signup.doc"))
        sm.add_widget(AboutScreen(name="About"))
        sm.add_widget(LoginDocScreen(name="login.doc"))
        sm.add_widget(Dietician2Screen(name="Dietician"))
        sm.add_widget(ProfileScreen(name='profile'))
        sm.add_widget(ChatScreen(name='chat'))
        sm.add_widget(DieticianScreen(name='dietician'))
        sm.add_widget(ai_chatapp(name='ai_chatapp'))
        sm.add_widget(SignUpDocScreen(name="signup.doc"))
        sm.add_widget(LoginDocScreen(name="login.doc"))
        
        

        
        Clock.schedule_once(self.show_tip_popup, 0.5)
        return sm

    def show_tip_popup(self, *args):
        # Show the popup with a health tip
        health_tips = HealthTips()
        tip = health_tips.get_random_tip()
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=tip, size_hint_y=None, height=44))
        close_button = Button(text="Thanks", size_hint_y=None, height=44)
        close_button.bind(on_press=self.close_popup)
        content.add_widget(close_button)

        self.popup = Popup(title="Health Tip", content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    def close_popup(self, instance):
        # Close the popup
        self.popup.dismiss()

    def update_health_tip(self):
        # Method to update the health tip
        print("Health Tip updated!")
        # You can add logic to change or refresh the tip if desired
        



# Run the App
if __name__ == "__main__":
    MedMateApp().run()
