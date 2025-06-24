def logAround(func):
    def wrapper(*args, **kwargs):
        print("This is Around Before...")
        result = func(*args, **kwargs)
        print("This is Around After...")
        return result
    return wrapper

@logAround
def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)


print(search(42, (-5, 1, 3, 5, 7, 10)))


















# def logAround(func, *args, **kwargs):

#     def wrapper(*args, **kwargs):
#         import re
#         BANNED_PATTERNS = ['\\beval\\s*\\(', '\\bexec\\s*\\(', '\\bcompile\\s*\\(', '\\b__import__\\s*\\(', '\\bos\\.system\\s*\\(', '\\bos\\.popen\\s*\\(', '\\bsubprocess\\.(call|run|Popen|check_output)\\s*\\(']
#         warnings = []
#         for pattern in BANNED_PATTERNS:
#             matches = list(re.finditer(pattern, args[1]))
#             for match in matches:
#                 line_no = args[1][:match.start()].count('\n') + 1
#                 warnings.append((pattern, line_no))
#         if warnings:
#             print('⚠️ 偵測到可疑語句：')
#             for (pattern, line) in warnings:
#                 print(f' - pattern `{pattern}` at line {line}')
#         else:
#             print('✅ 程式碼看起來安全')
#             func(*args, **kwargs)
#         return
#     return wrapper

# import multiprocessing
# import sys
# from io import StringIO
# from typing import Dict
# from app.tool.base import BaseTool

# class PythonExecute(BaseTool):
#     """A tool for executing Python code with timeout and safety restrictions."""
#     name: str = 'python_execute'
#     description: str = 'Executes Python code string. Note: Only print outputs are visible, function return values are not captured. Use print statements to see results.'
#     parameters: dict = {'type': 'object', 'properties': {'code': {'type': 'string', 'description': 'The Python code to execute.'}}, 'required': ['code']}

#     @logAround
#     def _run_code(self, code: str, result_dict: dict, safe_globals: dict) -> None:
#         original_stdout = sys.stdout
#         try:
#             output_buffer = StringIO()
#             sys.stdout = output_buffer
#             exec(code, safe_globals, safe_globals)
#             result_dict['observation'] = output_buffer.getvalue()
#             result_dict['success'] = True
#         except Exception as e:
#             result_dict['observation'] = str(e)
#             result_dict['success'] = False
#         finally:
#             sys.stdout = original_stdout

#     async def execute(self, code: str, timeout: int=5) -> Dict:
#         """
#         Executes the provided Python code with a timeout.

#         Args:
#             code (str): The Python code to execute.
#             timeout (int): Execution timeout in seconds.

#         Returns:
#             Dict: Contains 'output' with execution output or error message and 'success' status.
#         """
#         with multiprocessing.Manager() as manager:
#             result = manager.dict({'observation': '', 'success': False})
#             if isinstance(__builtins__, dict):
#                 safe_globals = {'__builtins__': __builtins__}
#             else:
#                 safe_globals = {'__builtins__': __builtins__.__dict__.copy()}
#             proc = multiprocessing.Process(target=self._run_code, args=(code, result, safe_globals))
#             proc.start()
#             proc.join(timeout)
#             if proc.is_alive():
#                 proc.terminate()
#                 proc.join(1)
#                 return {'observation': f'Execution timeout after {timeout} seconds', 'success': False}
#             return dict(result)
