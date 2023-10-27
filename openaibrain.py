import openai

# Set your OpenAI API key
api_key = 'api key'  # Replace with your actual API key

# Initialize the OpenAI client
openai.api_key = api_key

def chat_with_ai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose the GPT-3 engine you prefer
        prompt=prompt,  # Pass the prompt as a string, not a dictionary
        max_tokens=50,  # You can adjust the response length as needed
        temperature=0.7,  # Adjust the temperature for creativity
    )
    return response.choices[0].text.strip()

