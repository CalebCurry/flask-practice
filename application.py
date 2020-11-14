from drink_ratings import app as application #application for AWS


#__name__ will be main if this is ran directly with Python
#but not if imported to another module
if __name__ == '__main__':
    app.run(debug=True)
