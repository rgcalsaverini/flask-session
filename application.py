from flask_kit import create_app

from flask_sec import create_api

app = create_app(https=False, blueprints=[
    create_api()
])

if __name__ == '__main__':
    app.run(debug=True)
