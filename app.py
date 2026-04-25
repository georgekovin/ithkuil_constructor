from flask import Flask, request, jsonify

app = Flask(__name__)

# База слогов (можно расширять)
SYLLABLES = [
    "ка", "ле", "мо", "да", "ра", "ло", "ма", "де", "ро", "ла",
    "ми", "до", "ре", "ли", "му", "ды", "ру", "лу", "мя", "дё",
    "ря", "лё", "мё", "дэ", "рэ", "лэ", "ма", "ди", "ри", "ли",
    "ко", "ле", "ме", "де", "ре", "ло", "мы", "ды", "ры", "лы"
]


@app.route('/api/syllables', methods=['GET'])
def get_syllables():
    """Получить список доступных слогов"""
    return jsonify({"syllables": SYLLABLES})


@app.route('/api/build-word', methods=['POST'])
def build_word():
    """
    Сконструировать слово из предоставленных слогов.
    
    Ожидаемый JSON:
    {
        "syllables": ["ка", "ле", "ма"]
    }
    
    Ответ:
    {
        "word": "калема",
        "syllables_count": 3
    }
    """
    data = request.get_json()
    
    if not data or 'syllables' not in data:
        return jsonify({"error": "Необходимо предоставить список слогов в поле 'syllables'"}), 400
    
    syllables = data['syllables']
    
    if not isinstance(syllables, list):
        return jsonify({"error": "Поле 'syllables' должно быть списком"}), 400
    
    if len(syllables) == 0:
        return jsonify({"error": "Список слогов не может быть пустым"}), 400
    
    # Проверяем, что все элементы - строки
    for s in syllables:
        if not isinstance(s, str):
            return jsonify({"error": "Все слоги должны быть строками"}), 400
    
    # Собираем слово из слогов
    word = ''.join(syllables)
    
    return jsonify({
        "word": word,
        "syllables_count": len(syllables),
        "syllables_used": syllables
    })


@app.route('/api/generate-random-word', methods=['POST'])
def generate_random_word():
    """
    Сгенерировать случайное слово из заданного количества слогов.
    
    Ожидаемый JSON:
    {
        "length": 3
    }
    
    Ответ:
    {
        "word": "калемаро",
        "syllables_count": 3,
        "syllables_used": ["ка", "ле", "ма", "ро"]
    }
    """
    import random
    
    data = request.get_json()
    
    if not data or 'length' not in data:
        return jsonify({"error": "Необходимо указать количество слогов в поле 'length'"}), 400
    
    length = data['length']
    
    if not isinstance(length, int) or length < 1:
        return jsonify({"error": "Длина должна быть положительным целым числом"}), 400
    
    if length > 10:
        return jsonify({"error": "Максимальная длина слова - 10 слогов"}), 400
    
    # Выбираем случайные слоги
    selected_syllables = [random.choice(SYLLABLES) for _ in range(length)]
    word = ''.join(selected_syllables)
    
    return jsonify({
        "word": word,
        "syllables_count": length,
        "syllables_used": selected_syllables
    })


@app.route('/health', methods=['GET'])
def health_check():
    """Проверка работоспособности сервиса"""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
