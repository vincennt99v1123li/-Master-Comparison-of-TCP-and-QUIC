from flask import Flask, json
from flask import send_file
import docx2txt
#from PIL import Image
#import numpy as np



#image = Image.open("Polyu.png")
#arr = np.asarray(image, dtype=np.float64)

api = Flask(__name__)
# app.config['DEBUG'] = True
text = docx2txt.process("COMP5311_Project.docx")

@api.route('/Project/Topic', methods=['GET'])
def project_topic():
    response = {"COMP5311_Topic": "Comparison of TCP and QUIC"}
    return json.dumps(response), 200

@api.route('/Project/Report', methods=['GET'])
def project_report():
    response = {"Report": text}
    return json.dumps(response), 200

@api.route('/Project/html0', methods=['GET'])
def project_html0():
    path = "assisment_registor 2.html"
    return send_file(path, as_attachment=True)

@api.route('/Project/html1', methods=['GET'])
def project_html1():
    path = "test1.html"
    return send_file(path, as_attachment=True)

@api.route('/Project/Polyu0', methods=['GET'])
def project_Image0():
    path = "Polyu-0.png"
    return send_file(path, as_attachment=True)

@api.route('/Project/Polyu1', methods=['GET'])
def project_Image1():
    path = "Polyu-1.png"
    return send_file(path, as_attachment=True)

@api.route('/Project/Polyu2', methods=['GET'])
def project_Image2():
    path = "Polyu-2.png"
    return send_file(path, as_attachment=True)

@api.route('/Project/Polyu3', methods=['GET'])
def project_Image3():
    path = "Polyu-3.png"
    return send_file(path, as_attachment=True)



if __name__ == '__main__':
    api.run(port=5000)
