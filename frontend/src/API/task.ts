import { BASE_URL } from ".";

export const createTaskAPI = async (taskData: FormData) => {
  const response = await fetch(`${BASE_URL}/api/tasks/`, {
    method: "POST",
    body: taskData,
  });

  return await response.json();
};

export const listTaskAPI = async () => {
  const response = await fetch(`${BASE_URL}/api/tasks/`, {
    method: "GET",
    headers: {
      authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0MzgyNzE0LCJpYXQiOjE3NDQzNTM5MTQsImp0aSI6ImU2YzZmNzE1MzUwZDRkNzc4ZGRlOGU4ZDFlOWQ1MTVhIiwidXNlcl9pZCI6MTZ9.mK4YqWM78U7Ws4KxlTQ30y7u0-vLRlqnhUEZ-sviPik`,
    },
  });

  return await response.json();
};
