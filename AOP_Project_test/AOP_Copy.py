import ast
import autopep8
import inspect
from PatternSyntax import Pattern_Syntax_Process

function_setting_array = []
before_log = []
after_log = []
around_log = []

compile_code = ""

def set_node_lineno(node, lineno, col_offset=0):
    node.lineno = lineno
    node.col_offset = col_offset
    return node

class Pointcut_Visitor(ast.NodeVisitor):
    target_function = ""

    def set_target_function(self, target_function):
        self.target_function = target_function

    def visit_ClassDef(self, node):
        if self.target_function == node.name:
            print("=================================================== Class Information ===================================================")
            print("Node class name:", node.name)

            for class_body in node.body:
                print("Node class function name:", class_body.name)
                if class_body.name not in function_setting_array:
                    function_setting_array.append(class_body.name)

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if self.target_function == node.name:
            print("=================================================== Function Information ===================================================")
            print("Node function name:", node.name)
            if node.name not in function_setting_array:
                function_setting_array.append(node.name)

        self.generic_visit(node)

class Aspect_Visitor(ast.NodeVisitor):
    pointcut_define = ""

    def set_target(self, pointcut_define):
        print("Setting Aspect_Visitor target...")
        self.pointcut_define = pointcut_define

    def visit_FunctionDef(self, node):
        print("=================================================== Aspect Function Information ===================================================")
        print("Node args: ", len(node.args.args))
        for node_info in node.body:
            print("Node Information: ", node_info)
            if type(node_info) == ast.Expr and (before_log == [] or after_log == []):
                print()
                print("Function information: ", ast.dump(node_info.value, indent=4))
                print()
                print("AST Information: ", ast.dump(node_info, indent=4))
                print()

                if len(node.args.args) > 0:
                    ast_args = []
                    for i in range(len(node.args.args)):
                        ast_args.append(ast.Constant(value=node.name))
                    aspect_ast = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id=node.name, ctx=ast.Load()),
                            args=ast_args,
                            keywords=[]
                        )
                    )
                else:
                    aspect_ast = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id=node.name, ctx=ast.Load()),
                            args=[],
                            keywords=[]
                        )
                    )

                print("Aspect AST....", ast.dump(aspect_ast, indent=4))
                print()

                if self.pointcut_define == "Before":
                    before_log.append(set_node_lineno(aspect_ast, node.lineno))
                elif self.pointcut_define == "After":
                    after_log.append(set_node_lineno(aspect_ast, node.lineno))
                elif self.pointcut_define == "Around":
                    around_log.append(set_node_lineno(aspect_ast, node.lineno))
                    print("========================= Around log =================================")
                    print(around_log)


        self.generic_visit(node)

class AOPTransformer(ast.NodeTransformer):
    target_class = ""
    target_function = ""
    pointcut_define = ""
    has_return = False

    def set_target(self, target_class, target_function, pointcut_define):
        print("Setting target...")
        self.target_class = target_class
        self.target_function = target_function
        self.pointcut_define = pointcut_define

    def insert_exit_print_in_returns(self, body, advice_ast):
        """在所有 return 前插入 exit print"""
        new_body = []
        for stmt in body:
            if isinstance(stmt, ast.Return):
                new_body.append(advice_ast)  # 先插入 print
                self.has_return = True
            elif isinstance(stmt, ast.If):  
                # 遞迴處理 if 內的 return
                stmt.body = self.insert_exit_print_in_returns(stmt.body, advice_ast)
                stmt.orelse = self.insert_exit_print_in_returns(stmt.orelse, advice_ast)
            new_body.append(stmt)
        return new_body
    
    def setting_Advice_through_Pointcut(self, node):
        for target_function in self.target_function:
            if target_function == node.name:
                if self.pointcut_define == "Before":
                    if not node.body:
                        node.body.append(ast.Pass())
                    else:
                        node.body.insert(0, before_log[0])
                elif self.pointcut_define == "After":
                    if not node.body:
                        node.body.append(ast.Pass())
                    
                    print("insert_exit_print_in_returns calling...")
                    node.body = self.insert_exit_print_in_returns(node.body, after_log[0])

                    # if not any(isinstance(stmt, ast.Return) for stmt in node.body) and (node.body[-1] != after_log[0]):
                    #     print("there are not ast.Return finding...")
                    #     node.body.append(after_log[0])
                    if not self.has_return:
                        print("there are not ast.Return finding...")
                        node.body.append(after_log[0])

                # TODO
                elif self.pointcut_define == "Around":
                    print("Applying Around logic...")
                    print(node.name)
                    original_func_name = node.name

                    for around in around_log:
                        print("======================================= Around Log AST =========================================")
                        print(ast.dump(around, indent=4))
                    # # 將原本邏輯包成一個內部函式 __original_func
                    # inner_func = ast.FunctionDef(
                    #     name=original_func_name,
                    #     args=node.args,
                    #     body=node.body,
                    #     decorator_list=[],
                    #     returns=node.returns,
                    #     type_comment=None
                    # )

                    # print("===== inner function ======")
                    # print(ast.dump(inner_func, indent=4))

                    # call_original = ast.Assign(
                    #     targets=[ast.Name(id='result', ctx=ast.Store())],
                    #     value=ast.Call(
                    #         func=ast.Name(id=original_func_name, ctx=ast.Load()),
                    #         args=[ast.Name(id=arg.arg, ctx=ast.Load()) for arg in node.args.args],
                    #         keywords=[]
                    #     )
                    # )

                    # print("===== call original function ======")
                    # print(ast.dump(call_original, indent=4))

                    # return_stmt = ast.Return(value=ast.Name(id='result', ctx=ast.Load()))

                    # # Step 3: 呼叫 logAround(__original_foo, a, b, ...)
                    # arg_names = [ast.Name(id=arg.arg, ctx=ast.Load()) for arg in node.args.args]

                    # call_logAround = ast.Call(
                    #     func=ast.Name(id=around_log[0].value.func.id, ctx=ast.Load()),
                    #     args=[ast.Name(id=original_func_name, ctx=ast.Load())] + arg_names,
                    #     keywords=[]
                    # )

                    # return_stmt = ast.Return(value=call_logAround)

                    # # Step 4: 重寫原函式主體
                    # node.body = [inner_func, return_stmt]
                    
                    # print(ast.dump(around_log, indent=4))
                    # if not node.body:
                    #     node.body.append(ast.Pass())
                    
                    # print("insert_exit_print_in_returns calling...")
                    # node.body = self.insert_exit_print_in_returns(node.body, after_log[0])

                    # # if not any(isinstance(stmt, ast.Return) for stmt in node.body) and (node.body[-1] != after_log[0]):
                    # #     print("there are not ast.Return finding...")
                    # #     node.body.append(after_log[0])
                    # if not self.has_return:
                    #     print("there are not ast.Return finding...")
                    #     node.body.append(after_log[0])
        
        self.has_return = False
        return node
    
    def visit_ClassDef(self, node):
        print("Target class: " + self.target_class)
        if self.target_class == node.name:
            print("Find...")
            for class_function in node.body:
                print("Class node function...", class_function.name)
                node = self.setting_Advice_through_Pointcut(node)
                                
                print("=================================================== Function Name ===================================================")
                print("Node name: " + class_function.name)
                print("=================================================== Node AST Information ===================================================")
                print("Node Information: " + ast.dump(class_function, indent=4))

        elif self.target_class != "" and len(node.body) != 0 and all(isinstance(class_function, ast.FunctionDef) for class_function in node.body):
            print("Test node body:", node.body)
            for class_function in node.body:
                print("Class node function...", class_function.name)
                node = self.setting_Advice_through_Pointcut(node)

                print("=================================================== Function Name ===================================================")
                print("Node name: " + class_function.name)
                print("=================================================== Node AST Information ===================================================")
                print("Node Information: " + ast.dump(class_function, indent=4))

        return self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        node = self.setting_Advice_through_Pointcut(node)
        return self.generic_visit(node)
    
class AST_Process:
    source_tree = ""
    before_advice_tree = ""
    after_advice_tree = ""
    around_advice_tree = ""
    target_function = ""

    pointcut_visit = Pointcut_Visitor()
    visit_before = Aspect_Visitor()
    visit_after = Aspect_Visitor()
    visit_around = Aspect_Visitor()
    transformer = AOPTransformer()

    combined_tree = ""

    def Execution(self):
        # 為每個節點設置必要的行號（如果需要的話）
        ast.fix_missing_locations(self.combined_tree)
        print("=================================================== Combine Code In AST ===================================================")
        print(ast.dump(self.combined_tree, indent=4))
        print("=================================================== AST Convert To Code ===================================================")
        #print(ast.unparse(combined_tree))
        # 編譯並執行修改後的代碼

        print(ast.unparse(self.combined_tree))

        print("=================================================== Compile ===================================================")
        compile_code = compile(self.combined_tree, filename="<ast>", mode="exec")
        #print(compile_code)
        return compile_code


    def Pointcut_Process(self, Filepath, Function):
        print("Filepath: ", Filepath)
        code = open(Filepath, "r").read()
        self.source_tree = ast.parse(code)
        self.target_function = Function

        self.pointcut_visit.set_target_function(Function)
        print("=================================================== Source Code AST ===================================================")
        print(ast.dump(self.source_tree, indent=4))

        self.pointcut_visit.generic_visit(self.source_tree)

    def Before_Advice_Process(self, Advice_code):
        self.before_advice_tree = ast.parse(Advice_code)
        print("=================================================== Advice Code AST ===================================================")
        print(ast.dump(self.before_advice_tree, indent=4))

        self.visit_before.set_target("Before")
        self.visit_before.generic_visit(self.before_advice_tree)


        self.transformer.set_target(self.target_function, function_setting_array, "Before")
        if self.combined_tree == "":
            transformed_tree = self.transformer.visit(self.source_tree)
        else:
            transformed_tree = self.transformer.visit(self.combined_tree)

        self.combined_tree = ast.Module(body=self.before_advice_tree.body + transformed_tree.body, type_ignores=[])
        global before_log
        before_log = []

    def After_Advice_Process(self, Advice_code):
        self.after_advice_tree = ast.parse(Advice_code)
        print("=================================================== Advice Code AST ===================================================")
        print(ast.dump(self.after_advice_tree, indent=4))

        self.visit_after.set_target("After")
        self.visit_after.generic_visit(self.after_advice_tree)

        self.transformer.set_target(self.target_function, function_setting_array, "After")
        if self.combined_tree == "":
            transformed_tree = self.transformer.visit(self.source_tree)
        else:
            transformed_tree = self.transformer.visit(self.combined_tree)

        self.combined_tree = ast.Module(body=self.after_advice_tree.body + transformed_tree.body, type_ignores=[])
        global after_log 
        after_log = []

    # TODO
    def Around_Advice_Process(self, Advice_code):
        self.around_advice_tree = ast.parse(Advice_code)
        print("=================================================== Advice Code AST ===================================================")
        print(ast.dump(self.around_advice_tree, indent=4))

        self.visit_around.set_target("Around")
        self.visit_around.generic_visit(self.around_advice_tree)

        self.transformer.set_target(self.target_function, function_setting_array, "Around")
        if self.combined_tree == "":
            transformed_tree = self.transformer.visit(self.source_tree)
        else:
            transformed_tree = self.transformer.visit(self.combined_tree)

        self.combined_tree = ast.Module(body=self.around_advice_tree.body + transformed_tree.body, type_ignores=[])
        global after_log 
        after_log = []

ast_tree = AST_Process()

# Indenting advice code
def Code_Process(code):
    advice_code = inspect.getsource(code)
    lines = advice_code.split('\n')
    advice_code = '\n'.join(lines[1:])
    return autopep8.fix_code(advice_code)


def Aspect(cls):
    print(f"Catch class: {cls.__name__}...")
    compile_code = Weaver(cls())
    print("Code: ", compile_code)
    exec(compile_code, globals())

    return cls

# def Pointcut(Joinpoint, Pattern, Filepath, Function):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"Function name: {func.__name__}")
#             print(f"Joinpoint type: {Joinpoint}")
#             print(f"Pattern: {Pattern}")
#             print(f"Filepath: {Filepath}")
#             print(f"Function: {Function}")

#             ast_tree.Pointcut_Process(Filepath, Function)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

def Pointcut(Joinpoint, Pattern):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Function name: {func.__name__}")
            print(f"Joinpoint type: {Joinpoint}")
            pattern_syntax = Pattern_Syntax_Process(Pattern)
            print("Pattern syntax: ", pattern_syntax)

            ast_tree.Pointcut_Process(pattern_syntax.get("Filepath"), pattern_syntax.get("Function"))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def Before(param_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 呼叫傳入的函數參數
            result = param_func(*args, **kwargs)
            print(f"Function {func.__name__} is being called.")

            advice_code = Code_Process(func)

            print("========================================== Advice code ==========================================")
            print(advice_code)
            ast_tree.Before_Advice_Process(advice_code)

            #result = func()

            # 呼叫原始被裝飾的函數
            # return func
            return ast_tree.Execution()
        return wrapper
    return decorator

def After(param_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 呼叫傳入的函數參數
            result = param_func(*args, **kwargs)
            print(f"Function {func.__name__} is being called.")

            advice_code = Code_Process(func)

            print("========================================== Advice code ==========================================")
            print(advice_code)
            ast_tree.After_Advice_Process(advice_code)

            #result = func()

            # 呼叫原始被裝飾的函數
            # return func
            return ast_tree.Execution()
        return wrapper
    return decorator

# TODO
def Around(param_func):
    def decorator(func):
        def wrapper(*args, **kwargs):

            print("======================================= Around =================================================")
            # 呼叫傳入的函數參數
            result = param_func(*args, **kwargs)
            print(f"Function {func.__name__} is being called.")

            advice_code = Code_Process(func)

            print("========================================== Advice code ==========================================")
            print(advice_code)
            ast_tree.Around_Advice_Process(advice_code)

            result = func()

            # 呼叫原始被裝飾的函數
            # return func
            ##return ast_tree.Execution()
        return wrapper
    return decorator

def Weaver(Aspect):
    attributes = dir(Aspect)
    functions = [attr for attr in attributes if callable(getattr(Aspect, attr)) and not attr.startswith("__")]
    for func_name in functions:
        print(f"Function Name Calling By Weaver Function: {func_name}")
        func = getattr(Aspect, func_name)
        code = func()

    return code