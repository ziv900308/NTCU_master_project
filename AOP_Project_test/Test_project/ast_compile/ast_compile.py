import ast
import sys
import importlib.util
import os


# ===== ✅ Method 1: 使用 importlib.util 載入檔案 =====
def load_module_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None:
        raise ImportError(f"無法從 {file_path} 載入 {module_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[module_name] = module  # ✅ 確保可以被後續 import 使用
    return module

# ===== ✅ AST 擷取 Import =====
def extract_imports(source_code):
    tree = ast.parse(source_code)
    imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append((alias.name, None))  # (模組名, 無 from)
        elif isinstance(node, ast.ImportFrom):
            module = node.module
            for alias in node.names:
                imports.append((module, alias.name))  # (from 模組, 欲導入名稱)
    return imports, tree

# ===== ✅ Import 檢查並補救（支援檔案路徑）=====
# 你可以在這裡自訂 module 對應的 fallback 路徑
fallback_module_paths = {
    "FrontendManager": "C:/Users/Boss Hsu/Python_Code/Python_AOP_Library-main/AOP_Project_test/Test_project/Employees System Project/FrontendManager.py"
}

def validate_imports(import_list):
    errors = []
    for module, name in import_list:
        try:
            if name is None:
                print("None... import module:", module)
                __import__(module)
            else:
                print("Find... import module: {}, name: {}".format(module, name))
                imported_module = __import__(module, fromlist=[name])
                getattr(imported_module, name)
        except Exception as e:
            # 嘗試手動載入
            print(f"❗自動匯入失敗：{module}.{name or '*'}，嘗試從 fallback 載入")
            fallback_path = fallback_module_paths.get(module)
            if fallback_path and os.path.exists(fallback_path):
                try:
                    loaded_module = load_module_from_path(module, fallback_path)
                    if name and not hasattr(loaded_module, name):
                        raise AttributeError(f"{module} 沒有成員 {name}")
                except Exception as inner_e:
                    errors.append((f"{module}.{name or '*'}", f"Fallback 失敗: {inner_e}"))
                    print("Fallback 也失敗...")
            else:
                errors.append((f"{module}.{name or '*'}", f"找不到 fallback 路徑或檔案"))
    return errors

# ===== ✅ Weaving + 執行 =====
def weave_and_run(source_code):
    import_list, tree = extract_imports(source_code)
    print("📦 Import_List: ", import_list)
    errors = validate_imports(import_list)

    if errors:
        print("⚠️ 發現無法匯入的模組/成員:")
        for mod, msg in errors:
            print(f" - {mod}: {msg}")
        return

    print("✅ 所有匯入模組驗證通過，準備執行")

    compiled = compile(tree, filename="<ast>", mode="exec")
    exec_globals = globals().copy()
    exec_globals["__name__"] = "__main__"
    exec(compiled, exec_globals)


def scan_full_module_map(project_root):
    module_map = {}

    for dirpath, _, filenames in os.walk(project_root):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(filepath, project_root)
                module_name = rel_path[:-3].replace(os.sep, ".")  # 移除 .py 並轉為 module.path
                module_map[module_name] = filepath

    return module_map

print("="*20 + " Scan directory " + "="*20)
module = scan_full_module_map("C:/Users/Boss Hsu/Python_Code/Python_AOP_Library-main/AOP_Project_test/Test_project/Employees System Project")
for module_name in module:
    print(module_name)
print("="*20 + " Scan directory " + "="*20)



current_dir = os.path.dirname(os.path.abspath("C:/Users/Boss Hsu/Python_Code/Python_AOP_Library-main/AOP_Project_test/Test_project/Employees System Project/FrontendManager.py"))

print(current_dir)
# sys.path.append(current_dir)

# code = open("C:/Users/Boss Hsu/Python_Code/Python_AOP_Library-main/AOP_Project_test/Test_project/Employees System Project/Main.py", "r").read()
# weave_and_run(code)

# code = open("C:/Users/Boss Hsu/Python_Code/Python_AOP_Library-main/AOP_Project_test/Test_project/Employees System Project/Main.py", "r").read()

code = """
import requests
import logging

def fetch():
    r = requests.get('https://httpbin.org/get')
    print(r.status_code)

fetch()
print("Finish...")
"""

# print(code)

# tree = ast.parse(code)
# compiled = compile(tree, filename="<ast>", mode="exec")
# exec_globals = globals().copy()
# exec_globals["__name__"] = "__main__"
# exec(compiled, exec_globals)


# source_tree = ast.parse(code)
# compile_code = compile(source_tree, filename="<ast>", mode="exec")

# exec(compile_code, globals())

# exec_globals = globals().copy()
# exec_globals["__name__"] = "__main__"
# exec(compile_code, exec_globals)