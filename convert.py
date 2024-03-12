import os
import json

def create(file_name: str, content: list | dict | str = None) -> None:
    """Create a new JSON file.

    Args:
        file_name (str): Nombre del archivo o ruta.
        content (list | dict | str, optional): Contenido del archivo. Defaults to None.
    """
    mode = "w" if content else "x"
    try:
        with open(file_name, mode) as file:
            if content:
                if isinstance(content, dict):
                    content = [content]
                content = json.dumps(content, indent=2)
                file.write(content)
    except FileExistsError as error:
        raise OSError(f"JSON '{file_name}' already exists") from error
    except PermissionError as error:
        raise OSError(f"You do not have permission to create '{file_name}'") from error


def update(file_name: str, content: list | dict) -> None:
    """Create or update a JSON file.

    Args:
        file_name (str): Nombre del archivo.
        content (list | dict): Contenido a agregar al archivo.
    """
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            try:
                file_content = json.loads(file_content)
            except Exception:
                pass

        if isinstance(file_content, list):
            if isinstance(content, dict):
                file_content.append(content)
            elif isinstance(content, list):
                file_content += content
        elif isinstance(file_content, dict):
            if isinstance(content, dict):
                file_content = [file_content, content]
            elif isinstance(content, list):
                file_content = [file_content] + content

        with open(file_name, 'w') as file:
            file_content = json.dumps(file_content)
            file.write(file_content)

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' not found")


def read(file_name: str) -> list | dict:
    """Lee el contenido de un archivo JSON.

    Args:
        file_name (str): Nombre del archivo.

    Returns:
        list | dict: Contenido del archivo.
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File '{file_name}' not found")

    with open(file_name, "r") as file:
        content = file.read()
        try:
            return json.loads(content)
        except Exception:
            return content
