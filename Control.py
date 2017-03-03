import subprocess
import py4j
import time

# compilation = subprocess.Popen(["javac -cp py4j0.10.4.jar:JOpenShowVar-core.jar:. ClientEntryPoint.java"], shell=True)
# run = subprocess.Popen(["java -cp py4j0.10.4.jar:JOpenShowVar-core.jar:. ClientEntryPoint"], shell=True)

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
client = gateway.entry_point.getClient()
print(client.simpleRead("$OV_PRO"))
client.simpleWrite("$OV_PRO", "50")
print(client.simpleRead("$OV_PRO"))

# print(client.readVariable("$OV_JOG"))



# while True:
# 	# client.simpleRead("$OV_JOG")
# 	# print(p)
# 	print(client.simpleRead("$POS_ACT"))
# 	time.sleep(.1)

