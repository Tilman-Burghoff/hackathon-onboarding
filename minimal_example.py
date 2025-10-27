import robotic as ry

C = ry.Config()
C.addFile(ry.raiPath("scenarios/pandasTable.g"))

bot = ry.BotOp(C, useRealRobot=True)

qHome = bot.get_qHome()
bot.moveTo(qHome + 0.1)
bot.wait(C)
bot.home(C)