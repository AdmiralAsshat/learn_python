import os
from flask import Flask
from flask import render_template
from flask import request
from flask import abort, redirect, url_for
from mdserv import utils

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    # convert the markdown
    html = utils.convert_markdown("index")
    # render the template with content
    # return to browser
    return render_template('layout.html', body=html, doc='index')

# if they go to .html, serve that .md file
# /stuff/index.html
# /foo.html
@app.route('/<doc>.html')
def mdfile(doc):
   html = utils.convert_markdown(doc)
   return render_template('layout.html', body=html, doc=doc)

# @app.route("/<subdir>/")
# def sub_directory(subdir):
#     # get the index.md for the subdir
#     docs = os.path.join(subdir, "index")
#     html = utils.convert_markdown(docs) 
#     return render_template('layout.html', body=html)

@app.route("/edit/<doc>.html", methods=['POST', 'GET'])
def edit(doc):
    # if they are posting a change
    if request.method == 'POST':
        contents = request.form['contents']

        # write the contents to the file
        with open(os.path.join("docs", doc + ".md"), 'w') as f:
            f.write(contents)
        # redirect to the new file
        return redirect(doc + '.html')
    else:
        # load the raw md file 
        contents = open(os.path.join("docs", doc + ".md")).read()
        # give the edit template
        return render_template('edit.html', doc=doc, contents=contents)