from turtle import Turtle, Screen

def run_turtle() -> None:
    '''
    Function to use the turtle built-in library and run logic
    '''
    my_turtle = Turtle()
    my_turtle.shape("arrow")
    my_turtle.color("red")
    for shape_side_n in range(3, 11):
        draw_shape(shape_side_n, my_turtle)
    my_screen = Screen()
    my_screen.exitonclick()

def draw_shape(num_sides: int, my_turtle: object) -> None:
    '''Function to draw shapes using given range'''
    angle = 360 / num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_turtle()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    