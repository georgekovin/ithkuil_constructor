from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# База слогов (можно расширять)
SYLLABLES = [
    "ка", "ле", "мо", "да", "ра", "ло", "ма", "де", "ро", "ла",
    "ми", "до", "ре", "ли", "му", "ды", "ру", "лу", "мя", "дё",
    "ря", "лё", "мё", "дэ", "рэ", "лэ", "ма", "ди", "ри", "ли",
    "ко", "ле", "ме", "де", "ре", "ло", "мы", "ды", "ры", "лы"
]

def get_something():
    print('hi')




@app.route('/')
def index():
    data = get_something() # Вызываем вашу функцию
    return render_template('index.html', result=data)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
