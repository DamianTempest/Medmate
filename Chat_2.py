import os
import tkinter as tk
from tkinter import scrolledtext
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the local GPT-2 model and tokenizer
MODEL_PATH = "./models/health_gpt2"  # Ensure the model is saved in this directory
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Preload and save the model first.")

# Load GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)

# Function to generate responses
def chatbot_response(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
        top_p=0.9,
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response[len(prompt):].strip()

# GUI Application
class HealthBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthBot")

        # Chat history display
        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50)
        self.chat_history.pack(pady=10)
        self.chat_history.insert(tk.END, "HealthBot: Hi! How can I assist you today with health-related queries?\n")
        self.chat_history.config(state=tk.DISABLED)

        # User input field and send button
        input_frame = tk.Frame(root)
        input_frame.pack(pady=5)
        self.user_input = tk.Entry(input_frame, width=40)
        self.user_input.pack(side=tk.LEFT, padx=5)
        send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT)

    def send_message(self):
        # Get user input
        user_message = self.user_input.get().strip()
        if not user_message:
            return
        self.display_message(f"You: {user_message}", is_user=True)
        self.user_input.delete(0, tk.END)

        # Generate bot response
        bot_prompt = f"HealthBot: {user_message}\nAI:"
        bot_response = chatbot_response(bot_prompt)
        self.display_message(f"HealthBot: {bot_response}", is_user=False)

    def display_message(self, message, is_user):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{message}\n")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.yview(tk.END)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HealthBotApp(root)
    root.mainloop()
