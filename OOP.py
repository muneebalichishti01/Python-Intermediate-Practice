class ParentClass:
    '''
    Generic parent class
    '''
    def __init__(self):
        '''
        Initialize the parent class
        '''
        pass

    def parent_method(self):
        '''
        Method in the parent class
        '''
        pass

class ChildClass(ParentClass):
    '''
    Generic child class inheriting from ParentClass
    '''
    def __init__(self):
        '''
        Initialize the child class
        '''
        super().__init__()

    def child_method(self):
        '''
        Method in the child class
        '''
        pass

def main() -> None:
    '''
    Main function to create objects and run the program
    '''
    obj = ChildClass()
    pass

if __name__ == "__main__":
    main()
    