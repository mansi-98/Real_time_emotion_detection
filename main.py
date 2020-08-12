# import the necessary packages
from flask import Flask, render_template, Response
from videoTester import VideoCamera

app = Flask(__name__)
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')

def gen(camera):
    while True:
        #get camera frame
        videoTester.get_frame()
 
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # defining server ip address and port
    app.run(host='0.0.0.0',port='8080', debug=True)
