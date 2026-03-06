import os
import sys
from google.genai import types

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the specified file's raw content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to be read",
            ),
        },
        required=["file_path"],
    )
)

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    try:
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except ValueError:
        return f"Error: os.path.commonpath([{working_dir_abs}, {target_file}]) failed and raised a ValueError"
    except OSError:
        return f"Error: open({target_file}, 'r') failed and raised a OSError"

    
    return content
