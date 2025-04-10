import React, { useRef } from "react";
import { Link, useNavigate } from "react-router-dom";
import { registerAPI } from "../API/auth";

const RegisterPage: React.FC = () => {
    const navigate = useNavigate();
  const regForm = useRef<HTMLFormElement>(null);
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    console.log("Form submitted");

    const postData = new FormData(regForm.current!);
    registerAPI(postData).then((res) => {
        console.log(res);
      if (res.ok) {
        alert("Registration successful");
        navigate("/login");
      } else {
        // const response = res.json() as Record<string, any>;
        const keys: string[] = Object.keys(res);
        alert(`Registration failed : ${res[keys[0]]}`);
      }
    });
  };
  return (
    <main className=" flex flex-col gap-3 p-5 border-gray-400 border shadow-lg">
      <h1 className="font-bold text-2xl">Register</h1>
      <form
        className="flex flex-col gap-3"
        onSubmit={handleSubmit}
        ref={regForm}
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
        <input
          type="password"
          name="password_confirm"
          placeholder="Confirm Password"
          className="px-3 py-1 border-1 border-gray-400"
        />
        <Link to={"/login"} className="text-blue-300 underline">
          Login
        </Link>
        <input
          type="submit"
          className="bg-blue-500 px-5 py-2 rounded-lg text-white font-medium"
        />
      </form>
    </main>
  );
};

export default RegisterPage;
