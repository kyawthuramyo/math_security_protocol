class LocalReverseTransformer:
    def __init__(self, chunk_size: int = 16):
        """
        Initialize the Local Reverse Transformer with a specific chunk size.
        သတ်မှတ်ထားသော chunk_size ဖြင့် LocalReverseTransformer ကို စတင်ခြင်း။
        """
        self.chunk_size = chunk_size

    def reverse_chunks(self, encrypted_chunks: list[list[int]]) -> list[list[int]]:
        """
        Apply reverse coordinate transformation to restore original chunks.
        ဝှက်ထားသော Chunk များကို Inverse Math ဖြင့် မူလအခြေအနေသို့ ပြန်ဖော်ခြင်း (Decryption)။
        """
        decrypted_chunks = []
        
        # Loop through each encrypted chunk / Encrypted ဖြစ်နေသော Chunk တစ်ခုချင်းစီကို ဖြတ်သန်းခြင်း
        for chunk in encrypted_chunks:
            decrypted_chunk = []
            for i, val in enumerate(chunk):
                # Calculate the same mix factor used in encryption / Encryption တုန်းက သုံးခဲ့တဲ့ mix_factor ကို ပြန်တွက်ခြင်း
                mix_factor = 0 if i == 0 else (i * 3) % 256
                # Reverse the mathematical transformation / မူလတန်ဖိုးကို ပြန်ထုတ်ခြင်း
                original_val = (val - i - mix_factor) % 256
                decrypted_chunk.append(original_val)
                
            decrypted_chunks.append(decrypted_chunk)
            
        return decrypted_chunks