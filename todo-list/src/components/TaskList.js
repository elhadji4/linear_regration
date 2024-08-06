import React, { useState } from 'react';
import Task from './Task';

const TaskList = ({ tasks, updateTask, deleteTask, toggleComplete }) => {
  const [filter, setFilter] = useState('all');

  const filteredTasks = tasks.filter(task => {
    if (filter === 'completed') return task.completed;
    if (filter === 'incomplete') return !task.completed;
    return true;
  });

  return (
    <div>
      <div className="filter-buttons">
        <button onClick={() => setFilter('all')}>All</button>
        <button onClick={() => setFilter('completed')}>Completed</button>
        <button onClick={() => setFilter('incomplete')}>Incomplete</button>
      </div>
      <div className="task-list">
        {filteredTasks.map(task => (
          <Task 
            key={task.id} 
            task={task} 
            updateTask={updateTask} 
            deleteTask={deleteTask} 
            toggleComplete={toggleComplete} 
          />
        ))}
      </div>
    </div>
  );
};

export default TaskList;
