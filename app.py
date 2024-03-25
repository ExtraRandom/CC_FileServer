from flask import Flask, request, send_from_directory, render_template
import os
from requests import get

app = Flask(__name__)
debug_mode = False
cwd = os.getcwd()

s_folder = os.path.join(cwd, "files")

try:
    print("Public IP is {}:27000".format(get("https://api.ipify.org/").text))
except Exception as e:
    print("Error getting IP: {}".format(e))

# REMOTE RELATED
valid_commands = ["up", "down", "left", "right", "forward", "back",
                  "dig", "dig up", "dig down"]
command_queue = []


@app.route('/')
def index():
    """Homepage"""
    # log("Homepage")     # return render_template('index.html')
    return 'Homepage'


@app.route('/cc/d/<name>', methods=['GET'])
def search(name):
    """
    If 'name' is a file on the server then send it
    """

    # log("Searching for {} file.".format(name))
    s_file = "{}".format(name)

    if os.path.exists(os.path.join(s_folder, s_file)):
        print("Sending a file.")
        return send_from_directory(s_folder, name)
    else:
        print("User trying to access non-existent file.")
        return 'No Data'


@app.route("/cc/u/<name>", methods=['POST'])
def upload(name):
    """
    Accept upload of file 'name' if it doesn't already exist on the server
    """

    data = request.form['data']

    if os.path.exists(os.path.join(s_folder, name)):
        print("File exists, won't overwrite")
        return 'No'
    else:
        print("File doesnt exist, writing new file")

        file = open(os.path.join(s_folder, name), "w+")
        file.writelines(data)
        file.close()
        return 'Yes'


@app.route("/cc/s/<command>")
def status(command):
    """
    Return list of files
    """

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


@app.route("/cc/i/inspect", methods=['POST'])
def inspect():
    data = request.form['data']
    print(data)
    return "ty"


@app.route("/cc/r/remote")
def remote_control():
    if len(command_queue) > 0:
        cmd = command_queue.pop(0)
        return cmd
    else:
        return "Idle"


@app.route("/control")
def remote_control_control_page():
    return render_template('control_page.html')


@app.route("/control_queue_add", methods=['POST'])
def remote_control_add_to_queue():
    data = request.form['cmd']
    print(data)
    command_queue.append(data)
    print(command_queue)
    return "Hello"


if __name__ == '__main__':
    app.run(debug=debug_mode, host='0.0.0.0', port=27000)
