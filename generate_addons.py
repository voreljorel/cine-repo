import os
import hashlib

REPO_DIR = '.'  # aktuální složka
EXCLUDE = ['repository.cinemakitty']  # repozitář samotný se nebere jako doplněk

def get_addon_xmls():
    addon_xmls = []
    for folder in os.listdir(REPO_DIR):
        folder_path = os.path.join(REPO_DIR, folder)
        if os.path.isdir(folder_path) and folder not in EXCLUDE:
            addon_xml = os.path.join(folder_path, 'addon.xml')
            if os.path.exists(addon_xml):
                with open(addon_xml, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    addon_xmls.append(content)
    return addon_xmls

def write_addons_xml(addons):
    output = '<?xml version="1.0" encoding="UTF-8"?>\n<addons>\n'
    for addon in addons:
        output += addon + '\n'
    output += '</addons>\n'
    with open('addons.xml', 'w', encoding='utf-8') as f:
        f.write(output)
    return output

def write_md5(content):
    md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
    with open('addons.xml.md5', 'w') as f:
        f.write(md5)

if __name__ == '__main__':
    addon_xmls = get_addon_xmls()
    addons_content = write_addons_xml(addon_xmls)
    write_md5(addons_content)
    print('✅ addons.xml a addons.xml.md5 byly vygenerovány.')