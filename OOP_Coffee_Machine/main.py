from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def run_coffee_machine() -> None:
    '''
    Function to implement the logic of coffee machine
    '''
    # Creating objects from respective classes
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    coffee_menu = Menu()

    # Logic of coffee machine using objects, methods and attributes
    is_machine_on = True
    while is_machine_on:
        options_given = coffee_menu.get_items()
        user_choice = input(f"What would you like? ({options_given}): ")
        if user_choice == "off":
            is_machine_on = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink_chosen = coffee_menu.find_drink(user_choice)
            if coffee_maker.is_resource_sufficient(drink_chosen) and money_machine.make_payment(drink_chosen.cost):
                coffee_maker.make_coffee(drink_chosen)

def main() -> None:
    '''
    Main function to run the program
    '''
    try:
        run_coffee_machine()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted by the user. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
