import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/submit', methods=['POST'])
def post_submit():
    # print(request.form)
    # print(request.args)
    name = request.form['name']
    message = request.form['message']
    
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for char in text:
        if char in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"' 

@app.route('/sort_names', methods=['POST'])
def sort_names():
    if 'names' not in request.form:
        return "You didn't submit any names!", 400
    name_string = request.form['names']
    name_list = name_string.split(',')
    sorted_name_list = sorted(name_list)
    result = ','.join(sorted_name_list)
    return result

@app.route('/names', methods=['GET'])
def get_names_and_sort():
    old_name_list = ['Alice', 'Julia', 'Karim']
    new_name_string = request.args['add']
    new_name_list = new_name_string.split(',')
    name_list = old_name_list + new_name_list
    sorted_names = sorted(name_list)
    result = ', '.join(sorted_names)
    return result



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

