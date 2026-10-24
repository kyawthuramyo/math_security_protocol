class DataCombiner:
    def __init__(self):
        """
        Initialize the DataCombiner.
        DataCombiner ကို စတင်ခြင်း။
        """
        pass

    def combine_and_restore(self, low_level_chunks: list[list[int]]) -> str:
        """
        Combine low-level integer arrays and restore them back to high-level string (Plaintext).
        Low-level integer arrays များကို ပြန်လည်ပေါင်းစပ်ပြီး မူလ High-level String အဖြစ်သို့ ပြန်ပြောင်းမည်။
        """
        # 1. Flatten/extend all chunks back together / ခွဲထားသော Array အားလုံးကို တစ်ခုတည်းဖြစ်အောင် ပြန်ဆက်ခြင်း
        all_bytes = []
        for chunk in low_level_chunks:
            all_bytes.extend(chunk)
            
        # 2. Convert bytes back to high-level string / Bytes များကို မူလ High-level String သို့ ပြန်ပြောင်းခြင်း
        restored_text = bytes(all_bytes).decode('utf-8', errors='ignore')
        return restored_text