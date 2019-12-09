from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import docker_interface
import uuid
from shutil import copyfile
import boto3
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/challenge-1', methods=["POST"])
def challenge_1():
    if 'file' not in request.files:
        return "Error no file found"
    file = request.files['file']
    filename = "student_submission.py"
    folder_name = str(uuid.uuid4())
    os.mkdir(folder_name)
    file.save(os.path.join(folder_name, filename))
    copyfile("./../challenge_1/verify.py", folder_name + "/verify.py")
    copyfile("./../challenge_1/Dockerfile", folder_name + "/Dockerfile")
    image_id = docker_interface.build_image(path=folder_name, labels={}, tag=folder_name)
    try:
        result = docker_interface.run_container(image=folder_name, ports={5555:5555})
    except Exception as e:
        print(e)
        return "Error: Your code crashed. Please test your code and ensure it works prior to submission."
    docker_interface.remove_image(image_id)
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    os.rmdir(folder_name)

    client = boto3.client('dynamodb', region_name='us-east-1')
    database_record = client.get_item(
        Key={"student": {"S": request.form['Name']}},
        TableName="Scores"
    )

    final_item = {}
    result_text = str(result)
    result_text = result_text[2:]
    result_text = result_text[:-3]
    print(result_text)

    if "Item" in database_record:
        print("Found record")

        if 'c1' in database_record['Item']:
            if database_record['Item']['c1']['S'] != "pass":
                print("Found c1, checking for victory...")
                if result_text == "Victory!":

                    database_record['Item']['c1']['S'] = "pass"
                    database_record['Item']['score']['N'] = str(int(database_record['Item']['score']['N']) + 15)
        else:
            if result_text == "Victory!":
                    database_record['Item']['c1'] = { 'S': 'pass' }
                    database_record['Item']['score']['N'] = str(int(database_record['Item']['score']['N']) + 15)
            else:
                database_record['Item']['c1'] = { 'S': 'fail' }

        final_item = database_record["Item"]

    else:
        print("No record found")

        data = {
            "score": {"N": "0"},
            "student": {"S": request.form['Name']},
            "c1": {"S": "fail"}
        }

        if result_text == "Victory!":
            data['c1']['S'] = 'pass'
            data['score']['N'] = "15"

        final_item = data

    client.put_item(
        TableName="Scores",
        Item=final_item
    )
    return result

@app.route('/challenge-2', methods=["POST"])
def challenge_1():
    if 'file' not in request.files:
        return "Error no file found"
    file = request.files['file']
    filename = "student_submission.py"
    folder_name = str(uuid.uuid4())
    os.mkdir(folder_name)
    file.save(os.path.join(folder_name, filename))
    copyfile("./../challenge_2/verify.py", folder_name + "/verify.py")
    copyfile("./../challenge_2/Dockerfile", folder_name + "/Dockerfile")
    image_id = docker_interface.build_image(path=folder_name, labels={}, tag=folder_name)
    try:
        result = docker_interface.run_container(image=folder_name, ports={5555:5555})
    except Exception as e:
        print(e)
        return "Error: Your code crashed. Please test your code and ensure it works prior to submission."
    docker_interface.remove_image(image_id)
    for file in os.listdir(folder_name):
        file_path = os.path.join(folder_name, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    os.rmdir(folder_name)

    client = boto3.client('dynamodb', region_name='us-east-1')
    database_record = client.get_item(
        Key={"student": {"S": request.form['Name']}},
        TableName="Scores"
    )

    final_item = {}
    result_text = str(result)
    result_text = result_text[2:]
    result_text = result_text[:-3]
    print(result_text)

    if "Item" in database_record:
        print("Found record")

        if 'c2' in database_record['Item']:
            if database_record['Item']['c2']['S'] != "pass":
                print("Found c2, checking for victory...")
                if result_text == "Victory!":

                    database_record['Item']['c2']['S'] = "pass"
                    database_record['Item']['score']['N'] = str(int(database_record['Item']['score']['N']) + 50)
        else:
            if result_text == "Victory!":
                    database_record['Item']['c2'] = { 'S': 'pass' }
                    database_record['Item']['score']['N'] = str(int(database_record['Item']['score']['N']) + 50)
            else:
                database_record['Item']['c2'] = { 'S': 'fail' }

        final_item = database_record["Item"]

    else:
        print("No record found")

        data = {
            "score": {"N": "0"},
            "student": {"S": request.form['Name']},
            "c2": {"S": "fail"}
        }

        if result_text == "Victory!":
            data['c2']['S'] = 'pass'
            data['score']['N'] = "50"

        final_item = data

    client.put_item(
        TableName="Scores",
        Item=final_item
    )
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
