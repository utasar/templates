from flask import Flask, render_template
import os
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all the PNG files in the "static" folder
    static_folder = os.path.join(app.root_path,'static')
    png_files =[f for f in os.listdir(static_folder) if f.endwith('.png')]

    # Select a random image file from the list
    random_png = random.choice(png_files)

    # Render the "index.html" template and pass in the selected image file
    return render_template('index.html', random_png=random_png)

    @app.route('/static/<path:path>')
    def serve_static(path):
        # Serve static files from the static folder
        return send_from_directory('static', path)

if __name__ == '__main__':
    app.run()

