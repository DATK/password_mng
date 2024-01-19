import hashlib


class Shifer:

    def __init__(self):
        pass

    def cezar(self, text, key):
        alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТ\ЬОГ>ШЩДЛБЮЖЗХЭЪjklm/nopqr stuvwxy'z1234567)89_йф0ячыц<увсмипакен|ртогшлб,юдщьзжэхъ*-+=&:;?!@"
        cezar_shifr = []
        for j in range(len(text)):
            for i in range(len(alf)):
                if text[j] == alf[i]:
                    if i + key > len(alf)-1:
                        cezar_shifr.append(text[j])
                    else:
                        cezar_shifr.append(alf[i + key])

        return ''.join(cezar_shifr)

    def uncezar(self, text, key):
        alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТ\ЬОГ>ШЩДЛБЮЖЗХЭЪjklm/nopqr stuvwxy'z1234567)89_йф0ячыц<увсмипакен|ртогшлб,юдщьзжэхъ*-+=&:;?!@"
        cezar_un = []
        for j in range(len(text)):
            for i in range(len(alf)):
                # print(i,j)
                if alf[i] == text[j]:
                    if i + key > len(alf)-1:
                        # print("          ",i,j)
                        cezar_un.append(text[j])
                    else:
                        # print("                          ",i,j)
                        cezar_un.append(alf[i - key])

        return ''.join(cezar_un)

    def hashing(self, txt: str):
        h = hashlib.sha256()
        h.update(bytes(txt, "utf8"))
        return h.hexdigest()
