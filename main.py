from google import genai

file = open("data.txt", "r")
data=file.read()
file.close()

client = genai.Client(api_key="KEY")
ch = input("do you want to do (r/a) ?")
if ch == "a":
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["""The data that I am going to provide you is the data that you have already collected of the user. 
                  You can ask the user one more personal questions that you want to know more from the user. Eg. What is your favorite color?
                  Do not ask things that you already know from the data that I have provided you. Only ask teh question that you want to know more from the user. Output nothing else.
                  Data: """ + data]
    )

    question = response.text
    answer = input(question)

    file = open("data.txt", "a")
    file.write("      " + question + " " + answer)

if ch == "r":
    response= client.models.generate_content(
        model="gemini-2.0-flash",
        contents=["""The data that I am going to provide you is the data that you have already collected of the user.
                  Now you have to generate a summary of everything you know about the user from the data that I have provided you.
                  Data: """ + data]
    )
    print(response.text)