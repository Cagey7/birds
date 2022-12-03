#!/usr/bin/env python
from app import create_app, db
from app.models import *

app = create_app("default")
with app.app_context():
    db.drop_all()
    db.create_all()


if __name__ == "__main__":
    app.run()
