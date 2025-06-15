import ast
import autopep8
import inspect
from PatternSyntax import Pattern_Syntax_Process
import textwrap

function_setting_array = []
before_advice = []
after_advice = []
around_advice = []

compile_code = ""

def set_node_lineno(node, lineno, col_offset=0):
    node.lineno = lineno
    node.col_offset = col_offset
    return node

class Pointcut_Visitor(ast.NodeVisitor):
    target_function = ""

    def set_target_function(self, target_function):
        print("+"*100)
        print("Pointcut_Visitor target_function: ", target_function)
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

    def Wrapper_Function_Writting(self, node):
        wrapper_func = ast.FunctionDef(
                name="wrapper",
                args=ast.arguments(
                    posonlyargs=[],
                    args=[],  # 不要把 *args, **kwargs 放這裡
                    vararg=ast.arg(arg='args'),       # <-- 正確放這裡
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=ast.arg(arg='kwargs'),      # <-- 正確放這裡
                    defaults=[]
                ),
                body=node.body,
                decorator_list=[]
                )
            
        node.body = [
                wrapper_func,
                ast.Return(value=ast.Name(id="wrapper", ctx=ast.Load()))
        ]
        ast.fix_missing_locations(node)

        print(ast.dump(node, indent=4))
        print("==================================================================================")
        print(ast.unparse(node))

        return node
    
    def Before_Advice_Setting(self, node):
        # Recording Advice name
        before_advice.append(node.name)
        
        print("=========================================== Target node_name ============================================")
        print(ast.dump(node, indent=4))
        print("=========================================== Modify ============================================")
        node.body.append(
            ast.Return(
                value=ast.Call(
                    func=ast.Name(id='func', ctx=ast.Load()),
                    args=[
                        ast.Starred(
                            value=ast.Name(id='args', ctx=ast.Load()),
                            ctx=ast.Load()
                        )
                    ],
                    keywords=[
                        ast.keyword(
                            arg=None,
                            value=ast.Name(id='kwargs', ctx=ast.Load())
                        )
                    ]
                )
            )
        )

        return self.Wrapper_Function_Writting(node)

    def After_Advice_Setting(self, node):
        # Recording Advice name
        after_advice.append(node.name)
        
        print("=========================================== Target node_name ============================================")
        print(ast.dump(node, indent=4))
        print("=========================================== Modify ============================================")
        node.body.insert(0, ast.Assign(
                    targets=[ast.Name(id='result', ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='func', ctx=ast.Load()),
                        args=[
                            ast.Starred(value=ast.Name(id='args', ctx=ast.Load()), ctx=ast.Load())
                        ],
                        keywords=[
                            ast.keyword(arg=None, value=ast.Name(id='kwargs', ctx=ast.Load()))
                        ]
                    )
                ))
        
        node.body.append(
            ast.Return(
                        value=ast.Name(id='result', ctx=ast.Load())
                    )
        )

        return self.Wrapper_Function_Writting(node)
    
    # TODO Afterreturn and AfterThrowing
    # def AfterReturn_Advice_Setting(self, node):
    #     # Recording Advice name
    #     after_advice.append(node.name)
        
    #     print("=========================================== Target node_name ============================================")
    #     print(ast.dump(node, indent=4))
    #     print("=========================================== Modify ============================================")
    #     node.body.insert(0, ast.Assign(
    #                 targets=[ast.Name(id='result', ctx=ast.Store())],
    #                 value=ast.Call(
    #                     func=ast.Name(id='func', ctx=ast.Load()),
    #                     args=[
    #                         ast.Starred(value=ast.Name(id='args', ctx=ast.Load()), ctx=ast.Load())
    #                     ],
    #                     keywords=[
    #                         ast.keyword(arg=None, value=ast.Name(id='kwargs', ctx=ast.Load()))
    #                     ]
    #                 )
    #             ))
        
    #     node.body.append(
    #         ast.Return(
    #                     value=ast.Name(id='result', ctx=ast.Load())
    #                 )
    #     )

        return self.Wrapper_Function_Writting(node)
    

    # def After_Advice_Setting(self, node):
    #     # Recording Advice name
    #     after_advice.append(node.name)
        
    #     print("=========================================== Target node_name ============================================")
    #     print(ast.dump(node, indent=4))
    #     print("=========================================== Modify ============================================")
    #     node.body.append(
    #         ast.Return(
    #                     value=ast.Name(id='result', ctx=ast.Load())
    #                 )
    #     )

    #     return self.Wrapper_Function_Writting(node)


    def Around_Advice_Setting(self, node):
        # Recording Advice name
            around_advice.append(node.name)
            # print("*************************************************************************************")
            # print(ast.dump(node, indent=4))
            # print(ast.unparse(node))
            # print("*************************************************************************************")

            for i in range(len(node.body)):
                # print("*************************************************************************************")
                # print(ast.dump(node.body[i], indent=4))
                # print("*************************************************************************************")
                # print()
                # print("*************************************************************************************")
                if (hasattr(node.body[i], 'value') and type(node.body[i].value) == ast.Call and node.body[i].value.func.id == "func"):
                    print("=========================================== Target node_name ============================================")
                    print("*************************************************************************************")
                    print(ast.dump(node.body[i], indent=4))
                    print("*************************************************************************************")
                    print("=========================================== Modify (Not arguments to override...) ============================================")
                    if node.body[i].value.args == []:
                        node.body[i] = ast.Assign(
                        targets=[ast.Name(id='result', ctx=ast.Store())],
                        value=ast.Call(
                            func=ast.Name(id='func', ctx=ast.Load()),
                            args=[
                                ast.Starred(value=ast.Name(id='args', ctx=ast.Load()), ctx=ast.Load())
                            ],
                            keywords=[
                                ast.keyword(arg=None, value=ast.Name(id='kwargs', ctx=ast.Load()))
                            ]
                        )
                    )
                    
                    # Override with argument
                    else:
                        node.body[i] = ast.Assign(
                        targets=[ast.Name(id='result', ctx=ast.Store())],
                        value=node.body[i].value
                    )

                    # Only run once!!
                    node.body.append(
                        ast.Return(
                                    value=ast.Name(id='result', ctx=ast.Load())
                                )
                    )
                
                else:
                    print("Not found...")
            
            print("============ NEW ============")
            
            if type(node.body[-1]) != ast.Return:
                node.body.append(
                        ast.Return(
                                    value=None
                                )
                    )
                
            
            return self.Wrapper_Function_Writting(node)

    def visit_FunctionDef(self, node):
        print("=================================================== Aspect Function Information ===================================================")
        if self.pointcut_define == "Before":
            return self.Before_Advice_Setting(node)
        elif self.pointcut_define == "After":
            return self.After_Advice_Setting(node)
        elif self.pointcut_define == "Around":
            return self.Around_Advice_Setting(node)

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

        print("Target class: ", target_class)
        print("Target function: ", target_function)
        print("Point define: ", pointcut_define)

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
                    print("Applying Before logic...")
                    print("================================================ Before logic AST ===========================================================")
                    print(ast.dump(node, indent=4))
                    print("================================================ Before source code ===========================================================")
                    print(ast.unparse(node))
                    # print(node.name)
                    # original_func_name = node.name

                    node.decorator_list.insert(
                            0,
                            ast.Name(id=before_advice[0], ctx=ast.Load()) ###
                        )
                    
                    print("======================================= Insert.... =========================================")
                    print(ast.unparse(node))

                elif self.pointcut_define == "After":
                    print("Applying After logic...")
                    print("================================================ After logic AST ===========================================================")
                    print(ast.dump(node, indent=4))
                    print("================================================ After source code ===========================================================")
                    print(ast.unparse(node))
                    # print(node.name)
                    # original_func_name = node.name

                    node.decorator_list.insert(
                            0,
                            ast.Name(id=after_advice[0], ctx=ast.Load()) ###
                        )
                    
                    print("======================================= Insert.... =========================================")
                    print(ast.unparse(node))

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

                # TODO
                elif self.pointcut_define == "Around":
                    print("Applying Around logic...")
                    print("================================================ Around logic AST ===========================================================")
                    print(ast.dump(node, indent=4))
                    print("================================================ Around source code ===========================================================")
                    print(ast.unparse(node))

                    node.decorator_list.insert(
                            0,
                            ast.Name(id=around_advice[0], ctx=ast.Load()) ###
                        )
                    
                    print("======================================= Insert.... =========================================")
                    print(ast.unparse(node))
        
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
        global before_advice
        before_advice = []

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
        global after_advice
        after_advice = []

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


        global around_advice 
        around_advice = []

ast_tree = AST_Process()

# Indenting advice code
def Code_Process(code):
    advice_code = inspect.getsource(code)
    lines = advice_code.split('\n')
    advice_code = '\n'.join(lines[1:])
    advice_code = textwrap.dedent(advice_code)
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

#TODO class name need to be added
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

            #result = func()

            # 呼叫原始被裝飾的函數
            # return func
            return ast_tree.Execution()
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

# Problem:
# 1. Weaver(): Need to modify (func need target to execution)
# 2. Before、After、Around... multiple advice method need to implement
# 3. Around implement...

# # Problem:
# # 1. Weaver(): Need to modify (func need target to execution)
# # 2. Before、After、Around... multiple advice method need to implement
# # 3. Around implement...

#TODO
# Pattern Syntax need to catch specific class method