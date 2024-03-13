import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Program:
    def __init__(self):
        self.buffer = ""
        self.headline = "TODO - By NOXEP\n"
        self.input = ""

        self.tasks = ["Example", "Example2", "Example3"]

    def cycle(self):

        self.buffer = ""

        match self.input:
            case "":
                pass
            case "q":
                self.quit()
            case "n":
                self.new()
            case "d":
                self.delete()
            case "h":
                self.help()
            case _:
                self.no_command()

        self.buffer += self.headline

        for i in range(self.tasks.__len__()):
            self.buffer += f"{i + 1}. {self.tasks[i]}"

        cls()

        print(self.buffer)

    def start(self):
        # check if file exists or create a new one
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as file:
                file.write("Example\nExample2\nExample3\n")

        self.load()
        self.cycle()
        while True:
            self.input = input("Enter a command: ")
            self.cycle()

    def quit(self):
        cls()
        exit(0)

    def new(self):
        cls()
        if self.tasks.__len__() >= 100:
            print("You can't have more than 100 tasks")
            input("Press enter to continue")
            return
        self.tasks.append(input("Enter a new task: ") + "\n")
        self.save()

    def delete(self):
        cls()

        for i in range(self.tasks.__len__()):
            print(f"{i + 1}. {self.tasks[i]}"[:-1])
        if int(input("Enter the number of the task to delete: ")) > self.tasks.__len__():
            cls()
            print("Invalid number")
            input("Press enter to continue")
            return
        self.tasks.pop(int(input("Enter the number of the task to delete: ")) - 1)
        self.save()


    def no_command(self):
        cls()
        print("Invalid command")
        print("Press enter to continue")
        while input() != "":
            cls()
            print("Press enter to continue")

    def help(self):
        cls()
        print("Commands:")
        print("q - Quit")
        print("n - New task")
        print("d - Delete task")
        print("h - Help")

        input("Press anything to continue")

    def load(self):
        with open("tasks.txt", "r") as file:
            self.tasks = file.readlines()

    def save(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task)


program = Program()
program.start()
