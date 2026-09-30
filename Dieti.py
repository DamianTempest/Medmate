from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random

class DieticianApp(BoxLayout):
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


class DieticianAppMain(App):
    def build(self):
        return DieticianApp()


if __name__ == "__main__":
    DieticianAppMain().run()
