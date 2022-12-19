import pymem

dwEntityList = 0x4DFDE84
dwGlowObjectManager = 0x5358958
m_iGlowIndex = 0x10488

pm = pymem.Pymem("csgo.exe")
cliencatach = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

def main():
    glowmodule()

def glowmodule():
    while True:
        glow = pm.read_int(cliencatach + dwGlowObjectManager)

        for i in range(0, 32):
            entity = pm.read_int(cliencatach + dwEntityList + i *0x10)
            if entity:
                    entityglowing = pm.read_int(entity+m_iGlowIndex)

                    pm.write_float(glow + entityglowing * 0x38 + 0x8, float(0))
                    pm.write_float(glow + entityglowing * 0x38 + 0xC, float(1))
                    pm.write_float(glow + entityglowing * 0x38 + 0x10, float(0))
                    pm.write_float(glow + entityglowing * 0x38 + 0x14, float(1))
                    pm.write_int(glow + entityglowing * 0x38 + 0x28, 1)


if __name__ == '__main__':
    main()
