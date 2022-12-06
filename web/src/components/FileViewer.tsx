import { DirectoryObject } from "../types";

interface FileViewerProps {
  file: DirectoryObject;
}

function FileViewer(props: FileViewerProps) {
  const { file } = props;
  return <div>THIS IS A FILE: {file.name}</div>;
}

export default FileViewer;
