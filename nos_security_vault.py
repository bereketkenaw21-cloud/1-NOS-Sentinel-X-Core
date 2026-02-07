import hashlib

class SecurityVault:
    def __init__(self):
        # ብሔራዊ ሚስጥራዊ ቁልፍ (Secret Salt)
        self.national_salt = "ET_NOS_SHIELD_2024"

    def protect_identity(self, account_id):
        """
        የባለቤቱን ማንነት ወደ ረቂቅ ኮድ መቀየር (SHA-256 Encryption)
        """
        raw_data = account_id + self.national_salt
        # መረጃውን የማይመለስ ሚስጥራዊ ኮድ ማድረግ
        secure_hash = hashlib.sha256(raw_data.encode()).hexdigest()
        return f"🔐 ENCRYPTED_ID: {secure_hash[:20]}..."

# አጠቃቀም (Example)
vault = SecurityVault()
print(vault.protect_identity("CBE-1000234567"))
