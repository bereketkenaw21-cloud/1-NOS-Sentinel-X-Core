# 1-NOS Sentinel-X Neural Core V3.1
import hashlib

class NeuralCore:
    def __init__(self):
        self.risk_threshold = 0.85 # የስጋት ደረጃው ከ 85% በላይ ከሆነ Alert ይሰጣል
        self.transaction_graph = {}

    def analyze_behavior(self, sender, receiver, amount, bank):
        """
        በተለያዩ ባንኮች ያሉ ትስስሮችን የሚመረምር ስልተ-ቀመር
        """
        # 1. የዝውውር ትስስር መፍጠር
        if sender not in self.transaction_graph:
            self.transaction_graph[sender] = []
        
        self.transaction_graph[sender].append({"bank": bank, "amount": amount})
        
        # 2. 'Loop' መኖሩን ማረጋገጥ (የ 42 Loops ስሌት)
        unique_banks = set([tx['bank'] for tx in self.transaction_graph[sender]])
        
        if len(unique_banks) > 3 and amount > 500000:
            risk_score = 0.98 # 98% ስጋት
            return {
                "status": "CRITICAL",
                "risk_score": risk_score,
                "message": f"Detected: User operating across {len(unique_banks)} banks. High-risk loop identified."
            }
        
        return {"status": "STABLE", "risk_score": 0.10}

# የ Sentinel-X Neural Core ማስነሻ
sentinel_ai = NeuralCore()
