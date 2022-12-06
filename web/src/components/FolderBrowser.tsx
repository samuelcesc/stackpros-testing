import { DirectoryObject } from "../types";
import { FolderIcon, DocumentIcon } from "@heroicons/react/24/solid";
import { Link, useLocation } from "react-router-dom";

interface FolderBrowserProps {
  contents: DirectoryObject[];
}

function FolderBrowser(props: FolderBrowserProps) {
  const { contents } = props;
  const { pathname } = useLocation();
  console.log(pathname);

  return (
    <>
      {contents.map((content, key) => (
        <div key={key}>
          {content.type === "dir" && (
            <Link
              to={
                pathname === "/"
                  ? `${content.name}`
                  : `${pathname}/${content.name}`
              }
            >
              <FolderIcon />
              {content.name}
            </Link>
          )}
          {content.type === "file" && (
            <div>
              <Link
                to={
                  pathname === "/"
                    ? `${content.name}`
                    : `${pathname}/${content.name}`
                }
              >
                <DocumentIcon />
                {content.name}
              </Link>
            </div>
          )}
        </div>
      ))}
    </>
  );
}

export default FolderBrowser;
