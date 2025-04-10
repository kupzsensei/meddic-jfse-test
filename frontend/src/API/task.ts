import { BASE_URL } from ".";

export const createTaskAPI = async (taskData: FormData) => {
  const response = await fetch(`${BASE_URL}/api/tasks/`, {
    method: "POST",
    body: taskData,
  });

  return await response.json();
}

export const listTaskAPI = async () => {
  const response = await fetch(`${BASE_URL}/api/tasks/`, {
    method: "GET",
    headers: {
        authorization: `Bearer ${sessionStorage.getItem("token")}`,
    }
  });

  return await response.json();
}