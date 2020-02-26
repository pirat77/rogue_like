import os


def updater():
    user_directory = (input("Type relative path of files' directory to be updated."))
    user_change_from = input("What do you want to be replaced?")
    user_change_to = input("What shall it be replaced with?")

    try:
        os.listdir(user_directory)
    except FileNotFoundError:
        print("Directory not found.")

    for file_name in os.listdir(user_directory):
        with open(user_directory + "/" + file_name, 'r') as f:
            contents = f.read()

        contents = contents.replace(user_change_from, user_change_to)

        with open(user_directory + "/" + file_name, 'w') as f:
            f.write(contents)


updater()
