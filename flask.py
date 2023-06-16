from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/api/printHello', methods=['GET'])
def print_hello():
    return jsonify(message='Hello, world!')

@app.route('/api/modifyRecipe', methods=['POST'])
def modify_recipe():
    # Get the recipe data from the request
    recipe_data = 1

    # Process the recipe data here...
    # Modify the recipe as needed...

    # Return the modified recipe
    return jsonify(recipe=recipe_data)

if _name_ == '_main_':
    app.run(port=5001)