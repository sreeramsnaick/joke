import google.generativeai as genai
genai.configure(api_key="AIzaSyCi4AHxrgG_nSq6vH4qsWzr-2GKXDdIb9A")
model = genai.GenerativeModel("models/gemini-1.5-flash")
prompt = input("Enter a topic or prompt for a joke: ")
try:
    response = model.generate_content(prompt)
    print("\nHere's your joke:")
    print(response.text)

except Exception as e:
    print("⚠️ Error:", e)

