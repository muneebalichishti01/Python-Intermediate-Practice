class ParentClass:
    '''
    Generic parent class
    '''
    def __init__(self) -> None:
        '''
        Initialize the parent class
        '''
        pass

    def parent_method(self) -> None:
        '''
        Method in the parent class
        '''
        pass

class ChildClass(ParentClass):
    '''
    Generic child class inheriting from ParentClass
    '''
    def __init__(self) -> None:
        '''
        Initialize the child class
        '''
        super().__init__()

    def child_method(self) -> None:
        '''
        Method in the child class
        '''
        pass

def main() -> None:
    '''
    Main function to create objects and run the program
    '''
    obj: ChildClass = ChildClass()
    pass

if __name__ == "__main__":
    main()
    