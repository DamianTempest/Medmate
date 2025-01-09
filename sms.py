from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import requests


class HealthTipsApp(App):
    def build(self):
        # Main Layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # User data input
        self.user_data_label = Label(
            text="Enter your details (age, medical history, etc.):",
            size_hint_y=None,
            height=30,
        )
        self.user_data_input = TextInput(
            hint_text="e.g., Age: 25, Diabetes: No, Hypertension: Yes",
            multiline=True,
            size_hint_y=0.3,
        )

        # Submit Button
        self.submit_button = Button(
            text="Get Health Tips & Alerts",
            size_hint_y=None,
            height=50,
        )
        self.submit_button.bind(on_press=self.get_health_tips)

        # Result area (scrollable)
        self.result_area = ScrollView(size_hint=(1, 0.5))
        self.result_label = Label(
            text="Your health tips and alerts will appear here.",
            size_hint_y=None,
            height=200,
            text_size=(400, None),
        )
        self.result_area.add_widget(self.result_label)

        # Add widgets to layout
        layout.add_widget(self.user_data_label)
        layout.add_widget(self.user_data_input)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.result_area)

        return layout

    def get_health_tips(self, instance):
        """Fetch personalized health tips and alerts."""
        user_data = self.user_data_input.text.strip()

        if not user_data:
            self.result_label.text = "Please enter your details."
            return

        try:
            # Replace with your Flask server endpoint
            response = requests.post(
                "http://127.0.0.1:5000/health_tips",
                json={"user_data": user_data},
                timeout=10,
            )

            if response.status_code == 200:
                result = response.json()
                self.result_label.text = result.get(
                    "tips", "No health tips found. Try again later."
                )
            else:
                self.result_label.text = "Error: Could not connect to the server."
        except Exception as e:
            self.result_label.text = f"Error: {e}"


if __name__ == "__main__":
    HealthTipsApp().run()
