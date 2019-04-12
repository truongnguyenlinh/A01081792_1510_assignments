import requests


def request_image():
    res = requests.get("https://api.nasa.gov/planetary/apod?api_key=yfzbdZ4taiMg87W4CM0hbXG2Xsd4icD3Cj151Gtw")
    pyth_dictionary = res.json()
    return pyth_dictionary['url']


def website():
    """Display a created website."""
    user_name = input("Please enter your name!")
    user_name.strip().title()
    user_description = input("Please enter one sentence with a brief description of yourself.")
    user_description.strip().title()

    image_src = request_image()

    contents = """<!doctype html><html lang="en"> 
    <head><meta charset="utf-8"> 
    <title>Introduction</title> 
    <meta name="description" content="%s’s webpage"> 
    <meta name="author" content="%s"> 
    <link rel="stylesheet" href="css/styles.css?v=1.0"> 
    </head> 
    <body>
    <img src="%s"> 
    <center> 
    <h1>%s</h1> 
    </center> 
    %s
    </body> 
    </html>""" % (user_name, user_name, image_src, user_name, user_description)
    with open("index.html", "w") as file_object:
        file_object.write(contents)


def main():
    website()


if __name__ == '__main__':
    main()
