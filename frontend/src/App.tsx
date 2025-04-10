import { Outlet } from "react-router-dom"


function App() {

  return (
    <main className="h-screen w-screen flex flex-col gap-5 justify-center items-center">
      <Outlet />
    </main>
  )
}

export default App
