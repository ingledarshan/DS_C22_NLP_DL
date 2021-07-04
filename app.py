#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import flask

from flask import Flask

# Create an object of Flask class by the name 'app'
app = Flask(__name__)

# Create methods of flask which will route our app to hit the home web page
@app.route('/') # Home page
def hello():
    return "<h1>Hello DS_C22_NLP&DL track learners<h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

