import os
import markdown

def convert_markdown(doc):
    contents = open("docs/" + doc + ".md").read()
    html = markdown.markdown(contents)
    return html