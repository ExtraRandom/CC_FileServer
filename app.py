from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
debug_mode = False
cwd = os.getcwd()

print(os.path.realpath(__file__))

s = "\ "
s_folder = "{}{}files".format(cwd, s.replace(" ", ""))


@app.route('/')
def index():
    # log("Homepage")
    # return render_template('index.html')
    return 'This is the homepage yo'


@app.route('/<name>', methods=['GET'])
def search(name):
    # log("Request for {} file.".format(name))
    print("Received Request for File: {}".format(name))

    # s_file = "{}".format(name)
    s_file = name

    # print(os.path.join(s_folder, s_file))

    if os.path.exists(os.path.join(s_folder, s_file)):
        print("Sending a file.")
        return send_from_directory(s_folder, name)
    else:
        print("User trying to access non-existent file.")
        return 'No Data'


@app.route("/u/<name>", methods=['POST'])
def upload(name):

    # print("upload ")
    data = request.form['data']

    if os.path.exists(os.path.join(s_folder, name)):
        print("User tried to upload file that already exists on server.")
    else:
        print("User uploaded new file, saving now.")

        file = open(os.path.join(s_folder, name), "w+")
        file.writelines(data)
        file.close()

    return 'Hello there'


@app.route("/s/<command>")
def status(command):

    string = ""
    ns_string = ""
    for root, dirs, files in os.walk(s_folder):
        for name in files:
            string = string + name + ", "
            ns_string = ns_string + name + ","
    string = string[:-2]
    ns_string = ns_string[:-1]

    if command == "list":
        return string
    elif command == "ns":
        return ns_string


if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0', port=27000)
