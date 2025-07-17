# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_name():
    name = "KevFoxCodeCraft"
    print(f'My name is {name}')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Call the print_name function
    print_name()
    from openai import OpenAI

    client = OpenAI()

    resp = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": "Can you tell a joke?"}],
    )
    print(resp.choices[0].message.content)
