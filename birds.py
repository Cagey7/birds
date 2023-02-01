#!/usr/bin/env python
import sys
from app import create_app, db
from app.models import *

run_conf = "development"

# exit if more than two args
if len(sys.argv) > 3:
    sys.exit("Invalid usage")

if len(sys.argv) == 2:
    # exit if args is incorrect
    if sys.argv[1] not in ["prod", "dev"]:
        sys.exit("Invalid usage")
    
    # change configuration
    if sys.argv[1] == "prod":
        run_conf = "production"
    elif sys.argv[1] == "dev":
        run_conf = "development"


app = create_app(run_conf)

with app.app_context():
    ...


if __name__ == "__main__":
    if run_conf == "development":
        app.run(port=5000, host="0.0.0.0")
    elif run_conf == "production":
        app.run(port=5001, host="0.0.0.0")
