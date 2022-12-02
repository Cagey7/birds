from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    return "login"


@auth.route("/register", methods=["GET", "POST"])
def register():
    return "register"
