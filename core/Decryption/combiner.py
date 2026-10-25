class Combiner:
    def __init__(self):
        """
        Initialize the Combiner.
        Combiner ကို စတင်ခြင်း။
        """
        pass

    def to_text(self, decrypted_chunks: list[list[int]]) -> str:
        """
        Combine decrypted integer chunks back into plaintext string.
        ዲကုဒ်လုပ်ထားသော byte chunks များကို မူလစာသား string အဖြစ်သို့ ပြန်လည်ပေါင်းစပ်ခြင်း။
        """
        flat_bytes = []
        for chunk in decrypted_chunks:
            # Remove padding (zeros) if necessary / လိုအပ်ပါက padding (zeros) များကို ဖယ်ရှားခြင်း
            clean_chunk = [b for b in chunk if b != 0]
            flat_bytes.extend(clean_chunk)
        
        # Convert bytes back to string / bytes များကို string သို့ ပြန်ပြောင်းခြင်း
        restored_text = bytes(flat_bytes).decode('utf-8', errors='ignore')
        return restored_text