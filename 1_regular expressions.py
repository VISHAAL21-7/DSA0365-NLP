import re

text = "My email is test@example.com and phone is 9876543210"

# Match email pattern
email_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
emails = re.findall(email_pattern, text)

# Search phone number
phone_pattern = r'\b\d{10}\b'
phone = re.search(phone_pattern, text)

print("Emails found:", emails)
print("Phone found:", phone.group() if phone else "Not found")