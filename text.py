from cgitb import text
from hashlib import sha256

text_string  = "Admin123"

output = sha256(text_string.encode()).hexdigest()

print(output)