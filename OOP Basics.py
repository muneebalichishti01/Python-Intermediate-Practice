from turtle import Turtle, Screen
from prettytable import PrettyTable

def run_pretty_table_library() -> None:
    '''
    Function to use the cutsom installed prettytable library for understanding OOP
    '''
    my_table = PrettyTable()    # Object creation from the class
    my_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # Method usage for the object
    my_table.add_column("Type", ["Electric", "Water", "Fire"])  # Method usage for the object
    my_table.align = "l"    # Attribute usage for the object
    print(my_table)

def run_turtle_library() -> None:
    '''
    Function to use the turtle built-in library for understanding OOP
    '''
    my_turtle = Turtle()        # Object creation from the class
    my_turtle.shape("turtle")   # Method usage for the object
    my_turtle.color("blue")     # Method usage for the object

    for _ in range(4):          # Method usage for the object in loop
        my_turtle.forward(100)
        my_turtle.left(90)
        my_turtle.forward(100)

    my_screen = Screen()        # Method usage for the object
    my_screen.exitonclick()     # Method usage for the object

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        # run_turtle_library()
        run_pretty_table_library()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    