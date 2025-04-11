import { useQuery } from "@tanstack/react-query";
import { listTaskAPI } from "../API/task";

interface taskData {
  id: number;
  name: string;
  description: string;
  completed: boolean;
  category? : {id: number, name: string};
}

interface TodoCardProps {
  data: taskData;
}

const TodoCard: React.FC<TodoCardProps> = ({ data }) => {
  return (
    <div
      key={data.id}
      className="flex flex-col gap-2 border-gray-400 border p-2"
    >
      <div className="flex gap-5 justify-between items-center">
        <h1 className="font-bold">{data.name}</h1>
        <button
          className={`${
            data.completed
              ? "font-thin text-xs bg-green-400 text-white px-2 py-1 rounded-lg"
              : "font-thin text-xs bg-gray-400 text-white px-2 py-1 rounded-lg"
          }`}
        >
          {data.completed ? "completed" : "complete"}
        </button>
      </div>
      <p>{!!data.description || "No Description"}</p>
      <p>{!!data?.category?.name || "No Category"}</p>
      <div className="flex gap-2">
        <button className="bg-green-400 text-white rounded-lg flex-1 py-1">view</button>
        <button className="bg-red-700 text-white rounded-lg flex-1 py-1">delete</button>
      </div>
    </div>
  );
};

export const HomePage: React.FC = () => {
  const { data } = useQuery<taskData[]>({
    queryKey: ["tasks"],
    queryFn: listTaskAPI,
  });
  return (
    <section className="p-5 w-[400px] h-[80vh] flex flex-col gap-5 border-2 border-blue-500">
      <div className="flex gap-5 justify-between">
        <h1 className="font-bold text-2xl">Todo List</h1>
        <button className="text-white bg-blue-400 font-bold aspect-square px-3 py-1 rounded-full shadow-lg cursor-pointer">+</button>
      </div>
      <div className="flex gap-2">
        <input
          type="search"
          placeholder="Search..."
          className="px-3 py-1 border-1 border-gray-400 w-full"
        />
        <button className="bg-blue-400 text-white rounded-lg py-1 px-4 w-min">Go</button>
      </div>

      <div className="flex flex-col gap-3 flex-1 min-h-0 overflow-y-auto">
        {data?.map((task: taskData) => (
          <TodoCard data={task} />
        ))}
      </div>
    </section>
  );
};
