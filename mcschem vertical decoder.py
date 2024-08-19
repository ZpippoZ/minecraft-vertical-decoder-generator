import mcschematic
import time

schem = mcschematic.MCSchematic()

bits=int(input("Input the number of bits of the decoder: "))

for y in range(2**bits):
    for x in range(bits):
        value=list(bin(y)[2:].zfill(bits))
        schem.setBlock((x*2,y*2-2**bits*2,-1), "minecraft:red_stained_glass")
        schem.setBlock((x*2,y*2+1-2**bits*2,-2), "minecraft:red_stained_glass")
        schem.setBlock((x*2,y*2+1-2**bits*2,-1), "minecraft:redstone_wire")
        schem.setBlock((x*2,y*2-2**bits*2,-2), "minecraft:redstone_wire")
        schem.setBlock((x*2,y*2-2**bits*2,1), "minecraft:red_concrete")
        schem.setBlock((x*2-1,y*2-2**bits*2,1), "minecraft:red_concrete")
        schem.setBlock((x*2,y*2+1-2**bits*2,1), "minecraft:redstone_wire")
        schem.setBlock((x*2-1,y*2+1-2**bits*2,1), "minecraft:redstone_wire")

        if not y % 16 < 8:
            value[x] = str(0+(not int(value[x])))
        
        if value[x]=='0':
            schem.setBlock((x*2,y*2-2**bits*2,0), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**bits*2,0), "minecraft:repeater")
        if value[x]=='1':
            schem.setBlock((x*2,y*2+1-2**bits*2,0), "minecraft:red_concrete")
            schem.setBlock((x*2-1,y*2+1-2**bits*2,0),"minecraft:redstone_wall_torch[facing=west]")

        
        if not y%8 and y:
            schem.setBlock((x*2,y*2-2**bits*2,-3), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**bits*2,-3), "minecraft:redstone_torch")
            schem.setBlock((x*2,y*2+2-2**bits*2,-3), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**bits*2,-2), "minecraft:red_concrete")

        if not y:
            schem.setBlock((x*2,y*2-2**bits*2,-1), "minecraft:red_concrete")
            schem.setBlock((x*2,y*2+1-2**bits*2,-2), "minecraft:red_concrete")


for x in range(bits):
    schem.setBlock((x*2,-1,-2), "minecraft:air")
    

schem.save("C:/Users/zPippo/curseforge/minecraft/Instances/Redstone/config/worldedit/schematics", str(bits) + "bitVerticalDecoder", mcschematic.Version.JE_1_18_2)
print("Schematic saved")
time.sleep(5)