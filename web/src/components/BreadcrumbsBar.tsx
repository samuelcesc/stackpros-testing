import { Link, useLocation } from "react-router-dom";

function BreadcrumbsBar() {
  let paths: Record<string, any> = { "/": "/" };
  const { pathname } = useLocation();

  if (pathname !== "/") {
    let previousPath: string = "";
    let currentPath: string;
    for (var path of pathname.split("/")) {
      if (path !== "") {
        currentPath = `${previousPath}/${path}`;
        paths[path] = currentPath;
        previousPath = currentPath;
      }
    }
  }

  return (
    <div className="bg-white p-4 flex items-center flex-wrap">
      <ul className="flex items-center">
        {Object.keys(paths).map((path, index) => (
          <li key={index} className="inline-flex items-center">
            {(paths[path] === "/" && (
              <Link to="/" className="text-gray-600 hover:text-blue-500">
                <svg
                  className="w-5 h-auto fill-current mx-2 text-gray-400"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="#000000"
                >
                  <path d="M0 0h24v24H0V0z" fill="none" />
                  <path d="M10 19v-5h4v5c0 .55.45 1 1 1h3c.55 0 1-.45 1-1v-7h1.7c.46 0 .68-.57.33-.87L12.67 3.6c-.38-.34-.96-.34-1.34 0l-8.36 7.53c-.34.3-.13.87.33.87H5v7c0 .55.45 1 1 1h3c.55 0 1-.45 1-1z" />
                </svg>
              </Link>
            )) || (
              <>
                <span className="mx-4 h-auto text-gray-400 font-medium">/</span>
                <Link
                  to={paths[path]}
                  className="text-gray-600 hover:text-blue-500"
                >
                  {path}
                </Link>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BreadcrumbsBar;
