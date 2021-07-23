# Today is day5, today i will be revising object oriented concepts
# in python so I am thinking of making a Home appliance app

class Home:
    """
    Here I am making a Home Appliance App where I am declaring different
    classes for each appliance and making home as my super class I am
    inheriting it to the child class HomeAppliance
    :param is_on
    """
    def __init__(self, is_on):
        self.is_on = is_on

    def set_default(self):
        self.is_on = False


class HomeAppliance(Home):
    """
    The CLASS: HomeAppliance is the child class of Home, this inherits
    the VAR: is_on, and this has three methods, one is to switch on the appliance
    two is to switch off the appliance and the last method is to display the status
    of the appliance.
    :param is_on
    :param name
    :param loc
    :returns null
    """
    def __init__(self, is_on, name, loc):
        super().__init__(is_on)
        self.Name = name
        self.Loc = loc

    def switch_off(self):
        self.is_on = False
        if self.is_on is True:
            print("The {0} in your {1} is switched on".format(self.Name, self.Loc))
        else:
            print("The {0} in your {1} is switched off".format(self.Name, self.Loc))

    def switch_on(self):
        self.is_on = True
        if self.is_on is True:
            print("The {0} in your {1} is switched on".format(self.Name, self.Loc))
        else:
            print("The {0} in your {1} is switched off".format(self.Name, self.Loc))

    def status_display(self):
        if self.is_on is True:
            print("The {0} in your {1} is switched on".format(self.Name, self.Loc))
        else:
            print("The {0} in your {1} is switched off".format(self.Name, self.Loc))


if __name__ == '__main__':
    select_appliance = input("Which appliance do you want to use?\n").lower()
    location = input("Where is this {} located at: ".format(select_appliance))
    appliance = HomeAppliance(False, select_appliance, location)
    while True:
        print("If you want to exit please type quit")
        query_to_on_or_off = input("Do you want to switch it on or off?\n").lower()
        if query_to_on_or_off == "on":
            appliance.switch_on()
        elif query_to_on_or_off == "off":
            appliance.switch_off()
        elif query_to_on_or_off == "quit":
            break
        else:
            appliance.status_display()
