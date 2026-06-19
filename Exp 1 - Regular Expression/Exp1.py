import re

text = "Contact us at admin@example.com or call 9876543210. Apple and Android are popular."

email = re.search(r'\S+@\S+\.\S+', text)
if email:
    print("Email Found:", email.group())

phone = re.search(r'\d{10}', text)
if phone:
    print("Phone Number Found:", phone.group())

words = re.findall(r'\bA\w*', text)
print("Words Starting with A:", words)

if re.match(r'Contact', text):
    print("Text Starts with Contact")
else:
    print("Text Does Not Start with Contact")
