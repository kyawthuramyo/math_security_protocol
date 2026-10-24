class LocalForwardTransformer:
    def __init__(self, chunk_size: int = 16):
        """
        Initialize the Local Forward Transformer with a specific chunk size.
        သတ်မှတ်ထားသော chunk_size ဖြင့် LocalForwardTransformer ကို စတင်ခြင်း။
        """
        self.chunk_size = chunk_size

    def transform_chunks(self, low_level_chunks: list[list[int]]) -> list[list[int]]:
        """
        Apply forward coordinate transformation and index mixing to all chunks.
        Chunk တစ်ခုချင်းစီကို နေရာအလိုက် Index-mixing နဲ့ coordinate transformation ပြုလုပ်၍ ဝှက်ခြင်း (Encryption)။
        """
        encrypted_chunks = []
        
        # Loop through each chunk / Chunk တစ်ခုချင်းစီကို ဖြတ်သန်းခြင်း
        for chunk in low_level_chunks:
            encrypted_chunk = []
            for i, val in enumerate(chunk):
                # Calculate mix factor / mix_factor ကို တွက်ချက်ခြင်း
                mix_factor = 0 if i == 0 else (i * 3) % 256
                # Apply mathematical transformation / သင်္ချာနည်းအရ အသွင်ပြောင်းခြင်း
                transformed_val = (val + i + mix_factor) % 256
                encrypted_chunk.append(transformed_val)
                
            encrypted_chunks.append(encrypted_chunk)
            
        return encrypted_chunks