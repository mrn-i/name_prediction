#!/usr/bin/env python3

from name_predict_app import app
import os

if __name__ == "__main__":

# in development
    app.run(debug=True)

# before exporting
# Bind to PORT if defined, otherwise default to 5000.

    #port = int(os.environ.get('PORT', 5000))
    #app.run(debug=True, host='0.0.0.0', port=port)


