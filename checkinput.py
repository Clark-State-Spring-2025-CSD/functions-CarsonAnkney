#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def get_integer(prompt_message, error_message):
    while True:
        user_input = input(prompt_message)
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()): 
            return int(user_input)
        else:
            print(error_message)

if __name__ == "__main__":
    prompt_message = "Please enter an integer: "
    error_message = "That is not a valid integer. Please try again."
   
    number = get_integer(prompt_message, error_message)
    print(f"You entered the integer: {number}")