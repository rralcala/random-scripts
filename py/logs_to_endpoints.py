tokens = set()
method_mapping = {}


for line in open("./logs_endpoints_map.in"):
    request, method = line.strip().split(",")
    verb, path = request.split(" ")
    path_parts = path.split("/")
    for i in range(len(path_parts)):
        if path_parts[i].startswith("<"):
            path_parts[i] = "<>"
        else:
            tokens.add(path_parts[i])
    method_mapping[verb + "/".join(path_parts)] = method.strip()


method_count = {}
for line in open("./logs_to_endpoints.in"):
    verb, path = line.split(" ")
    parsed_path = verb
    for token in path.split("/")[1:]:
        token = token.strip()
        if token in tokens:
            parsed_path += "/" + token
        else:
            parsed_path += "/<>"
    method_count.setdefault(method_mapping[parsed_path], 0)
    method_count[method_mapping[parsed_path]] += 1


print(tokens)
print(method_count)
