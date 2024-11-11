import ollama

link = "badCode.py"
with open(link,'rb') as file:
    content = file.read()

prompts = f'Review this code, alert any security vulnerabilities first such as sql injection and risks of attacks, provide suggestions for improvement, coding best practices, improve readability, and maintainability. Provide code examples for your suggestion. Respond in markdown format. If the file does not have any code or does not need any changes, say "No changes needed" {content}'

response = ollama.generate(model='codellama:7b',prompt=prompts)
aResponse = response['response']

file_path = 'responses.txt'

with open(file_path, 'a') as file:
    file.write(f"Response: {aResponse}\n\n")
    print(f"Response saved to {file_path}")