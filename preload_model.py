from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Specify the model name (GPT-2 base model)
model_name = "gpt2"

# Load the model and tokenizer from Hugging Face
print("Downloading and loading the GPT-2 model...")
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Save the model locally
save_path = "./models/health_gpt2"
print(f"Saving model to {save_path}...")
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)

print("Model saved successfully!")
