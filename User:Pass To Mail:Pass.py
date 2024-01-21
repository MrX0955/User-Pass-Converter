from time import sleep


class Settings:
    name = input(" [?] Combolist Name (Must be in the same folder) : ")
    if len(name) == 0:
        print(" Wrong Input the Combolist Name")
        sleep(1)
        exit()
    mrx = input(
        "[?] Mail Types --> [@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, "
        "@outlook.com.tr, @icloud.com, @edu.com] : ")
    if len(mrx) == 0:
        print(" Wrong Input the Mail Type")
        sleep(1)
        exit()
    izinli_karakterler = (
        '@gmail.com,@hotmail.com,@yahoo.com,@outlook.com, @yahoo.com.tr, @outlook.com.tr, @icloud.com, @edu.com ')


for mails in Settings.izinli_karakterler:
    if mails in Settings.mrx:
        print(" [+] Success.")
        break
    else:
        break

try:

    with open(Settings.name, errors="ignore", encoding="utf-8") as file:

        combolist = file.readlines()

        if len(combolist) > 0:

            savefile = open(f"{Settings.mrx}--pass.txt", "a")

            for combo in combolist:

                try:
                    user = combo.split("\n")[0].split(":")[0].strip() + Settings.mrx
                    password = combo.split("\n")[0].split(":")[1].strip()
                    savefile.write("{}:{}\n".format(user, password))
                except Exception:
                    pass
        else:
            print("Empty File...")
            sleep(1)
            exit()

except Exception:
    print("Can not find the file...")
    sleep(1)
    exit()
