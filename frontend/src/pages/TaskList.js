import React, { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "../api";
import Task from "../components/Task";

const TaskList = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState({ title: "", description: "" });

    useEffect(() => {
        fetchTasks();
    }, []);

    const fetchTasks = async () => {
        const data = await getTasks();
        setTasks(data);
    };

    const handleCreateTask = async () => {
        await createTask(newTask);
        fetchTasks();
        setNewTask({ title: "", description: "" });
    };

    const handleUpdateTask = async (taskId, updatedTask) => {
        await updateTask(taskId, updatedTask);
        fetchTasks();
    };

    const handleDeleteTask = async (taskId) => {
        await deleteTask(taskId);
        fetchTasks();
    };

    return (
        <div>
            <h1>To-Do List</h1>
            <input
                type="text"
                placeholder="Task Title"
                value={newTask.title}
                onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
            />
            <input
                type="text"
                placeholder="Task Description"
                value={newTask.description}
                onChange={(e) => setNewTask({ ...newTask, description: e.target.value })}
            />
            <button onClick={handleCreateTask}>Add Task</button>
            <div>
                {tasks.map((task) => (
                    <Task key={task.id} task={task} onUpdate={handleUpdateTask} onDelete={handleDeleteTask} />
                ))}
            </div>
        </div>
    );
};

export default TaskList;
