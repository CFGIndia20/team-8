from flaskblog import create_app

app = create_app() #not passing config as a parameter bcoz that's the default parameter

if __name__ == '__main__':
    app.run(debug=True)