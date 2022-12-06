import { useQuery } from "react-query";

const BASE_API_URL = "http://localhost:8000";

export function useFetchPathData(path: string) {
  const url = `${BASE_API_URL}${path}`;
  return useQuery(url, () => fetch(url).then((res) => res.json()));
}
