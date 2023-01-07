from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    arq = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arq),
        "linhas_do_arquivo": arq,
    }

    for index in range(len(instance)):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            return None


    instance.enqueue(dict)
    sys.stdout.write(str(dict))

    return dict


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
