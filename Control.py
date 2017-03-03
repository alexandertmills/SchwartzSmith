import subprocess

compilation = subprocess.Popen(["javac -cp py4j0.10.4.jar:JOpenShowVar-core.jar:. ClientEntryPoint.java"], shell=True)
run = subprocess.Popen(["java -cp py4j0.10.4.jar:JOpenShowVar-core.jar:. ClientEntryPoint"], shell=True)

from py4j.java_gateway import JavaGateway
gateway = JavaGateway()
client = gateway.entry_point.getClient()
print("thing goes here")
while True:
	pass