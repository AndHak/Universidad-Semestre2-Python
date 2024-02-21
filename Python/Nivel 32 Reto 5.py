palabras = ["isla","último","Ángela","Italia",
            "Índice","Íñigo","óptica","árbol",
            "Úrsula","época","Olmedo","Uruguay",
            "Elvira","ukelele","Argentina","Écija",
            "Óscar","amapola","elefante","objeto"]

palabras.sort(key=lambda p: p.lower().replace("á", "a"). \
              replace("é", "e").replace("í", "i"). \
                replace("ó", "o").replace("ú", "u"). \
                    replace("ñ", "nzz"))

print(palabras)

