import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in instance.queue:
        if i["nome_do_arquivo"] == path_file:
            return None

    list_of_lines = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_of_lines),
        "linhas_do_arquivo": list_of_lines
    }

    instance.enqueue(result)

    return print(result, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)

    name_of_file = instance.queue[0]["nome_do_arquivo"]

    instance.dequeue()

    return print(f"Arquivo {name_of_file} removido com sucesso")


def file_metadata(instance, position):
    if position > len(instance.queue) or position < 0:
        return print("Posição inválida", file=sys.stderr)

    result = instance.search(position)

    return print(result, file=sys.stdout)
