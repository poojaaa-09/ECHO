from flask import render_template,request,redirect
import speech_recognition as sr
from application import app
from flask_cors import cross_origin
from application.convert import text_to_speech

#
@app.route("/",methods=['GET','POST'])
def index():
    return render_template("mainpage.html")



@app.route('/textspeech', methods=['POST', 'GET'])
@cross_origin()
def textspeech():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('textspeech.html')
    else:
        return render_template('textspeech.html')

#
# @app.route('/speechtext',methods=['POST','GET'])
# def speechtext():
#     transcript = ""
#     if request.method == "POST":
#
#         file = request.files["file"]
#         speech_text(file)
#
#     return render_template('speechtext.html')


@app.route("/speechtext", methods=["GET", "POST"])
def speechtext():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = AudioSegment.from_wav(file)

            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)


    return render_template('speechtext.html', transcript=transcript)

if __name__ == "__main__":
    app.run(port=8000, debug=True)