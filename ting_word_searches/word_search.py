def exists_word(word, instance):
    founded = list()
    location = list()

    for index in range(len(instance)):
        arq = instance.search(index)
        line = arq['linhas_do_arquivo']
        for index in range(len(line)):
            if word.lower() in line[index].lower():
                founded.append({'linha': index + 1})

        if len(founded) >= 1:
            location.append({
                'palavra': word,
                'arquivo': arq['nome_do_arquivo'],
                'ocorrencias': founded,
            })

    return location


def search_by_word(word, instance):
    founded = list()
    location = list()

    for index in range(len(instance)):
        arq = instance.search(index)
        line = arq['linhas_do_arquivo']
        for index, row in enumerate(line):
            if word.lower() in row.lower():
                founded.append({
                    'linha': index + 1,
                    'conteudo': line[index],
                    })

        if len(founded) >= 1:
            location.append({
                'palavra': word,
                'arquivo': arq['nome_do_arquivo'],
                'ocorrencias': founded,
            })

    return location
