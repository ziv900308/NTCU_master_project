import os

def parse_aspectj_expression(expr):
    expr = expr.strip()

    # Step 1: 去掉括號與多餘空格
    if expr.endswith("(..)"):
        expr = expr[:-4].strip()

    # Step 2: 拆分空格
    parts = expr.split()

    if len(parts) != 2:
        raise ValueError("不合法的 AspectJ 表示式格式")

    return_type, full_path = parts

    # Step 3: 拆分 module 與 class/method
    path_parts = full_path.split('.')
    print("Path_parts = ", path_parts)

    # 假設最後一段是 method/class pattern（*）
    if path_parts[-1] == "*":
        method_pattern = "*"
        class_path = ".".join(path_parts[:-1])
    else:
        method_pattern = path_parts[-1]
        class_path = ".".join(path_parts[:-1])

    if method_pattern == '*':
        method_pattern = class_path.split('.')[-1]
        print("############################", method_pattern)
        print("############################", class_path)

        if len(class_path.split('.')) == 2: 
            class_path = class_path +'.py'

        else:
            class_path = '.'.join(class_path.split('.')[:-1]) +'.py'

        print("############################qweqwe", class_path)

        #class_path = class_path.replace(method_pattern, 'py')
        print("############################", class_path)
        class_path = class_path.replace('.', '\\', 1)
        print("############################", class_path)

        # class_path = class_path.replace(method_pattern, 'py')
        # print("############################", class_path)
        # class_path = class_path.replace('.', '\\', 1)
        # print("############################", class_path)
    else:
        remove_function = class_path.split('.')[-1]
        if len(class_path.split('.')) == 2: 
            class_path = class_path +'.py'

        else:
            class_path = '.'.join(class_path.split('.')[:-1]) +'.py'
        #class_path = class_path.replace(remove_function, 'py')
        class_path = class_path.replace('.', '\\', 1)

    if method_pattern != "":
        return {
            "return_type": return_type,
            "package_path": class_path,
            "method_pattern": method_pattern,
            "pattern": 'MethodPattern'
        }

def Pattern_Syntax_Process(expr):
    parsed = parse_aspectj_expression(expr)
    print(parsed)
    Filepath = os.getcwd()+'\\'+parsed.get("package_path")
    Filepath = Filepath.replace('\\', '/')
    print("Filepath: ", Filepath)
    
    return {
        "Filepath": Filepath,
        "Function": parsed.get("method_pattern"),
        "Pattern": parsed.get("pattern")
    }



# # === 測試 ===
# expr = "* AOP_Project_test.app.Service.*(..)"
# Pattern_Syntax_Process("* Create_a_simple_stopwatch.stopwatch.*(..)")

# Only Method Pattern, need to extend function and modify...
# Need to added error exception (Can't find the target path)



