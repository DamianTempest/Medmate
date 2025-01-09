from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import requests


class SymptomCheckerApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input prompt
        self.label = Label(
            text="Enter your symptoms (e.g., fever, headache, fatigue):",
            size_hint_y=None,
            height=30,
        )

        # Text input box
        self.input_box = TextInput(
            hint_text="Type your symptoms here...",
            multiline=True,
            size_hint_y=0.4,
        )

        # Submit button
        self.submit_button = Button(
            text="Analyze Symptoms", size_hint_y=None, height=50
        )
        self.submit_button.bind(on_press=self.check_symptoms)

        # Result area (scrollable)
        self.result_area = ScrollView(size_hint=(1, 0.5))
        self.result_label = Label(
            text="", size_hint_y=None, height=200, text_size=(400, None)
        )
        self.result_area.add_widget(self.result_label)

        # Add widgets to layout
        layout.add_widget(self.label)
        layout.add_widget(self.input_box)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.result_area)

        return layout

    def check_symptoms(self, instance):
        """Handles submission of symptoms and displays analysis."""
        symptoms = self.input_box.text.strip()

        if not symptoms:
            self.result_label.text = "Please enter your symptoms."
            return

        try:
            # Replace with your Flask server endpoint
            response = requests.post(
                "http://127.0.0.1:5000/check",
                json={"symptoms": symptoms},
                timeout=10,
            )

            if response.status_code == 200:
                result = response.json()
                self.result_label.text = result.get("analysis", "No analysis found.")
            else:
                self.result_label.text = "Error: Could not connect to server."
        except Exception as e:
            self.result_label.text = f"Error: {e}"


if __name__ == "__main__":
    SymptomCheckerApp().run()
