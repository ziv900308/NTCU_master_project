import os

def parse_aspectj_expression(expr):

    # Remove ' ' or '\n' from string (first and last)
    expr = expr.strip()
    if expr.endswith("(..)"):
        expr = expr[:-4].strip()

    parts = expr.split('.')
    # print("Parts: ", parts)

    # Not support multiple layer package...
    # Not support all function without class...
    if len(parts) == 3:
        directory, module, target_function = parts
        classname = None
        directory = directory.removeprefix("* ")
        # print("Dir: ", directory)
    elif len(parts) == 4:
        directory, module, classname, target_function = parts
        directory = directory.removeprefix("* ")
        # print("Dir: ", directory)
    else:
        raise ValueError("不合法的 AspectJ 表示式格式")
    

    if target_function == "*":
        method_pattern = classname # * only support all function in class
    else:
        method_pattern = target_function

    class_path = ".".join([directory, module]).replace('.', '\\', 1) +'.py'
    # print("Class path: " + class_path)
    # print("Method_Pattern: " + method_pattern)

    return{
            "package_path": class_path,
            "class_name": classname,
            "module": module,
            "method_pattern": method_pattern,
            "pattern": 'MethodPattern'
    }

def Pattern_Syntax_Process(expr):
    print("="*100)

    parsed = parse_aspectj_expression(expr)
    print(parsed)
    Filepath = os.getcwd()+'\\'+parsed.get("package_path")
    Filepath = Filepath.replace('\\', '/')
    print("Filepath: ", Filepath)

    print("="*100)
    
    return {
        "Filepath": Filepath,
        "Function": parsed.get("method_pattern"),
        "Pattern": parsed.get("pattern"),
        "Module": parsed.get("module"),
        "class_name": parsed.get("class_name")
    }



# Pattern_Syntax_Process("* Billing_system.biling_system.Bill_App.*(..)")
# Pattern_Syntax_Process("* Employees System Project.Employee.Employee.*(..)")
# Pattern_Syntax_Process("* Countdown_timer.main.countdown")
# Pattern_Syntax_Process("* Employees System Project.FrontendManager.FrontendManager.print_menu")



# def parse_aspectj_expression(expr):
#     expr = expr.strip()
#     print("Expr: ", expr)

#     # Step 1: 去掉括號與多餘空格
#     if expr.endswith("(..)"):
#         expr = expr[:-4].strip()

#     # Step 2: 拆分空格
#     parts = expr.split()

#     if len(parts) != 2:
#         raise ValueError("不合法的 AspectJ 表示式格式")

#     return_type, full_path = parts

#     # Step 3: 拆分 module 與 class/method
#     path_parts = full_path.split('.')
#     print("Path_parts = ", path_parts)

#     # 假設最後一段是 method/class pattern（*）
#     if path_parts[-1] == "*":
#         method_pattern = "*"
#         class_path = ".".join(path_parts[:-1])
#         print(path_parts[:-1])
#         print("Thus, class_path = " + class_path)
#     else:
#         method_pattern = path_parts[-1]
#         class_path = ".".join(path_parts[:-1])

#     if method_pattern == '*':
#         method_pattern = class_path.split('.')[-1]
#         print("############################", method_pattern)
#         print("############################", class_path)

#         if len(class_path.split('.')) == 2: 
#             class_path = class_path +'.py'

#         else:
#             class_path = '.'.join(class_path.split('.')[:-1]) +'.py'

#         print("############################qweqwe", class_path)

#         #class_path = class_path.replace(method_pattern, 'py')
#         print("############################", class_path)
#         class_path = class_path.replace('.', '\\', 1)
#         print("############################", class_path)

#         # class_path = class_path.replace(method_pattern, 'py')
#         # print("############################", class_path)
#         # class_path = class_path.replace('.', '\\', 1)
#         # print("############################", class_path)
#     else:
#         remove_function = class_path.split('.')[-1]
#         if len(class_path.split('.')) == 2: 
#             class_path = class_path +'.py'

#         else:
#             class_path = '.'.join(class_path.split('.')[:-1]) +'.py'
#         #class_path = class_path.replace(remove_function, 'py')
#         class_path = class_path.replace('.', '\\', 1)

#     if method_pattern != "":
#         return {
#             "return_type": return_type,
#             "package_path": class_path,
#             "method_pattern": method_pattern,
#             "pattern": 'MethodPattern'
#         }

# def Pattern_Syntax_Process(expr):
#     parsed = parse_aspectj_expression(expr)
#     print(parsed)
#     Filepath = os.getcwd()+'\\'+parsed.get("package_path")
#     Filepath = Filepath.replace('\\', '/')
#     print("Filepath: ", Filepath)
    
#     return {
#         "Filepath": Filepath,
#         "Function": parsed.get("method_pattern"),
#         "Pattern": parsed.get("pattern")
#     }

# Pattern_Syntax_Process("* Employees System Project.Employee.Employee.*(..)")
# Pattern_Syntax_Process("* Countdown_timer.main.countdown")
# Pattern_Syntax_Process("* Employees System Project.FrontendManager.FrontendManager.print_menu")





# "* Employees System Project.Employee.Employee.(..)" (directory/.py/class or function)
# "* Employees System Project.Employee.FrontendManager.print_menu" (dirctory/.py file/class/function)

# # === 測試 ===
# expr = "* AOP_Project_test.app.Service.*(..)"
# Pattern_Syntax_Process("* Create_a_simple_stopwatch.stopwatch.*(..)")

# Only Method Pattern, need to extend function and modify...
# Need to added error exception (Can't find the target path)