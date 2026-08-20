from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basit bir görev listesi (Bunu veritabanına bağlayacağız)
tasks = []
task_id_counter = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    global task_id_counter
    data = request.json
    new_task = {
        'id': task_id_counter,
        'title': data['title'],
        'status': data['status']
    }
    tasks.append(new_task)
    task_id_counter += 1
    return jsonify({'status': 'success'})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    global tasks
    task_id = request.json['id']
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)