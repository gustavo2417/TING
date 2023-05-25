def exists_word(word, instance):
    result = []
    index = 1

    for i in instance.queue:
        my_dict = {
                    "palavra": word,
                    "arquivo": i["nome_do_arquivo"],
                    "ocorrencias": []
                }

        for line in i["linhas_do_arquivo"]:
            if word in line.lower():
                my_dict["ocorrencias"].append(
                        {
                            "linha": index
                         }
                    )
                index += 1

            else:
                index += 1

        if len(my_dict["ocorrencias"]) != 0:
            result.append(my_dict)

        return result


def search_by_word(word, instance):
    result = []
    index = 1

    for i in instance.queue:
        my_dict = {
                    "palavra": word,
                    "arquivo": i["nome_do_arquivo"],
                    "ocorrencias": []
                }

        for line in i["linhas_do_arquivo"]:
            if word in line.lower():
                my_dict["ocorrencias"].append(
                        {
                            "linha": index,
                            "conteudo": line
                         }
                    )
                index += 1

            else:
                index += 1

        if len(my_dict["ocorrencias"]) != 0:
            result.append(my_dict)

        return result
