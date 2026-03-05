import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    
    try:
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)
        
        command_result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30
        )

        result = ""

        if command_result.returncode != 0:
            result += f"Process exited with code {command_result.returncode}\n"

        if command_result.stdout:
            result += f"STDOUT: {command_result.stdout}\n"

        if command_result.stderr:
            result += f"STDERR: {command_result.stderr}\n"

        if not(command_result.stdout or command_result.stderr):
            result += f"No output produced\n"


    except Exception as e:
        return f'Error: executing Python file: {e}'

    return result


