import networkx as nx

# 1-NOS Sentinel-X: The Neural Guard Core
class SentinelXCore:
    def __init__(self):
        # የፋይናንስ መረብ ግንባታ (Neural Mesh)
        self.financial_mesh = nx.DiGraph()

    def analyze_flow(self, sender, receiver, amount):
        # ዝውውሩን ወደ ሲስተሙ ማስገቢያ
        self.financial_mesh.add_edge(sender, receiver, weight=amount)
        
        # የረቀቀ የክበብ ዝውውር መለያ (Illicit Loop Detection)
        # ይህ በአጭር ጊዜ ውስጥ ትልቅ የገንዘብ ማጠብ ወንጀልን ይለያል
        try:
            illicit_loop = nx.find_cycle(self.financial_mesh, orientation="original")
            return f"🚨 CRITICAL ALERT: Illicit Loop Detected! Path: {illicit_loop}"
        except nx.NetworkXNoCycle:
            return "✅ Transaction Secured: 1-NOS Monitoring Active."

# የሲስተሙን ብቃት መፈተኛ (Simulation)
nos = SentinelXCore()
print(nos.analyze_flow("User_A", "User_B", 100000))
print(nos.analyze_flow("User_B", "User_C", 100000))
print(nos.analyze_flow("User_C", "User_A", 100000)) # እዚህ ጋር ሰንሰለቱን ይይዘዋል!
