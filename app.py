import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "code": "SIA 101",
        "name": "System Integration and Architecture",
        "description": "Principles of integrating enterprise applications, APIs, and cloud services."
    },
    {
        "id": 2,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to building responsive web and mobile interfaces."
    },
    {
        "id": 3,
        "code": "DBMS 201",
        "name": "Database Management Systems",
        "description": "Relational database design, SQL querying, and data modeling."
    },
    {
        "id": 4,
        "code": "NET 202",
        "name": "Computer Networks and Security",
        "description": "Fundamentals of HTTP, HTTPS, network protocols, and cybersecurity."
    },
    {
        "id": 5,
        "code": "SOFT 301",
        "name": "Software Engineering",
        "description": "Software development lifecycle, version control with Git, and testing."
    }
]

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Student Course API is running smoothly."
    }), 200

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses), 200

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)
    if course is None:
        return jsonify({
            "error": "Not Found",
            "message": f"Course with ID {course_id} does not exist."
        }), 404
    return jsonify(course), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
