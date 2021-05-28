from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

story = stories.Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

app = Flask(__name__)

@app.route('/madlibs')
def madlibs_fill():
    """Gets the person's input for Madlibs"""

    #get the template from story.prompts and loop thru it
  

    return render_template("madlibs.html", prompts = story.prompts)

@app.route('/story')
def generate_story():
    user_input = request.args
    generated_story = story.generate(user_input) #loop through user_input and fill in madlib template
    #by caling story.generate

    return render_template("story.html", user_input=user_input, generated_story=generated_story)
