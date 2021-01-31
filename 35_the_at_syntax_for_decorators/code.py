import functools

user = {"username": "jose", "access_level": "guest"}

"""Functions can be defined inside of functions WHAT?"""
'''Make secure is the decorator'''
def make_secure(func):
    @functools.wraps(func) #This secures that get_admin_password still keeps its docmuntation and name.
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."

    return secure_function


"""This will make the function passed through the decorator
    when making the function to prevent errors @make_secure"""
@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())