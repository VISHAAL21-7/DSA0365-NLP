from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = input("Enter a prompt: ")

result = generator(prompt, max_length=50)

print("\nGenerated Text:")
print(result[0]["generated_text"])
