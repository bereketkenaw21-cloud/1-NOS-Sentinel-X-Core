import numpy as np

class SentinelAIEngine:
    def __init__(self):
        # የጥቁር ገበያ መለያ ነጥቦች (Weights)
        self.risk_threshold = 0.75 

    def calculate_risk_score(self, frequency, avg_amount, new_connections):
        """
        frequency: በሰዓት ስንት ጊዜ ተላከ
        avg_amount: አማካይ የተላከው ብር
        new_connections: ለመጀመሪያ ጊዜ የተላከላቸው ሰዎች ብዛት
        """
        # ረቂቅ የ AI ስሌት (Behavioral Scoring)
        # አነስተኛ ብር ለብዙ አዳዲስ ሰዎች መላክ ከፍተኛ ስጋት (Risk) ነው
        risk_index = (frequency * 0.4) + (new_connections * 0.5) - (avg_amount * 0.1)
        normalized_score = 1 / (1 + np.exp(-risk_index)) # Sigmoid function ለትክክለኛ ውጤት
        
        return round(normalized_score, 4)

# የ AI ሞዴሉን መፈተኛ
ai_guard = SentinelAIEngine()

# ተጠቃሚ 1፦ መደበኛ ሰው (በቀን 1 ጊዜ 5000 ብር ለታወቀ ሰው የሚልክ)
score1 = ai_guard.calculate_risk_score(frequency=1, avg_amount=5000, new_connections=0)
print(f"User 1 Risk Score: {score1} (Safe ✅)")

# ተጠቃሚ 2፦ የጥቁር ገበያ ነጋዴ (በሰዓት 20 ጊዜ 100 ብር ለማያውቃቸው ሰዎች የሚልክ)
score2 = ai_guard.calculate_risk_score(frequency=20, avg_amount=100, new_connections=15)
print(f"User 2 Risk Score: {score2} (🚨 High Risk - Black Market Suspect)")
