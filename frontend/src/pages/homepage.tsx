import { useQuery } from "@tanstack/react-query";
import { listTaskAPI } from "../API/task";

export const HomePage: React.FC = () => {
  const { data }: { data: [] | undefined } = useQuery({
    queryKey: ["tasks"],
    queryFn: listTaskAPI,
  });
  return (
    <section className="p-5 flex flex-col gap-5">
      <div className="flex gap-5">
        <h1 className="font-bold text-2xl">Todo List</h1>
        <button className="border border-blue-400">create</button>
      </div>
      <div className="flex gap-2">
        <input
          type="search"
          placeholder="Search..."
          className="px-3 py-1 border-1 border-gray-400"
        />
        <button>search</button>
      </div>

      <div className="flex flex-col gap-3">
        {data?.map((task) => (
          <div key={task.id} className="flex gap-5">
            <h1>{task.name}</h1>
            <p>{task.description}</p>
            <button className="border border-gray-400">completed</button>
            <button className="border border-red-500">delete</button>
          </div>
        ))}
      </div>
    </section>
  );
};
