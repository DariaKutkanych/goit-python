import os
import shutil


FOLDERS = ["images", "documents", "audio", "video", "archives", "others"]

folder_ext_dict = {"images": ["JPEG", "PNG", "JPG", "SVG"],
                   "documents": ["DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"],
                   "audio": ["MP3", "OGG", "WAV", "AMR"],
                   "video": ["AVI", "MP4", "MOV", "MKV"],
                   "archives": ["ZIP", "GZ", "TAR"],
                   "others": ["IPYNB"]}

cwd_path = os.getcwd()

for folder in FOLDERS:
    os.makedirs(f"{cwd_path}/{folder}", exist_ok=True)


def normalize(name):

    cyrillic = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к',
                'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    latin = ['a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i', 'yi', 'y', 'k', 'l', 'm',
             'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'yu', 'ya']

    name = "".join([x if x.isalnum() or x == "." else "_" for x in name])

    mytable = {ord(cyr): lat for cyr, lat in zip(cyrillic, latin)}
    mytable.update({ord(cyr.upper()): lat.upper()
                   for cyr, lat in zip(cyrillic, latin)})  # added uppercase letters to the dict

    result = name.translate(mytable)

    return result


def sort_docs(path):

    for item in os.listdir(path):

        if os.path.isdir(item):
            sort_docs(f"{path}/{item}")

        elif os.path.isfile(item):

            print(type(item))
            file_name, file_type = item.split(".")
            folder_to_move = "others"

            for k, v in folder_ext_dict.items():
                if file_type.upper() in folder_ext_dict.get(k):
                    folder_to_move = k
                    break

            os.rename(f"{path}/{item}", f"{path}/{folder_to_move}/{item}")


sort_docs(cwd_path)
