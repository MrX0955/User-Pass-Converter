logo = f"""
   ___________                        __________                    _____                                            __           
   \_   _____/_______   ____    ____  \______   \_______   ____    /  _  \    ____    ____    ____   __ __   ____  _/  |_   ______
    |    __)  \_  __ \_/ __ \ _/ __ \  |     ___/\_  __ \_/ __ \  /  /_\  \ _/ ___\ _/ ___\  /  _ \ |  |  \ /    \ \   __\ /  ___/
    |     \    |  | \/\  ___/ \  ___/  |    |     |  | \/\  ___/ /    |    \\  \___ \  \___ (  <_> )|  |  /|   |  \ |  |   \___ \ 
    \___  /    |__|    \___  > \___  > |____|     |__|    \___  >\____|__  / \___  > \___  > \____/ |____/ |___|  / |__|  /____  >
        \/                 \/      \/                         \/         \/      \/      \/                     \/             \/ 
                                                                                 """
print("\n" + logo + "\n")

input(" [INFO] UYARI! MAIL TÜRÜ YAZARKEN [gmail ise @gmail.com] YAZMALISINIZ! DEVAM ETMEK İÇİN BİR TUŞA TIKLAYIN!")
name = input(" [?] Combonuzun İsmi (Aynı Klasörde Olmalıdır sonuna .txt ekleyin.) : ")
mrx = input(" [?] İstediğiniz mail türünü yazın. [@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, @outlook.com.tr, @icloud.com, @edu.com] : ")
izinli_karakterler = ('@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, @outlook.com.tr, @icloud.com, @edu.com ')

for mails in izinli_karakterler:
    if mails in mrx:
        print(" [+] Success. -->> [DefaceR]MrX ..! <<--")
        break
    else:
        print(" [-] What you looking? ")
        break

try:

    with open(name, errors="ignore", encoding="utf-8") as file:

        combolist = file.readlines()

        if len(combolist) > 0:

            savefile = open(f"{mrx}--pass.txt", "a")

            for combo in combolist:

                try:

                    user = combo.split("\n")[0].split(":")[0].strip() + mrx
                    password = combo.split("\n")[0].split(":")[1].strip()
                    savefile.write("{}:{}\n".format(user, password))

                except Exception:
                    pass
        else:
            input("Boş Dosya ...")

except Exception:
    input("Dosya Bulunamadı...")
