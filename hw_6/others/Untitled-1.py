def normalize(name):

    cyrillic = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    latin = ['a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i', 'yi', 'y', 'k', 'l', 'm',
             'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'yu', 'ya']

    # all spaces and other chars replaced with "_"
    name = "".join([x if x.isalnum() or x == "." else "_" for x in name])

    mytable = {ord(cyr): lat for cyr, lat in zip(cyrillic, latin)}
    mytable.update({ord(cyr.upper()): lat.upper()
                   for cyr, lat in zip(cyrillic, latin)})  # added uppercase letters to the dict

    result = name.translate(mytable)

    return result


print(normalize("Даша Губе)н'ко Василівн.шья"))
