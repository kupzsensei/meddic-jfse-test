import { BASE_URL } from ".";

// The API URL for the login and register endpoints
export const loginAPI = async (loginData: FormData) => {
  const response = await fetch(`${BASE_URL}/api/login/`, {
    method: "POST",
    body: loginData,
  });

  return await response.json();
};

// The API URL for the login and register endpoints
export const registerAPI = async (regData: FormData) => {
  const response = await fetch(`${BASE_URL}/api/register/`, {
    method: "POST",
    body: regData,
  });

  if (!response.ok) {
    const errorData = await response.json();
    return errorData;
  }
  return response;
};
