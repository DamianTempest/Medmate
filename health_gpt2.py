from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

model.save_pretrained("./models/health_gpt2")
tokenizer.save_pretrained("./models/health_gpt2")
