# =====================================================================
# [EN] Sender Validator Layer: Pre-checks outgoing chunks and metadata 
#      integrity before injection and network transmission.
# [MY] Sender Validator အလွှာ- အတုမထည့်မီနှင့် Network ပေါ်သို့ မပို့ခင် 
#      ထွက်လာမည့် Chunks များနှင့် Metadata များကို ကြိုတင်စစ်ဆေးခြင်း။
# =====================================================================

class SenderValidator:
    def __init__(self, expected_chunk_count: int = None):
        """
        [EN] Initialize the Sender Validator.
        [MY] Sender Validator ကို စတင်ခြင်း။
        """
        self.expected_chunk_count = expected_chunk_count

    def validate_outgoing_stream(self, chunks: list[list[int]]) -> bool:
        """
        [EN] Validates that outgoing chunks are not empty and structurally sound.
        [MY] ထွက်လာမည့် Chunks များသည် ဗလာမဖြစ်ဘဲ ဖွဲ့စည်းပုံ မှန်ကန်ကြောင်း စစ်ဆေးသည်။
        """
        if not chunks:
            raise ValueError("[SENDER SECURITY ERROR] Outgoing chunk stream is empty!")
        
        for idx, chunk in enumerate(chunks):
            if not isinstance(chunk, list) or len(chunk) == 0:
                raise ValueError(f"[SENDER SECURITY ERROR] Malformed chunk detected at index {idx}!")
                
        return True