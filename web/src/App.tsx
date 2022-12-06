import BreadcrumbsBar from "./components/BreadcrumbsBar";
import FolderBrowser from "./components/FolderBrowser";
import FileViewer from "./components/FileViewer";
import { Routes, Route, useLocation } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "react-query";
import { useFetchPathData } from "./apis";

const queryClient = new QueryClient();
function App() {
  return (
    <Routes>
      <Route
        path="*"
        element={
          <QueryClientProvider client={queryClient}>
            <Layout />
          </QueryClientProvider>
        }
      />
    </Routes>
  );
}

function Layout() {
  const { pathname } = useLocation();
  const { isLoading, isError, data } = useFetchPathData(pathname);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (isError) {
    return <div>An error occured!</div>;
  }

  return (
    <div className="grid place-items-center h-screen">
      <BreadcrumbsBar />
      {(Array.isArray(data) && <FolderBrowser contents={data} />) || (
        <FileViewer file={data} />
      )}
    </div>
  );
}

export default App;
