import os

def list_files_and_write(directory: str, output_file: str) -> None:
    with open(output_file, mode="w", encoding="utf-8") as out:
        for root, _, files in os.walk(codeRelativePath + directory):
            for filename in files:
                if check_directory(root) and check_file(filename):
                    full_path: str = os.path.join(root, filename)
                    rel_path: str = os.path.relpath(full_path, start=codeRelativePath)
                    out.write(formatter(rel_path, to_language(filename)) + "\n")

codeRelativePath: str = "../EEETWV/EasonEetwViewer/"

projects: list[tuple[str, str]]= [
    ("EasonEetwViewer", "gui"),
    ("EasonEetwViewer.Services.Kmoni", "kmoni-settings"),
    ("EasonEetwViewer.Dmdata.Api", "dmdata-api"),
    ("EasonEetwViewer.Dmdata.Authentication", "dmdata-auth"),
    ("EasonEetwViewer.Dmdata.Dtos", "dmdata-dtos"),
    ("EasonEetwViewer.Dmdata.Telegram", "dmdata-telegram"),
    ("EasonEetwViewer.Dmdata.WebSocket", "dmdata-websocket"),
    ("EasonEetwViewer.JmaTravelTime", "jma-travel-time"),
    ("EasonEetwViewer.KyoshinMonitor", "kyoshin-monitor"),
]

outputDir: str = "outputTex/"

def to_language(file: str) -> str:
    if file.endswith(".axaml") or file.endswith(".resx"):
        return "xml"
    elif file.endswith(".json"):
        return "json"
    elif file.endswith(".cs"):
        return "csharp"
    return "text"

def check_file(file: str) -> bool:
    return check_csharp(file) or file.endswith(".axaml") or file.endswith(".resx") or file.endswith("appsettings.json")

def check_directory(directory: str) -> bool:
    return "obj/" not in directory and "bin/" not in directory

def check_csharp(file: str) -> bool:
    return file.endswith(".cs") and not file.endswith("Designer.cs")

def formatter(dir: str, lang: str) -> str:
    return """\\begin{normallisting}
    \\inputminted{""" + lang + """}{\\CodeBasePath EasonEetwViewer/""" + dir + """}
    \\caption{\\Code{""" + dir + """}}
    \\label{code-listing:""" + dir + """}
\\end{normallisting}"""

if __name__ == "__main__":
    for project in projects:
        list_files_and_write(project[0], outputDir + project[1] + ".tex")