import React, { useState } from 'react';

const EditTask = ({ task, updateTask, cancelEdit }) => {
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description);

  const handleSubmit = (e) => {
    e.preventDefault();
    updateTask(task.id, { ...task, title, description });
    cancelEdit();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        placeholder="Task Title" 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
        required 
      />
      <textarea 
        placeholder="Task Description" 
        value={description} 
        onChange={(e) => setDescription(e.target.value)} 
        required 
      ></textarea>
      <button type="submit">Save</button>
      <button type="button" onClick={cancelEdit}>Cancel</button>
    </form>
  );
};

export default EditTask;
