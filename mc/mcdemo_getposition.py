#A Miciche
#mcdemo get position

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.getPos()

pos = mc.player.getPos()
mc.postToChat(pos)
mc.postToChat("Your X position: " + str(pos.x))
mc.postToChat("Your Y position: " + str(pos.y))
mc.postToChat("Your Z position: " + str(pos.z))