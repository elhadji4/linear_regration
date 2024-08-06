import React, { useState } from 'react';

const Task = ({ task, updateTask, deleteTask, toggleComplete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description);

  const handleUpdate = () => {
    updateTask(task.id, { ...task, title, description });
    setIsEditing(false);
  };

  return (
    <div className={`task ${task.completed ? 'completed' : ''}`}>
      {isEditing ? (
        <div>
          <input 
            type="text" 
            value={title} 
            onChange={(e) => setTitle(e.target.value)} 
          />
          <textarea 
            value={description} 
            onChange={(e) => setDescription(e.target.value)} 
          ></textarea>
          <button onClick={handleUpdate}>Save</button>
        </div>
      ) : (
        <div>
          <h3>{task.title}</h3>
          <p>{task.description}</p>
        </div>
      )}
      <button onClick={() => setIsEditing(!isEditing)}>
        {isEditing ? 'Cancel' : 'Edit'}
      </button>
      <button onClick={() => deleteTask(task.id)}>Delete</button>
      <button onClick={() => toggleComplete(task.id)}>
        {task.completed ? 'Mark Incomplete' : 'Mark Complete'}
      </button>
    </div>
  );
};

export default Task;
