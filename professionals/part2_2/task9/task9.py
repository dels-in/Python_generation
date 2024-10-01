with open("files.txt") as file:
    lines = [line.split() for line in file.read().splitlines()]
    translation = {"B": lambda x: x, "KB": lambda x: x * 1024, "MB": lambda x: x * 1024 ** 2,
                   "GB": lambda x: x * 1024 ** 3}
    groups = {}
    for line in lines:
        full_name, size, measurement = line
        name, extension = full_name.split(".")
        extension = "." + extension
        bytes = translation[measurement](int(size))
        groups.setdefault(extension, []).append((full_name, bytes))

    for key, value in sorted(groups.items()):
        summary = 0
        for full_name, bytes in sorted(value):
            summary += bytes
            print(full_name)
        print("----------")

        summary //= 1024
        measurement = "KB"
        if summary >= 1024:
            summary = round(summary / 1024)
            measurement = "MB"
            if summary >= 1024:
                summary = round(summary / 1024)
                measurement = "GB"
        print(f"Summary: {summary} {measurement}\n")

