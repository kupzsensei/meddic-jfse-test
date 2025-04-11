import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { loginAPI } from "../API/auth";

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const loginForm = React.useRef<HTMLFormElement>(null);
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    console.log("Form submitted");
    // Add your login logic here
    const postData = new FormData(loginForm.current!);
    loginAPI(postData).then((res) => {
      console.log(res);
      if (res.access) {
        sessionStorage.setItem("token", res.access);
        
        alert("Login successful");
        navigate("/");
      } else {
        const keys: string[] = Object.keys(res);
        alert(`Login failed : ${res[keys[0]]}`);
      }
    });
  };

  return (
    <main className=" flex flex-col gap-3 p-5 border-gray-400 border shadow-lg">
      <h1 className="font-bold text-2xl">Login</h1>
      <form
        className="flex flex-col gap-3"
        onSubmit={handleSubmit}
        ref={loginForm}
      >
        <input
          type="text"
          name="username"
          placeholder="Username"
          className="px-3 py-1 border-1 border-gray-400"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          className="px-3 py-1 border-1 border-gray-400"
        />
        <Link to={"/register"} className="text-blue-300 underline">
          Register
        </Link>
        <input
          type="submit"
          className="bg-blue-500 px-5 py-2 rounded-lg text-white font-medium"
        />
      </form>
    </main>
  );
};

export default LoginPage;
