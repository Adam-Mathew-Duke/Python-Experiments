name = "Gandalf the White Timetwister Tundra The Tabernacle at Pendrell Vale Murktide Regent Mana Crypt"
cost = 1599.50, 4446.50, 4199.99, 3400.27, 3307.50, 3098.17
print (name[0:17] +": $"+ str(cost[0]) + "\n" + name[18:29] +": $"+ str(cost[1]))
print (name[30:36] +": $"+ str(cost[2]) + "\n" + name[37:68] +": $"+ str(cost[3]))
print (name[69:84] +": $"+ str(cost[4]) + "\n" + name[85:] +": $"+ str(cost[5]))
print ("=" * 10 + "\n" + f"Total Cost: ${cost[0]+cost[1]+cost[2]+cost[3]+cost[4]+cost[5]}")
