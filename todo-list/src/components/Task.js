import React, { useState } from 'react';
import EditTask from './EditTask';

const Task = ({ task, updateTask, deleteTask, toggleComplete }) => {
  const [isEditing, setIsEditing] = useState(false);

  const handleCancelEdit = () => {
    setIsEditing(false);
  };

  return (
    <div className={`task ${task.completed ? 'completed' : ''}`}>
      {isEditing ? (
        <EditTask 
          task={task} 
          updateTask={updateTask} 
          cancelEdit={handleCancelEdit} 
        />
      ) : (
        <div>
          <h3>{task.title}</h3>
          <p>{task.description}</p>
          <button onClick={() => setIsEditing(true)}>Edit</button>
          <button onClick={() => deleteTask(task.id)}>Delete</button>
          <button onClick={() => toggleComplete(task.id)}>
            {task.completed ? 'Mark Incomplete' : 'Mark Complete'}
          </button>
        </div>
      )}
    </div>
  );
};

export default Task;
