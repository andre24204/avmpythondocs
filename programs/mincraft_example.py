#A Miciche
#Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.getTilePos()

playerPosition = mc.player.getTilePos()
mc.postToChat(playerPosition)
