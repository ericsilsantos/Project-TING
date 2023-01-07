def exists_word(word, instance):
    info_founded = list()
    info_location = list()

    for index in range(len(instance)):
        arq = instance.search(index)
        line = arq['linhas_do_arquivo']
        for index in range(len(line)):
            if word.lower() in line[index].lower():
                info_founded.append({'linha': index + 1})

        if len(info_founded) >= 1:
            info_location.append({
                'palavra': word,
                'arquivo': arq['nome_do_arquivo'],
                'ocorrencias': info_founded
            })

    return info_location


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
