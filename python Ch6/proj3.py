#birthday wishes
#demo keywords arguments and default parameter values
#positional parameters
def birthday1(name, age):
    print("Happy Birthday,", name, "!", "I hear you are", age, "today.\n")
#parameter with default values
def birthday2(name = "Jackson", age = 11):
    print("Happy Birthday", name, "!", "I hear you're", age, "today.\n")
birthday1("jackson", 1)
birthday1(1, "Jackson")
birthday1(age = 11, name = "Jackson")

birthday2()
birthday2(name = "Kathy")
birthday2(age = 12)
birthday2(name = "Kathy", age = 12)
birthday2("Kathy", 12)

