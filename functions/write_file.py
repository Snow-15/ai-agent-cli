import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Creates a new file or overwrite an existing one with new text",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path where the file should be saved",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string content to write into the file",
            ),
        },
        required=[
            "file_path",
            "content",
        ],
    )
)

def write_file(working_directory, file_path, content):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    try:
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

    except ValueError:
        return f"Error: os.path.commonpath([{working_dir_abs}, {target_file}]) failed and raised a ValueError"
    except OSError:
        return f"Error: open({target_file}, 'w') failed and raised a OSError"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



