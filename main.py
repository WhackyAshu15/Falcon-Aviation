import xpc
client = xpc.XPlaneConnect()
position = client.getPOSI()
print("Latitude: %.4f, Longitude: %.4f, Altitude: %.4f"\
     % (position[0],position[1],position[2]))


