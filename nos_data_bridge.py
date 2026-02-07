class DataBridge:
    def __init__(self):
        self.supported_sources = ["Telebirr", "CBE", "Abyssinia"]

    def transform_to_nos(self, raw_data):
        """
        ከባንክ የመጣን ጥሬ መረጃ (Raw Data) ለ AI እንዲመች አድርጎ መቀየር
        """
        # መረጃውን የማጽዳት እና የማስተካከያ ሂደት
        formatted_data = {
            "origin": raw_data.get("sender_id"),
            "target": raw_data.get("receiver_id"),
            "val": float(raw_data.get("amount", 0)),
            "timestamp": raw_data.get("time")
        }
        return formatted_data

# አጠቃቀም (Example)
bridge = DataBridge()
raw_bank_info = {"sender_id": "ACC123", "receiver_id": "ACC789", "amount": "50000", "time": "2024-03-01"}
print(bridge.transform_to_nos(raw_bank_info))
