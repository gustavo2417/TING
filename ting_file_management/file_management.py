import sys


def txt_importer(path_file):
    if not path_file.endswith("txt"):
        return sys.stderr.write("Formato inválido")

    try:
        file = open(path_file, "r")
        content = file.read()

        result = content.split("\n")
        file.close()

        return result

    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
