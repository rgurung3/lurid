from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/talk')
def talk():
    return render_template('talk.html', show_stressors=False)

@app.route('/send_message', methods=['POST'])
def send_message():
    # get the text from the textarea
    message = request.form.get("message", "")
    chart_data = {
        
    }
    return render_template("results.html", show_stressors=True)


if __name__ == '__main__':
    app.run(debug=True)
