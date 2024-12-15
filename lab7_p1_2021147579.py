import re

def parse_funcdecl(file):
    pattern = r"^\s*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\("
    funcdecl = []
    with open(file, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            match = re.match(pattern, line)
            if match:
                function_name = match.group(1)
                funcdecl.append((function_name, line_number))
    return funcdecl

def parse_funccalls(file, function_names, funcdecls):
    decl_lines = {name: line for name, line in funcdecls}
    funccalls = {name: [] for name in function_names}
    call_pattern = r"([a-zA-Z_][a-zA-Z0-9_]*)\s*\("
    with open(file, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            matches = re.findall(call_pattern, line)
            unique_matches = set(matches)
            for match in unique_matches:
                if match in function_names and line_number != decl_lines[match]:
                    funccalls[match].append(line_number)   
    return funccalls

if __name__ == "__main__":
    filename = "input_7_1.txt"
    funcdecls = parse_funcdecl(filename)
    funcdeclseq = [decl[0] for decl in funcdecls]
    funccalls = parse_funccalls(filename, funcdeclseq, funcdecls)
    for i in range(len(funccalls)):
        func_name, decl_line = funcdecls[i]
        calls = funccalls.get(func_name, [])
        calls_str = ", ".join(map(str, calls)) if calls else "none"
        print(f"{func_name}: def in {decl_line}, calls in [{calls_str}]")