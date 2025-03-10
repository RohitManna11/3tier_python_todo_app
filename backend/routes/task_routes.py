from flask import Blueprint, jsonify, request
from app import db
from models.task import Task

task_routes = Blueprint("task_routes", __name__)

# Get all tasks
@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Get task by ID
@task_routes.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.to_dict()), 200

# Create a new task
@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], description=data.get("description"))
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# Update a task
@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.completed = data.get("completed", task.completed)

    db.session.commit()
    return jsonify(task.to_dict()), 200

# Delete a task
@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200
